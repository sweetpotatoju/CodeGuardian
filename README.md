# 🛡️ Software Reliability Assurance Agent

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=for-the-badge&logo=docker)

**Software Reliability Assurance Agent**는 소프트웨어의 신뢰성을 보증하기 위해 LLM 기반으로 **요구사항 및 설계 문서를 분석**하고, **코드의 결함을 예측 및 수정**하는 AI 시스템입니다.

---

## 📌 **기능 (Features)**
✅ **RAG 기반 문서 검색** → **요구사항 명세서 (SRS) 및 설계 문서 (SDS) 분석**  
✅ **코드 분석** → **파일 및 메소드 단위 결함 탐색**  
✅ **LLM 기반 결함 예측** → **Mamba-CCL, CodeBERT, SecureBERT 활용**  
✅ **자동 코드 수정** → **AI 기반 코드 수정 및 보안 강화**  
✅ **UI 연동** → **PyCharm Git Merge Tool과 유사한 코드 비교 및 수정 반영**  
✅ **FastAPI 기반 REST API** → **데이터 저장 및 분석 결과 반환**  
✅ **Docker 지원** → **손쉬운 배포 및 실행**


---

## 📂 **프로젝트 구조 (Project Structure)**

📌 **구성 요소 설명**  
- `backend/` → FastAPI 서버 및 API 관리  
- `models/` → LLM 기반 코드 분석 모델 저장  
- `database/` → 결함 분석 결과 및 벡터 검색 저장소
- scripts/ -> 생각 안해봄..  
- `tests/` → API 및 유닛 테스트  
