"""
Sherlock Holmes QA Bot - FastAPI 메인
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import logging
from contextlib import asynccontextmanager

from .schemas import QuestionRequest, AnswerResponse, HealthResponse
from .model import sherlock_model

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """앱 시작/종료 시 실행"""
    # 시작 시
    logger.info("🚀 FastAPI 서버 시작")
    logger.info("📦 모델 로딩 중...")
    try:
        sherlock_model.load_model()
        logger.info("✅ 모델 로딩 완료")
    except Exception as e:
        logger.error(f"❌ 모델 로딩 실패: {e}")
    
    yield
    
    # 종료 시
    logger.info("👋 FastAPI 서버 종료")


# FastAPI 앱 생성
app = FastAPI(
    title="🎩 Sherlock Holmes QA Bot",
    description="셜록 홈즈 스토리 기반 질의응답 AI 챗봇",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def root():
    """루트 엔드포인트 - 간단한 웹 페이지"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sherlock Holmes QA Bot</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            h1 { font-size: 3em; margin-bottom: 10px; }
            .emoji { font-size: 1.5em; }
            a {
                color: #ffd700;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover { text-decoration: underline; }
            .info-box {
                background: rgba(255, 255, 255, 0.2);
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
            }
            code {
                background: rgba(0, 0, 0, 0.3);
                padding: 2px 8px;
                border-radius: 4px;
                font-family: 'Courier New', monospace;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1><span class="emoji">🎩</span> Sherlock Holmes QA Bot</h1>
            <p style="font-size: 1.2em;">셜록 홈즈 스토리 기반 질의응답 AI 챗봇</p>
            
            <div class="info-box">
                <h2>📖 API 문서</h2>
                <p>
                    <a href="/docs" target="_blank">Swagger UI</a> |
                    <a href="/redoc" target="_blank">ReDoc</a>
                </p>
            </div>
            
            <div class="info-box">
                <h2>🚀 빠른 시작</h2>
                <p><strong>POST /ask</strong> - 셜록에게 질문하기</p>
                <pre><code>curl -X POST "http://localhost:8000/ask" \\
  -H "Content-Type: application/json" \\
  -d '{"question": "Who is Irene Adler?"}'</code></pre>
            </div>
            
            <div class="info-box">
                <h2>ℹ️ 정보</h2>
                <p>
                    📦 <strong>Model:</strong> Google Gemma-2-2B-IT + LoRA<br>
                    🔗 <strong>GitHub:</strong> <a href="https://github.com/Sung1Lim/sherlock-qa-bot" target="_blank">Sung1Lim/sherlock-qa-bot</a><br>
                    🤗 <strong>HuggingFace:</strong> <a href="https://huggingface.co/Sung1Lim/sherlock-holmes-lora" target="_blank">Sung1Lim/sherlock-holmes-lora</a>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """헬스 체크 엔드포인트"""
    return HealthResponse(
        status="healthy",
        model_loaded=sherlock_model.is_loaded(),
        version="1.0.0"
    )


@app.post("/ask", response_model=AnswerResponse)
async def ask_sherlock(request: QuestionRequest):
    """
    셜록 홈즈에게 질문하기
    
    - **question**: 질문 내용 (필수)
    - **max_tokens**: 최대 생성 토큰 수 (기본: 300)
    - **temperature**: 생성 다양성 0.1~1.0 (기본: 0.7)
    """
    if not sherlock_model.is_loaded():
        raise HTTPException(
            status_code=503,
            detail="모델이 아직 로드되지 않았습니다. 잠시 후 다시 시도해주세요."
        )
    
    try:
        logger.info(f"질문 수신: {request.question}")
        
        # 답변 생성
        answer = sherlock_model.generate_answer(
            question=request.question,
            max_tokens=request.max_tokens,
            temperature=request.temperature
        )
        
        logger.info(f"답변 생성 완료 (길이: {len(answer)} 글자)")
        
        return AnswerResponse(
            question=request.question,
            answer=answer
        )
        
    except Exception as e:
        logger.error(f"답변 생성 중 오류: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"답변 생성 중 오류가 발생했습니다: {str(e)}"
        )


@app.get("/examples")
async def get_examples():
    """예시 질문들"""
    return {
        "examples": [
            "How does Holmes regard emotions and love?",
            "Who is Dr. John Watson?",
            "Tell me about Irene Adler",
            "What is 221B Baker Street?",
            "How did the Red-Headed League scheme function?",
            "Who is Professor Moriarty?",
            "What happened in 'A Scandal in Bohemia'?",
            "How does Sherlock Holmes solve his cases?"
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)