<div align="center">

# 🎩 Sherlock Holmes QA Bot
# 🎩 셜록 홈즈 QA 챗봇

**Sherlock Holmes Universe-Based LoRA Fine-tuned QA Chatbot**  
**셜록 홈즈 세계관 기반 LoRA 파인튜닝 QA 챗봇**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![HuggingFace](https://img.shields.io/badge/🤗-Transformers-FFD21E?style=flat)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)

A lightweight AI chatbot that provides specialized question-answering performance focused on Sherlock Holmes by fine-tuning the Google Gemma-2-2B-IT model using the LoRA method.

Includes a web-based demo UI and FastAPI server, allowing you to run the **SHERLOCK chatbot** immediately in your local environment.

Google Gemma-2-2B-IT 모델을 LoRA 방식으로 파인튜닝하여 셜록 홈즈에 특화된 질의응답 성능을 제공하는 경량 AI 챗봇입니다.

웹 기반 데모 UI와 FastAPI 서버를 포함하고 있어 로컬 환경에서 바로 **SHERLOCK 챗봇**을 실행할 수 있습니다.

[Demo](#-quick-start) • [Features](#-features) • [API Docs](#-api-endpoints)

<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">

</div>

---

## 🚀 Features | 주요 기능

<table>
<tr>
<td>

### ✨ **Key Features | 핵심 기능**

**English:**
- 🧠 Gemma-2-2B-IT + LoRA(PEFT) based Sherlock-Holmes QA model
- 📥 Automatic model loading from HuggingFace Hub
- ⚡ FastAPI + Uvicorn REST API server
- 🎨 All-in-one Web UI (Victorian era theme, embedded CSS/JS)
- 📚 Health check / Automatic Swagger documentation
- 💻 Executable even in CPU environments

**한국어:**
- 🧠 Gemma-2-2B-IT + LoRA(PEFT) 기반 Sherlock-Holmes QA 모델
- 📥 HuggingFace Hub 자동 모델 로딩
- ⚡ FastAPI + Uvicorn REST API 서버
- 🎨 올인원 웹 UI (빅토리아 시대 테마, CSS/JS 내장)
- 📚 헬스체크 / Swagger 문서 자동 제공
- 💻 CPU 환경에서도 실행 가능

</td>
</tr>
</table>

---

## 📦 Quick Start | 빠른 시작

### 1️⃣ Installation | 설치

```bash
# Clone repository | 저장소 복제
git clone https://github.com/your-username/sherlock-qa-bot.git
cd sherlock-qa-bot

# Install dependencies | 의존성 설치
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI Server | FastAPI 서버 실행

**Option 1: Simple Run | 옵션 1: 간단 실행**
```bash
python run.py
```

**Option 2: Manual Run | 옵션 2: 수동 실행**
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 3️⃣ Access the Chatbot UI | 챗봇 UI 접속

**English:** Open your browser and navigate to:  
**한국어:** 브라우저에서 다음 주소로 접속하세요:

```
🌐 Web UI:     http://localhost:8000
📚 API Docs:   http://localhost:8000/docs
📖 ReDoc:      http://localhost:8000/redoc
❤️  Health:     http://localhost:8000/health
```

---

## 🔌 API Endpoints | API 엔드포인트

| Method | Endpoint | Description (EN) | 설명 (KR) |
|--------|----------|------------------|-----------|
| `GET` | `/` | Web Chat UI | 웹 채팅 UI |
| `POST` | `/ask` | Ask Sherlock (configurable max_tokens, temperature) | 셜록에게 질문하기 (max_tokens, temperature 설정 가능) |
| `GET` | `/health` | Check server & model status | 서버 & 모델 상태 확인 |
| `GET` | `/docs` | Swagger documentation | Swagger 문서 |

### 📝 Request Example | 요청 예시

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Who is Dr. Watson?",
    "max_tokens": 300,
    "temperature": 0.7
  }'
```

### 📤 Response Example | 응답 예시

```json
{
  "question": "Who is Dr. Watson?",
  "answer": "Dr. John H. Watson is Holmes's trusted companion and chronicler...",
  "context": null
}
```

---

## 🧠 Model | 모델

<div align="center">

| Component | Details |
|-----------|---------|
| **Base Model | 기본 모델** | [`google/gemma-2-2b-it`](https://huggingface.co/google/gemma-2-2b-it) |
| **LoRA Model | LoRA 모델** | [`Sung1Lim/sherlock-holmes-qa`](https://huggingface.co/Sung1Lim/sherlock-holmes-qa) |
| **Dataset | 데이터셋** | [`Alleinzellgaenger/sherlock-holmes-qa`](https://huggingface.co/datasets/Alleinzellgaenger/sherlock-holmes-qa) |
| **Fine-Tuning | 파인튜닝** | PEFT LoRA (r=16, alpha=32) |
| **Training Loss | 학습 손실** | 1.46 → 0.52 |
| **Validation Loss | 검증 손실** | 0.85 → 0.74 |

</div>

> 💡 **Auto-loading (EN)**: Automatically downloads and loads checkpoints from HuggingFace Hub when running FastAPI.  
> 💡 **자동 로딩 (KR)**: FastAPI 실행 시 HuggingFace Hub에서 자동으로 체크포인트를 다운로드하여 로딩합니다.

---

## 🏗️ Project Structure | 프로젝트 구조

```
sherlock-qa-bot/
│
├── 📁 api/
│   ├── main.py              # FastAPI endpoints + Web UI | FastAPI 엔드포인트 + 웹 UI
│   ├── model.py             # Gemma + LoRA loading & inference | Gemma + LoRA 로딩 & 추론
│   └── schemas.py           # Request/Response schemas | Request/Response 구조체
│
├── 📁 templates/
│   └── index.html           # Web-based chat UI (incl. CSS/JS) | 웹 기반 채팅 UI (CSS/JS 포함)
│
├── 📁 scripts/
│   └── client.py            # API test script | API 테스트 스크립트
│
├── 📁 notebooks/
│   └── train_sherlock.ipynb # LoRA training notebook | LoRA 학습 노트북
│
├── run.py                   # Server execution script | 서버 실행 스크립트
├── requirements.txt         # Python package list | Python 패키지 목록
└── README.md
```

> 💡 **Note (EN)**: The `templates/index.html` file contains all styles (CSS) and scripts (JavaScript), eliminating the need for a separate static folder.  
> 💡 **참고 (KR)**: `templates/index.html` 파일에 모든 스타일(CSS)과 스크립트(JavaScript)가 포함되어 있어 별도의 static 폴더가 필요하지 않습니다.

---

## 🛠️ Tech Stack | 기술 스택

<div align="center">

### Core Technologies | 핵심 기술

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face-FFD21E?style=for-the-badge&logoColor=black)

### Libraries & Frameworks | 라이브러리 및 프레임워크

| Category (EN) | 카테고리 (KR) | Technologies | 기술 |
|---------------|--------------|--------------|------|
| **Language** | **언어** | Python 3.10+ | Python 3.10+ |
| **Deep Learning** | **딥러닝** | PyTorch 2.x, Transformers | PyTorch 2.x, Transformers |
| **Fine-Tuning** | **파인튜닝** | PEFT (LoRA) | PEFT (LoRA) |
| **API Server** | **API 서버** | FastAPI, Uvicorn | FastAPI, Uvicorn |
| **Frontend** | **프론트엔드** | HTML5, CSS3, JavaScript (Single-file) | HTML5, CSS3, JavaScript (단일 파일) |
| **Templating** | **템플릿** | Jinja2 | Jinja2 |
| **Development** | **개발** | Jupyter Notebook | Jupyter Notebook |

</div>

---

## 💡 Usage Examples | 사용 예시

### Python Client | Python 클라이언트

```python
from scripts.client import ask_sherlock

# Ask a question | 질문하기
question = "Who is Irene Adler?"
answer = ask_sherlock(question)
print(answer)
```

### cURL

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is the significance of the hound of the Baskervilles?",
    "max_tokens": 300,
    "temperature": 0.7
  }'
```

### JavaScript (Fetch API)

```javascript
const response = await fetch('http://localhost:8000/ask', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ 
    question: 'Who is Professor Moriarty?',
    max_tokens: 300,
    temperature: 0.7
  })
});

