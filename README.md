<div align="center">

# 🎩 Sherlock Holmes QA Bot

**셜록 홈즈 세계관 기반 LoRA 파인튜닝 QA 챗봇**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?style=flat&logo=pytorch&logoColor=white)](https://pytorch.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![HuggingFace](https://img.shields.io/badge/🤗-Transformers-FFD21E?style=flat)](https://huggingface.co)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat)](LICENSE)

Google Gemma-2-2B-IT 모델을 LoRA 방식으로 파인튜닝하여 셜록 홈즈에 특화된 질의응답 성능을 제공하는 경량 AI 챗봇입니다.

웹 기반 데모 UI와 FastAPI 서버를 포함하고 있어 로컬 환경에서 바로 **SHERLOCK 챗봇**을 실행할 수 있습니다.

[Demo](#-quick-start) • [Features](#-features) • [API Docs](#-api-endpoints)

<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">

</div>

---

## 🚀 Features

<table>
<tr>
<td>

✨ **핵심 기능**
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

## 📦 Quick Start

### 1️⃣ Installation

```bash
# Clone repository
git clone https://github.com/your-username/sherlock-qa-bot.git
cd sherlock-qa-bot

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI Server

**Option 1: Simple Run**
```bash
python run.py
```

**Option 2: Manual Run**
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 3️⃣ Access the Chatbot UI

브라우저에서 다음 주소로 접속하세요:

```
🌐 Web UI:     http://localhost:8000
📚 API Docs:   http://localhost:8000/docs
📖 ReDoc:      http://localhost:8000/redoc
❤️  Health:     http://localhost:8000/health
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | 웹 채팅 UI |
| `POST` | `/ask` | 셜록에게 질문하기 (max_tokens, temperature 설정 가능) |
| `GET` | `/health` | 서버 & 모델 상태 확인 |
| `GET` | `/docs` | Swagger 문서 |

### 📝 Request Example

```bash
curl -X POST "http://localhost:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Who is Dr. Watson?",
    "max_tokens": 300,
    "temperature": 0.7
  }'
```

### 📤 Response Example

```json
{
  "question": "Who is Dr. Watson?",
  "answer": "Dr. John H. Watson is Holmes's trusted companion and chronicler...",
  "context": null
}
```

---

## 🧠 Model

<div align="center">

| Component | Details |
|-----------|---------|
| **Base Model** | [`google/gemma-2-2b-it`](https://huggingface.co/google/gemma-2-2b-it) |
| **LoRA Model** | [`Sung1Lim/sherlock-holmes-qa`](https://huggingface.co/Sung1Lim/sherlock-holmes-qa) |
| **Dataset** | 커스텀 Sherlock Holmes QA 데이터셋 |
| **Fine-Tuning** | PEFT LoRA (r=16, alpha=32) |
| **Training Loss** | 1.46 → 0.52 |
| **Validation Loss** | 0.85 → 0.74 |

</div>

> 💡 **자동 로딩**: FastAPI 실행 시 HuggingFace Hub에서 자동으로 체크포인트를 다운로드하여 로딩합니다.

---

## 🏗️ Project Structure

```
sherlock-qa-bot/
│
├── 📁 api/
│   ├── main.py              # FastAPI 엔드포인트 + 웹 UI
│   ├── model.py             # Gemma + LoRA 로딩 & 추론
│   └── schemas.py           # Request/Response 구조체
│
├── 📁 templates/
│   └── index.html           # 웹 기반 채팅 UI (CSS/JS 포함)
│
├── 📁 scripts/
│   └── client.py            # API 테스트 스크립트
│
├── 📁 notebooks/
│   └── train_sherlock.ipynb # LoRA 학습 노트북
│
├── run.py                   # 서버 실행 스크립트
├── requirements.txt         # Python 패키지 목록
└── README.md
```

> 💡 **참고**: `templates/index.html` 파일에 모든 스타일(CSS)과 스크립트(JavaScript)가 포함되어 있어 별도의 static 폴더가 필요하지 않습니다.

---

## 🛠️ Tech Stack

<div align="center">

### Core Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![HuggingFace](https://img.shields.io/badge/🤗_Hugging_Face-FFD21E?style=for-the-badge&logoColor=black)

### Libraries & Frameworks

| Category | Technologies |
|----------|-------------|
| **Language** | Python 3.10+ |
| **Deep Learning** | PyTorch 2.x, Transformers |
| **Fine-Tuning** | PEFT (LoRA) |
| **API Server** | FastAPI, Uvicorn |
| **Frontend** | HTML5, CSS3, JavaScript (Single-file) |
| **Templating** | Jinja2 |
| **Development** | Jupyter Notebook |

</div>

---

## 💡 Usage Examples

### Python Client

```python
from scripts.client import ask_sherlock

# 질문하기
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

## 📊 Performance

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Training Loss | 1.46 | 0.52 | ⬇️ 64.4% |
| Validation Loss | 0.85 | 0.74 | ⬇️ 12.9% |
| Model Size | ~5GB | ~50MB | ⬇️ 99% (LoRA) |
| Inference Speed | - | ~2-3s | CPU-friendly |

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact & Support

<div align="center">

**프로젝트 관련 제안이나 질문은 GitHub Issues로 남겨주세요!**

[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-181717?style=for-the-badge&logo=github)](https://github.com/your-username/sherlock-qa-bot/issues)
[![HuggingFace](https://img.shields.io/badge/🤗-Model_Card-FFD21E?style=for-the-badge)](https://huggingface.co/Sung1Lim/sherlock-holmes-qa)

---

### ⭐ Star this project if you find it useful!

Made with ❤️ by [Sung1Lim](https://github.com/Sung1Lim)

</div>