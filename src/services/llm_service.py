from langchain_ollama import ChatOllama

from src.config.settings import (
    OLLAMA_BASE_URL,
    OLLAMA_MODEL,
)


class LLMService:
    """
    Handles all communication with the language model.
    """

    def __init__(self):

        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0,
        )

        print("Language model loaded successfully.")

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the LLM.
        """

        response = self.llm.invoke(prompt)

        return response.content