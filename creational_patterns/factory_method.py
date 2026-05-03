from abc import ABC, abstractmethod

class LLMProcessor(ABC):
    @abstractmethod
    def process_request(self, prompt: str) -> str:
        pass

class OpenAIProcessor(LLMProcessor):
    def process_request(self, prompt: str) -> str:
        return f"[OpenAI API Generated]: {prompt}"

class GeminiProcessor(LLMProcessor):
    def process_request(self, prompt: str) -> str:
        return f"[Gemini API Generated]: {prompt}"