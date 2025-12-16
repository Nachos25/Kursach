from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import auth as auth_router
from .routers import products as products_router
from .routers import orders as orders_router
from .routers import assets as assets_router
from sqlalchemy import text

# Create DB schema on startup (SQLite, simple demo)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tech Store API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(products_router.router)
app.include_router(orders_router.router)
app.include_router(assets_router.router)


@app.get("/api/health")
def health():
    return {"status": "ok"}


# Ensure new columns exist (very light migration for SQLite)
with engine.begin() as conn:
    # add users.username if missing
    cols = [r[1] for r in conn.exec_driver_sql("PRAGMA table_info(users);").all()]
    if "username" not in cols:
        conn.exec_driver_sql("ALTER TABLE users ADD COLUMN username VARCHAR(255);")
        # backfill username with email prefix if possible
        conn.exec_driver_sql("UPDATE users SET username = COALESCE(username, email);")




