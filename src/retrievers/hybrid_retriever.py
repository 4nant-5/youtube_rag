from langchain_core.documents import Document

from src.retrievers.base_retriever import BaseRetriever
from src.retrievers.dense_retriever import DenseRetriever
from src.retrievers.bm25_retriever import BM25Retriever


class HybridRetriever(BaseRetriever):
    """
    Combines Dense Retrieval and BM25 Retrieval.
    """

    def __init__(
        self,
        dense_retriever: DenseRetriever,
        bm25_retriever: BM25Retriever,
    ):

        self.dense_retriever = dense_retriever
        self.bm25_retriever = bm25_retriever

    def retrieve(
        self,
        query: str,
        video_id: str,
        k: int = 5,
    ) -> list[Document]:

        dense_results = self.dense_retriever.retrieve(
            query=query,
            video_id=video_id,
            k=k,
        )

        bm25_results = self.bm25_retriever.retrieve(
            query=query,
            video_id=video_id,
            k=k,
        )

        merged_documents = {}

        for document in dense_results + bm25_results:

            chunk_id = document.metadata["chunk_id"]

            if chunk_id not in merged_documents:

                merged_documents[chunk_id] = document

        return list(merged_documents.values())