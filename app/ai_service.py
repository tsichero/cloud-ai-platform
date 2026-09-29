from dataclasses import dataclass

@dataclass
class AIResponse:
    answer: str
    mode: str

class AIService:
    """Provider-agnostic AI service with deterministic demo mode."""

    def __init__(self, mode: str = "demo") -> None:
        self.mode = mode

    def generate(self, prompt: str) -> AIResponse:
        if self.mode != "demo":
            raise NotImplementedError("External model provider is a roadmap item.")
        return AIResponse(
            answer=f"Demo response generated for: {prompt.strip()}",
            mode="demo",
        )
