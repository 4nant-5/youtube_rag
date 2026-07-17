from langchain_core.documents import Document


class PromptService:
    """
    Responsible for building the prompt
    sent to the LLM.
    """

    def build_prompt(
        self,
        question: str,
        documents: list[Document],
        response_language: str,
    ) -> str:

        context = ""

        for index, document in enumerate(documents, start=1):

            start = document.metadata.get("start_time", "N/A")
            end = document.metadata.get("end_time", "N/A")

            context += f"""
----------------------------
Chunk {index}
Timestamp: {start:.2f}s - {end:.2f}s

{document.page_content}

"""

        prompt = f"""
You are an expert AI assistant that answers questions about YouTube videos.

Your task is to answer ONLY using the provided context.

Rules:

1. Never invent information.
2. Never use outside knowledge.
3. If the answer cannot be found in the context, respond exactly with:

"I couldn't find the answer in the provided video."

4. Keep the answer concise but complete.
5. If appropriate, mention the timestamp(s) where the information appears.
6. Do not mention that you are using chunks or retrieved documents.
7. Answer in {response_language}.
8. Preserve technical terms when necessary.
9. If the user asks in another language, still answer in {response_language}.

==================================================
VIDEO CONTEXT
==================================================

{context}

==================================================
USER QUESTION
==================================================

{question}

==================================================
ANSWER
==================================================
"""

        return prompt