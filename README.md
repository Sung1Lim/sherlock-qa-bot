🎩 Sherlock Holmes QA Bot

셜록 홈즈(Sherlock Holmes) 세계관 기반의 질의응답 AI 챗봇
Google Gemma-2-2B-IT 모델을 LoRA 방식으로 파인튜닝하여 구축했습니다.

📋 프로젝트 개요

Base Model: Google Gemma-2-2B-IT

Fine-Tuning: LoRA (PEFT)

Dataset: 커스텀 Sherlock QA 데이터셋

Serving: FastAPI 기반 REST API 서버

Inference: 실시간 답변 생성 API 제공

HuggingFace 모델: Sung1Lim/sherlock-holmes-qa

🚀 빠른 시작
1. 설치
pip install -r requirements.txt

2. 모델 다운로드 / 로딩 방식

학습된 LoRA 모델은 코드에 포함되지 않습니다.
FastAPI 서버 실행 시 Hugging Face Hub에서 자동으로 다운로드됩니다.

➡️ 사용 모델:
google/gemma-2-2b-it
Sung1Lim/sherlock-holmes-qa

따라서 별도의 수동 다운로드는 필요 없습니다.

3. API 실행
python run.py


또는 수동 실행:

uvicorn api.main:app --reload --host 0.0.0.0 --port 8000


브라우저에서 확인:

http://localhost:8000
http://localhost:8000/docs
http://localhost:8000/redoc
http://localhost:8000/health

💬 사용 예시 (curl)
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Who is Dr. Watson?"}'


응답 예시:

{
  "question": "Who is Dr. Watson?",
  "answer": "Dr. John H. Watson was Holmes's close friend...",
  "context": null
}

🧑‍💻 Python 사용 예시
from scripts.clients import ask_sherlock

question = "Who is Irene Adler?"
answer = ask_sherlock(question)
print(answer)

📊 학습 결과 (요약)

Training Loss: 1.46 → 0.52

Validation Loss: 0.85 → 0.74

Epochs: 5epochs

PEFT LoRA 적용으로 빠르고 경량화된 학습 수행

🏗️ 프로젝트 구조
sherlock-qa-bot/
│
├── api/
│   ├── main.py              # FastAPI 엔드포인트
│   ├── model.py             # Gemma + LoRA 모델 로딩 & 추론
│   └── schemas.py           # Request/Response 모델
│
├── notebooks/
│   └── train_sherlock.ipynb # LoRA 학습 노트북
│
├── models/                  # (optional) 로컬 저장 시 사용
│
├── scripts/
│   └── clients.py           # API 테스트 클라이언트
│
├── run.py                   # FastAPI 서버 실행 스크립트
├── requirements.txt         # 패키지 목록
└── README.md

🛠️ 기술 스택

Python 3.10+

PyTorch 2.x

HuggingFace Transformers

PEFT (LoRA)

FastAPI

Uvicorn

Jupyter Notebook



📄 라이센스

MIT License