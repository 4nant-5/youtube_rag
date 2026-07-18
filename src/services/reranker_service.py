import logging

from langchain_core.documents import Document
from src.config.settings import RERANKER_MODEL

logger = logging.getLogger(__name__)


class RerankerService:

    def __init__(self):
        self.model = None
        self.model_loaded = False

    def _load_model(self) -> bool:
        if self.model_loaded:
            return self.model is not None

        self.model_loaded = True

        try:
            from sentence_transformers import CrossEncoder

            logger.info("Loading reranker model %s", RERANKER_MODEL)
            self.model = CrossEncoder(RERANKER_MODEL)
            logger.info("Reranker loaded successfully")
            return True
        except Exception as exc:
            logger.exception("Failed to load reranker model: %s", exc)
            self.model = None
            return False

    def score(
        self,
        query: str,
        document: Document,
    ) -> float:
        if not self._load_model():
            return 0.0

        try:
            score = self.model.predict([
                (
                    query,
                    document.page_content,
                )
            ])
            return float(score[0])
        except Exception as exc:
            logger.exception("Reranker scoring failed: %s", exc)
            return 0.0

    def rerank(
        self,
        query: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:
        if not documents:
            return []

        if not self._load_model():
            logger.warning("Reranker model unavailable; returning original documents")
            return documents

        scored_documents = []

        for document in documents:
            score = self.score(
                query=query,
                document=document,
            )
            scored_documents.append((score, document))

        scored_documents.sort(key=lambda item: item[0], reverse=True)

        reranked_documents = []
        for score, document in scored_documents[:top_k]:
            document.metadata["reranker_score"] = score
            reranked_documents.append(document)

        return reranked_documents
