import logging
import os

from fastapi import FastAPI
from pydantic import BaseModel, Field

from .ai_service import AIService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Cloud AI Platform", version="0.1.0")
ai_service = AIService(mode=os.getenv("AI_MODE", "demo"))

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)

class GenerateResponse(BaseModel):
    answer: str
    mode: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "cloud-ai-platform"}

@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    logger.info("generation_request mode=%s", ai_service.mode)
    result = ai_service.generate(request.prompt)
    return GenerateResponse(answer=result.answer, mode=result.mode)
