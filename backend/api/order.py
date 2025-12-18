from fastapi import APIRouter, Request, Header, HTTPException
from service.order_service import OrderService
from pydantic import BaseModel
from typing import Optional
import uuid
import time

router = APIRouter()
service = OrderService()

# Простий in-memory rate-limit: IP -> [timestamps]
rate_limit: dict[str, list[float]] = {}
WINDOW_SEC = 10
MAX_REQ = 8

class OrderCreateRequest(BaseModel):
    title: str

class OrderResponse(BaseModel):
    id: str
    title: str
    requestId: str

class ErrorResponse(BaseModel):
    error: str
    code: Optional[str] = None
    details: Optional[list] = None
    requestId: str

# Middleware-like decorator для X-Request-Id та rate-limit
async def process_request(request: Request, func):
    rid = request.headers.get("X-Request-Id") or str(uuid.uuid4())
    ip = request.client.host
    # rate-limit
    timestamps = rate_limit.get(ip, [])
    now_ts = time.time()
    timestamps = [t for t in timestamps if now_ts - t < WINDOW_SEC]
    if len(timestamps) >= MAX_REQ:
        return ErrorResponse(
            error="too_many_requests",
            code=None,
            details=None,
            requestId=rid
        ), 429
    timestamps.append(now_ts)
    rate_limit[ip] = timestamps
    # call handler
    return await func(rid)

# POST /orders
@router.post("/orders", response_model=OrderResponse, status_code=201)
async def create_order(
    req: OrderCreateRequest,
    request: Request,
    idempotency_key: Optional[str] = Header(None),
):
    async def handler(rid):
        try:
            order = service.create_order(req.title, idempotency_key)
            return OrderResponse(id=order.id, title=order.title, requestId=rid)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    resp, status = await process_request(request, handler)
    from fastapi.responses import JSONResponse
    if isinstance(resp, ErrorResponse):
        return JSONResponse(content=resp.dict(), status_code=status)
    return resp

# GET /health
@router.get("/health")
async def health():
    return {"status": "ok"}
