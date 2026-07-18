import logging

from src.config.settings import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)

logger = logging.getLogger(__name__)


class LLMService:
    """
    Handles all communication with the language model.
    """

    def __init__(self):
        self.llm = None
        self.model_available = None

    def _initialize(self) -> bool:
        if self.model_available is not None:
            return self.model_available

        try:
            from langchain_ollama import ChatOllama

            self.llm = ChatOllama(
                model=OLLAMA_MODEL,
                base_url=OLLAMA_BASE_URL,
                temperature=0,
            )
            logger.info("LLM service initialized with Ollama at %s", OLLAMA_BASE_URL)
            self.model_available = True
        except Exception as exc:
            logger.exception("Failed to initialize Ollama LLM: %s", exc)
            self.llm = None
            self.model_available = False

        return self.model_available

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the LLM.
        """

        if not self._initialize():
            return self._fallback_answer()

        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as exc:
            logger.exception("LLM invocation failed: %s", exc)
            return self._fallback_answer()

    def _fallback_answer(self) -> str:
        return (
            "I couldn't generate an answer because the Ollama language model is unavailable. "
            f"Please ensure Ollama is running at {OLLAMA_BASE_URL} and the model '{OLLAMA_MODEL}' is loaded."
        )
