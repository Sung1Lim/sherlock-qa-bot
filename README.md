# 🎩 Sherlock Holmes QA Bot

셜록 홈즈 스토리 기반 질의응답 AI 챗봇

## 📋 프로젝트 개요

- **모델**: Google Gemma-2-2B-IT
- **파인튜닝**: LoRA (Low-Rank Adaptation)
- **데이터**: HuggingFace sherlock-holmes-qa dataset
- **API**: FastAPI

## 🚀 빠른 시작

### 1. 설치

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 2. 모델 다운로드

학습된 모델은 용량 문제로 Git에 포함되지 않습니다.
[Google Drive 링크] 또는 [HuggingFace Hub]에서 다운로드하세요.

### 3. API 실행

\`\`\`bash
cd api
uvicorn main:app --reload
\`\`\`

브라우저에서 http://localhost:8000/docs 접속

## 📊 학습 결과

- Training Loss: 1.46 → 0.52
- Validation Loss: 0.85 → 0.74
- 학습 에폭: 5 epochs

## 🏗️ 프로젝트 구조

\`\`\`
sherlock-qa-bot/
├── notebooks/     # 학습 노트북
├── src/          # 학습/추론 코드
├── api/          # FastAPI 앱
└── models/       # 학습된 모델 (별도 다운로드)
\`\`\`

## 📝 사용 예시

\`\`\`python
from src.inference import ask_sherlock

question = "Who is Irene Adler?"
answer = ask_sherlock(question)
print(answer)
\`\`\`

## 🛠️ 기술 스택

- Python 3.10+
- PyTorch
- Transformers (HuggingFace)
- PEFT (LoRA)
- FastAPI

## 📄 라이센스

MIT License
\`\`\`

## 4. 모델 저장 위치 수정

학습 코드에서 출력 경로를 `models/` 폴더로 변경:

\`\`\`python
# 기존
output_dir="./sherlock-lora-final"

# 변경
output_dir="./models/sherlock-lora-final"
\`\`\`