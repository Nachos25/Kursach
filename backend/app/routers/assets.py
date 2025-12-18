from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse, FileResponse
import httpx
from pathlib import Path
from typing import Literal

ALLOWED_EXTENSIONS: tuple[Literal["png", "jpg", "jpeg", "webp", "gif", "svg"], ...] = (
    "png",
    "jpg",
    "jpeg",
    "webp",
    "gif",
    "svg",
)

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


@router.get("/images/{filename}")
def serve_local_image(filename: str):
    # Безопасность: не позволяем подниматься по директориям
    if Path(filename).name != filename:
        raise HTTPException(status_code=400, detail="Invalid filename")
    ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Unsupported image extension")

    # Корень проекта (из файла routers/assets.py -> app -> backend -> <root>)
    repo_root = Path(__file__).resolve().parents[3]
    file_path = repo_root / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Image not found")

    return FileResponse(str(file_path))