const data = await response.json();
console.log(data.answer);
```

---

## 📊 Performance | 성능

| Metric (EN) | 지표 (KR) | Before | After | Improvement | 개선율 |
|-------------|-----------|--------|-------|-------------|--------|
| Training Loss | 학습 손실 | 1.46 | 0.52 | ⬇️ 64.4% | ⬇️ 64.4% |
| Validation Loss | 검증 손실 | 0.85 | 0.74 | ⬇️ 12.9% | ⬇️ 12.9% |
| Model Size | 모델 크기 | ~5GB | ~50MB | ⬇️ 99% (LoRA) | ⬇️ 99% (LoRA) |
| Inference Speed | 추론 속도 | - | ~2-3s | CPU-friendly | CPU 친화적 |

---

## 📄 License | 라이선스

**English:** This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**한국어:** 이 프로젝트는 **MIT 라이선스** 하에 배포됩니다 - 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

---

## 💬 Contact & Support | 연락처 및 지원

<div align="center">

**English:** For suggestions or questions about the project, please open a GitHub Issue!  
**한국어:** 프로젝트 관련 제안이나 질문은 GitHub Issues로 남겨주세요!

[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-181717?style=for-the-badge&logo=github)](https://github.com/your-username/sherlock-qa-bot/issues)
[![HuggingFace](https://img.shields.io/badge/🤗-Model_Card-FFD21E?style=for-the-badge)](https://huggingface.co/Sung1Lim/sherlock-holmes-qa)

---

### ⭐ Star this project if you find it useful! | 유용하다면 프로젝트에 Star를 눌러주세요!

Made with ❤️ by [Sung1Lim](https://github.com/Sung1Lim)

</div>