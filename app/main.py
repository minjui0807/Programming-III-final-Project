from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import Base, engine
from app.routers import expenses
from app.config import settings
import os

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    # ... (資料庫部分保留不變) ...
    Base.metadata.create_all(bind=engine)
    app.include_router(expenses.router, prefix="/api/v1")

    # 前端靜態檔案路徑
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
    
    # ⭐ 關鍵修正：將 StaticFiles 掛載到根目錄 "/"
    # 這樣 /transaction.html, /recordpage.html 才能被伺服器找到
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="static")

    # 設定根目錄 / 打開 index.html
    # 由於上面已經用 StaticFiles 掛載了，其實這行可以省略，
    # 但為了明確性，保留 FileResponse
    @app.get("/")
    def root():
        return FileResponse(os.path.join(frontend_path, "index.html"))

    return app

app = create_app()