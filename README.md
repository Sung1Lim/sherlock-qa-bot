# 🎩 Sherlock Holmes QA Bot

**Sherlock Holmes Universe LoRA Fine-Tuned QA Chatbot**
<br>
**셜록 홈즈 세계관 기반 LoRA 파인튜닝 QA 챗봇**

[](https://www.python.org)
[](https://pytorch.org)
[](https://fastapi.tiangolo.com)
[](https://huggingface.co)
[](https://www.google.com/search?q=LICENSE)

A lightweight AI chatbot fine-tuned on the **Google Gemma-2-2B-IT** model using LoRA, specialized for answering questions within the Sherlock Holmes universe. It includes a web-based demo UI and a FastAPI server, allowing you to run the **SHERLOCK Chatbot** locally.

Google Gemma-2-2B-IT 모델을 LoRA 방식으로 파인튜닝하여 셜록 홈즈에 특화된 질의응답 성능을 제공하는 경량 AI 챗봇입니다. 웹 기반 데모 UI와 FastAPI 서버를 포함하고 있어 로컬 환경에서 바로 **SHERLOCK 챗봇**을 실행할 수 있습니다.

[Demo](https://www.google.com/search?q=%23-quick-start) • [Features](https://www.google.com/search?q=%23-features) • [API Docs](https://www.google.com/search?q=%23-api-endpoints)

\<img src="[https://img.shields.io/badge/Status-Active-success?style=for-the-badge](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)" alt="Status"\>

\</div\>

-----

## 🚀 Features

\<table\>
\<tr\>
\<td\>

✨ **Key Features (핵심 기능)**

  - 🧠 **Model**: Sherlock-Holmes QA model based on Gemma-2-2B-IT + LoRA (PEFT).
    <br>(Gemma-2-2B-IT + LoRA(PEFT) 기반 Sherlock-Holmes QA 모델)
  - 📥 **Auto-Load**: Automatic model loading from HuggingFace Hub.
    <br>(HuggingFace Hub 자동 모델 로딩)
  - ⚡ **Server**: FastAPI + Uvicorn REST API server.
    <br>(FastAPI + Uvicorn REST API 서버)
  - 🎨 **UI**: All-in-one Web UI (Victorian theme, CSS/JS included).
    <br>(올인원 웹 UI - 빅토리아 시대 테마, CSS/JS 내장)
  - 📚 **Docs**: Automatic Health Check / Swagger documentation.
    <br>(헬스체크 / Swagger 문서 자동 제공)
  - 💻 **Efficiency**: Capable of running in a CPU-only environment.
    <br>(CPU 환경에서도 실행 가능)

\</td\>
\</tr\>
\</table\>

-----

## 📦 Quick Start

### 1️⃣ Installation (설치)

```bash
# Clone repository
git clone https://github.com/your-username/sherlock-qa-bot.git
cd sherlock-qa-bot

# Install dependencies
pip install -r requirements.txt
```

### 2️⃣ Run FastAPI Server (서버 실행)

**Option 1: Simple Run (간편 실행)**

```bash
python run.py
```

**Option 2: Manual Run (수동 실행)**

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 3️⃣ Access the Chatbot UI (접속)

Open your browser and navigate to the following addresses:
<br>
브라우저에서 다음 주소로 접속하세요:

```
🌐 Web UI:     http://localhost:8000
📚 API Docs:   http://localhost:8000/docs
📖 ReDoc:      http://localhost:8000/redoc
❤️  Health:     http://localhost:8000/health
```

-----

## 🔌 API Endpoints

| Method | Endpoint | Description (English) | Description (Korean) |
|:------:|:---------|:----------------------|:---------------------|
| `GET` | `/` | Web Chat UI | 웹 채팅 UI |
| `POST` | `/ask` | Ask Sherlock a question (supports max\_tokens, temperature) | 셜록에게 질문하기 (파라미터 설정 가능) |
| `GET` | `/health` | Check server & model status | 서버 및 모델 상태 확인 |
| `GET` | `/docs` | Swagger Documentation | Swagger 문서 |

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

-----

## 🧠 Model Information

\<div align="center"\>

| Component | Details |
|-----------|---------|
| **Base Model** | [`google/gemma-2-2b-it`](https://www.google.com/search?q=%5Bhttps://huggingface.co/google/gemma-2-2b-it%5D\(https://huggingface.co/google/gemma-2-2b-it\)) |
| **LoRA Model** | [`Sung1Lim/sherlock-holmes-qa`](https://www.google.com/search?q=%5Bhttps://huggingface.co/Sung1Lim/sherlock-holmes-qa%5D\(https://huggingface.co/Sung1Lim/sherlock-holmes-qa\)) |
| **Dataset** | [`Alleinzellgaenger/sherlock-holmes-qa`](https://www.google.com/search?q=%5Bhttps://huggingface.co/datasets/Alleinzellgaenger/sherlock-holmes-qa%5D\(https://huggingface.co/datasets/Alleinzellgaenger/sherlock-holmes-qa\)) |
| **Fine-Tuning** | PEFT LoRA (r=16, alpha=32) |
| **Training Loss** | 1.46 → 0.52 |
| **Validation Loss** | 0.85 → 0.74 |

\</div\>

> 💡 **Auto-Loading**: When FastAPI starts, it automatically downloads and loads the checkpoint from the HuggingFace Hub.
> <br>
> 💡 **자동 로딩**: FastAPI 실행 시 HuggingFace Hub에서 자동으로 체크포인트를 다운로드하여 로딩합니다.

-----

## 🏗️ Project Structure

```
sherlock-qa-bot/
│
├── 📁 api/
│   ├── main.py              # FastAPI Endpoints + Web UI
│   ├── model.py             # Gemma + LoRA Loading & Inference
│   └── schemas.py           # Request/Response Schemas
│
├── 📁 templates/
│   └── index.html           # Web Chat UI (CSS/JS included)
│
├── 📁 scripts/
│   └── client.py            # API Test Script
│
├── 📁 notebooks/
│   └── train_sherlock.ipynb # LoRA Training Notebook
│
├── run.py                   # Server Entry Point
├── requirements.txt         # Dependencies
└── README.md
```

> 💡 **Note**: The `templates/index.html` file contains all styles (CSS) and scripts (JavaScript), so no separate static folder is required.
> <br>
> 💡 **참고**: `templates/index.html` 파일에 모든 스타일(CSS)과 스크립트(JavaScript)가 포함되어 있어 별도의 static 폴더가 필요하지 않습니다.

-----

## 🛠️ Tech Stack

\<div align="center"\>

### Core Technologies

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

\</div\>

-----

## 💡 Usage Examples

### Python Client

```python
from scripts.client import ask_sherlock

# Ask a question (질문하기)
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

-----

## 📊 Performance

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Training Loss | 1.46 | 0.52 | ⬇️ 64.4% |
| Validation Loss | 0.85 | 0.74 | ⬇️ 12.9% |
| Model Size | \~5GB | \~50MB | ⬇️ 99% (LoRA) |
| Inference Speed | - | \~2-3s | CPU-friendly |

-----

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

-----

## 💬 Contact & Support

\<div align="center"\>

**Please leave suggestions or questions as GitHub Issues\!**
<br>
**프로젝트 관련 제안이나 질문은 GitHub Issues로 남겨주세요\!**

[](https://github.com/your-username/sherlock-qa-bot/issues)
[](https://huggingface.co/Sung1Lim/sherlock-holmes-qa)

-----

### ⭐ Star this project if you find it useful\!

Made with ❤️ by [Sung1Lim](https://github.com/Sung1Lim)

\</div\>