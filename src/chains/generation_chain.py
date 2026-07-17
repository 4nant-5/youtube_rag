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

        documents = self.retrieval_chain.retrieve(
            question,
            video_id,
        )

        prompt = self.prompt_service.build_prompt(
            question=question,
            documents=documents,
            response_language=response_language,
        )

        answer = self.llm_service.generate(
            prompt,
        )

        return answer