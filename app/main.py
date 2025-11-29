import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import Base, engine
from app.routers import expenses
from app.config import settings

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

    # 修改首頁路由
    @app.get("/")
    def root():
        # 當使用者打開首頁時，回傳前端網頁
        return FileResponse('static/index.html')

    return app

app = create_app()

#啟動在終端機輸入:uvicorn app.main:app --reload