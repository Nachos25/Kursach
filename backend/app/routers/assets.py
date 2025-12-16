from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
import httpx

router = APIRouter(prefix="/api", tags=["assets"])


@router.get("/proxy")
async def proxy_image(url: str = Query(..., description="Absolute image URL")):
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=10) as client:
            resp = await client.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if resp.status_code >= 400:
                raise HTTPException(status_code=resp.status_code, detail="Image fetch error")
            content_type = resp.headers.get("content-type", "image/jpeg")
            return StreamingResponse(iter([resp.content]), media_type=content_type)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Proxy failed: {e}")



