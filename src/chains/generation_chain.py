import logging


logger = logging.getLogger(__name__)


class GenerationChain:

    def __init__(
        self,
        retrieval_chain,
        prompt_service,
        llm_service,
    ):

        self.retrieval_chain = retrieval_chain
        self.prompt_service = prompt_service
        self.llm_service = llm_service

    def generate(
        self,
        question: str,
        video_id: str,
        response_language: str,
    ) -> str:

        try:
            documents = self.retrieval_chain.invoke(
                question,
                video_id,
            )
        except Exception as exc:
            logger.exception("Retrieval failed: %s", exc)
            raise

        try:
            prompt = self.prompt_service.build_prompt(
                question=question,
                documents=documents,
                response_language=response_language,
            )
        except Exception as exc:
            logger.exception("Prompt building failed: %s", exc)
            raise

        try:
            answer = self.llm_service.generate(
                prompt,
            )
        except Exception as exc:
            logger.exception("LLM generation failed: %s", exc)
            raise

        return answer