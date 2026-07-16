from sentence_transformers import CrossEncoder

from src.config.settings import RERANKER_MODEL
from langchain_core.documents import Document

class RerankerService:

    def __init__(self):

        print("Loading BGE Reranker...")

        self.model = CrossEncoder(RERANKER_MODEL)

        print("Reranker loaded successfully!")

    def score(
    self,
    query: str,
    document: Document,
) -> float:

        score = self.model.predict(
            [
                (
                    query,
                    document.page_content,
                )
            ]
        )

        return float(score[0])
    
    def rerank(
    self,
    query: str,
    documents: list[Document],
    top_k: int = 5,
) -> list[Document]:

        scored_documents = []

        for document in documents:

            score = self.score(
                query=query,
                document=document,
            )

            scored_documents.append(
                (
                    score,
                    document,
                )
            )

        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        reranked_documents = []

        for score, document in scored_documents[:top_k]:

            document.metadata["reranker_score"] = score

            reranked_documents.append(document)

        return reranked_documents