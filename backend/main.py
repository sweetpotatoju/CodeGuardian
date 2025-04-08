import os

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from starlette.responses import HTMLResponse

from backend.DB.base import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import UploadFile, File
from fastapi.requests import Request
from models.inference import analyze_all


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
# CORS 설정 추가 (모든 도메인 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안 이슈 있을 수 있음)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/check-db")
def check_db_connection(db: Session = Depends(get_db)):  # ✅ get_db() 사용
    try:
        result = db.execute(text("SELECT version();"))
        version = result.fetchone()
        return {"status": "success", "postgresql_version": version[0]}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.get("/analyze_page", response_class=HTMLResponse)
async def admin_login_web(request: Request):
    return templates.TemplateResponse("mainpage.html", {"request": request})


@app.post("/analyze")
async def analyze_code_file(file: UploadFile = File(...)):
    contents = await file.read()
    code = contents.decode("utf-8")
    result = analyze_all(code)
    return result
