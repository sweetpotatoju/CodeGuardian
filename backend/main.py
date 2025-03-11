from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from backend.DB.base import SessionLocal
from fastapi.middleware.cors import CORSMiddleware


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# CORS 설정 추가 (모든 도메인 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안 이슈 있을 수 있음)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


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
