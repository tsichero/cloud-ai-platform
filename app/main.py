import logging
import os
import time
import uuid

from fastapi import FastAPI, Request
from pydantic import BaseModel, Field

from .ai_service import AIService

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="Cloud AI Platform", version="0.2.0")
ai_service = AIService(mode=os.getenv("AI_MODE", "demo"))

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=2000)

class GenerateResponse(BaseModel):
    answer: str
    mode: str
    request_id: str

@app.middleware("http")
async def request_logging(request: Request, call_next):
    request_id = str(uuid.uuid4())
    started = time.perf_counter()
    response = await call_next(request)
    elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
    response.headers["X-Request-ID"] = request_id
    logger.info("request_id=%s method=%s path=%s status=%s latency_ms=%s",
                request_id, request.method, request.url.path, response.status_code, elapsed_ms)
    return response

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "cloud-ai-platform"}

@app.get("/ready")
def ready() -> dict[str, str]:
    return {"status": "ready", "ai_mode": ai_service.mode}

@app.post("/generate", response_model=GenerateResponse)
def generate(request: GenerateRequest) -> GenerateResponse:
    request_id = str(uuid.uuid4())
    logger.info("generation_request request_id=%s mode=%s", request_id, ai_service.mode)
    result = ai_service.generate(request.prompt)
    return GenerateResponse(answer=result.answer, mode=result.mode, request_id=request_id)
