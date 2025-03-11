import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# .env 파일 로드
load_dotenv()

# 환경변수에서 DATABASE_URL 가져오기
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, connect_args={"options": "-c client_encoding=UTF8"})

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델 베이스 클래스
Base = declarative_base()
