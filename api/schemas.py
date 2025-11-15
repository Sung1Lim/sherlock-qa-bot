from pydantic import BaseModel
from typing import Optional, List


class QuestionRequest(BaseModel):
    """
    사용자가 보내는 질문 요청 스키마
    """
    question: str
    top_k: Optional[int] = 3
    max_tokens: Optional[int] = 300
    temperature: Optional[float] = 0.7


class AnswerResponse(BaseModel):
    """
    모델이 반환하는 답변 스키마
    """
    question: str
    answer: str
    context: Optional[List[str]] = None  # 필요 없으면 main.py에서 안 써도 됨


class HealthResponse(BaseModel):
    """
    헬스 체크 응답 스키마
    """
    status: str = "ok"
    model_loaded: bool
