# 🎩 Sherlock Holmes QA Bot

셜록 홈즈 세계관 기반 질의응답 AI 챗봇

## 📋 프로젝트 개요

Google Gemma-2-2B-IT 모델을 LoRA 방식으로 파인튜닝하여 구축한 셜록 홈즈 전문 AI 챗봇입니다.

- **Base Model**: Google Gemma-2-2B-IT
- **Fine-Tuning**: LoRA (PEFT)
- **Dataset**: 커스텀 Sherlock Holmes QA 데이터셋
- **Serving**: FastAPI 기반 REST API 서버
- **HuggingFace**: [Sung1Lim/sherlock-holmes-qa](https://huggingface.co/Sung1Lim/sherlock-holmes-qa)


## 🚀 빠른 시작

### 설치

```bash
pip install -r requirements.txt
```

### 모델 다운로드

학습된 LoRA 모델은 FastAPI 서버 실행 시 HuggingFace Hub에서 자동으로 다운로드됩니다.

### API 서버 실행

```bash
python run.py
```

또는

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 접속

- http://localhost:8000
- http://localhost:8000/docs (API 문서)
- http://localhost:8000/health (헬스 체크)


## 📊 학습 결과

- **Training Loss**: 1.46 → 0.52
- **Validation Loss**: 0.85 → 0.74
- **Epochs**: 5
- PEFT LoRA 적용으로 빠르고 경량화된 학습 수행


## 🏗️ 프로젝트 구조

```
sherlock-qa-bot/
├── api/
│   ├── main.py          # FastAPI 엔드포인트
│   ├── model.py         # 모델 로딩 & 추론
│   └── schemas.py       # Request/Response 스키마
├── notebooks/
│   └── train_sherlock.ipynb  # LoRA 학습 노트북
├── scripts/
│   └── clients.py       # API 테스트 클라이언트
├── run.py               # 서버 실행 스크립트
├── requirements.txt
└── README.md
```


## 🛠️ 기술 스택

- Python 3.10+
- PyTorch 2.x
- HuggingFace Transformers
- PEFT (LoRA)
- FastAPI
- Uvicorn
- Jupyter Notebook


## 📄 라이센스

MIT License

## 📧 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 Issue를 생성해주세요.