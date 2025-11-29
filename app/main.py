import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import Base, engine
from app.routers import expenses
from app.config import settings
import os

def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    # 自動建立資料表
    Base.metadata.create_all(bind=engine)

    # 掛載靜態檔案 (讓網頁可以讀取 CSS/JS)
    # 確保 static 資料夾存在
    if not os.path.exists("static"):
        os.makedirs("static")
        
    app.mount("/static", StaticFiles(directory="static"), name="static")

    # 掛載 Router
    # 注意：因為有加 prefix="/api/v1"，所以 API 路徑變成了 /api/v1/expenses
    app.include_router(expenses.router, prefix="/api/v1")

    # 前端靜態檔案路徑
    frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")
    app.mount("/frontend", StaticFiles(directory=frontend_path), name="frontend")

    # 設定根目錄 / 打開 index.html
    @app.get("/")
    def root():
        return FileResponse(os.path.join(frontend_path, "index.html"))

    return app

app = create_app()
