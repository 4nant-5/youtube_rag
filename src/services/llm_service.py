from langchain_ollama import ChatOllama

from src.config.settings import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
)


class LLMService:
    """
    Service responsible for interacting with the LLM.
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0,
        )

        print("LLM loaded")

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.llm.invoke(prompt)

        return response.content