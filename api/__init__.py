"""
API 패키지 초기화 모듈
FastAPI 애플리케이션 인스턴스를 외부에서 바로 import 할 수 있도록 설정.
"""

from .main import app

__all__ = ["app"]
