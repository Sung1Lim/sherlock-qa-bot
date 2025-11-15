"""
Sherlock Holmes 모델 로딩 및 추론
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import logging
from typing import Optional, List, Dict

logger = logging.getLogger(__name__)


class SherlockModel:
    """셜록 홈즈 QA 모델"""

    def __init__(self):
        self.model: Optional[AutoModelForCausalLM] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # 베이스 모델 & LoRA 어댑터 경로
        self.base_model_name = "google/gemma-2-2b-it"
        self.lora_model_id = "Sung1Lim/sherlock-holmes-qa"

    def load_model(self):
        """모델 및 토크나이저 로드"""
        try:
            logger.info(f"모델 로딩 시작: {self.base_model_name}")

            # 토크나이저는 LoRA 리포에서 로드 (특수 토큰 / chat_template 포함)
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.lora_model_id,
                use_fast=True,
            )

            # pad_token 없으면 eos로 대체
            if self.tokenizer.pad_token is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            # 생성 태스크이므로 왼쪽 패딩이 편함
            if self.tokenizer.padding_side != "left":
                self.tokenizer.padding_side = "left"

            # Base 모델 로드 (Gemma-2 권장: bfloat16 + device_map="auto")
            dtype = torch.bfloat16 if self.device == "cuda" else torch.float32
            base_model = AutoModelForCausalLM.from_pretrained(
                self.base_model_name,
                torch_dtype=dtype,
                device_map="auto" if self.device == "cuda" else None,
            )

            # LoRA 어댑터 로드
            logger.info(f"LoRA 어댑터 로딩: {self.lora_model_id}")
            self.model = PeftModel.from_pretrained(
                base_model,
                self.lora_model_id,
            )
            self.model.eval()

            # CPU 환경에서는 명시적으로 이동
            if self.device == "cpu":
                self.model = self.model.to(self.device)

            logger.info(f"모델 로딩 완료 (device: {self.device})")
            return True

        except Exception as e:
            logger.error(f"모델 로딩 실패: {e}")
            raise

    def _build_chat_prompt(self, question: str) -> str:
        """
        Gemma / LoRA 토크나이저의 chat_template 사용해서 프롬프트 생성
        """
        # chat 형식: [{"role": "user", "content": "..."}, ...]
        messages: List[Dict[str, str]] = [
            {"role": "user", "content": question}
        ]

        if hasattr(self.tokenizer, "apply_chat_template"):
            # add_generation_prompt=True -> model turn까지 포함한 프롬프트 생성
            return self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
            )
        else:
            # fallback: 예전 방식
            return (
                "<start_of_turn>user\n"
                + question
                + "\n<end_of_turn>\n<start_of_turn>model\n"
            )

    def generate_answer(
        self,
        question: str,
        max_tokens: int = 300,
        temperature: float = 0.7,
    ) -> str:
        """
        질문에 대한 답변 생성

        Args:
            question: 사용자 질문
            max_tokens: 생성할 최대 토큰 수
            temperature: 생성 다양성 (0.1~1.0)

        Returns:
            셜록 홈즈의 답변
        """
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("모델이 로드되지 않았습니다. load_model()을 먼저 호출하세요.")

        try:
            # 프롬프트 생성 
            prompt = self._build_chat_prompt(question)

            # 토크나이징
            inputs = self.tokenizer(
                prompt,
                return_tensors="pt",
            )

            input_len = inputs["input_ids"].shape[-1]

            # GPU로 이동
            if self.device == "cuda":
                inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # 생성
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=max_tokens,
                    temperature=temperature,
                    top_p=0.9,
                    do_sample=True,
                    repetition_penalty=1.1,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )

            # 입력 프롬프트 길이 이후 토큰만 추출해서 디코딩
            generated_ids = outputs[0][input_len:]
            answer = self.tokenizer.decode(
                generated_ids,
                skip_special_tokens=True,
            ).strip()

            # 혹시 너무 짧게 나오거나 공백이면 fallback
            if not answer:
                full_response = self.tokenizer.decode(
                    outputs[0],
                    skip_special_tokens=True,
                )
                if "<start_of_turn>model" in full_response:
                    answer = full_response.split("<start_of_turn>model")[-1].strip()
                else:
                    answer = full_response.strip()

            return answer

        except Exception as e:
            logger.error(f"답변 생성 실패: {e}")
            raise

    def is_loaded(self) -> bool:
        """모델 로드 여부 확인"""
        return self.model is not None and self.tokenizer is not None


# 싱글톤 인스턴스
sherlock_model = SherlockModel()