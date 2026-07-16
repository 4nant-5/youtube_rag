from langchain_core.documents import Document

from src.retrievers.hybrid_retriever import HybridRetriever
from src.services.reranker_service import RerankerService


class RetrievalChain:
    """
    Coordinates the complete retrieval pipeline.
    """

    def __init__(
        self,
        hybrid_retriever: HybridRetriever,
        reranker_service: RerankerService,
    ):

        self.hybrid_retriever = hybrid_retriever
        self.reranker_service = reranker_service

    def invoke(
        self,
        query: str,
        video_id: str,
        retrieval_k: int = 10,
        rerank_k: int = 5,
    ) -> list[Document]:

        candidate_documents = self.hybrid_retriever.retrieve(
            query=query,
            video_id=video_id,
            k=retrieval_k,
        )

        reranked_documents = self.reranker_service.rerank(
            query=query,
            documents=candidate_documents,
            top_k=rerank_k,
        )

        return reranked_documents