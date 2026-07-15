from langchain_chroma import Chroma

from src.config.settings import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
)


class ChromaService:
    """Service responsible for interacting with ChromaDB."""

    def __init__(self, embedding_model):

        self.vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embedding_model,
            persist_directory=str(CHROMA_DB_PATH),
        )
    
    def get_indexed_chunk_count(self, video_id: str) -> int:
        """
        Returns the number of chunks indexed for a given video.
        """

        results = self.vector_store.get(
            where={"video_id": video_id}
        )

        return len(results["ids"])
    def video_exists(self, video_id: str) -> bool:
        """
        Check if a video's chunks already exist in ChromaDB.
        """

        results = self.vector_store.get(
            where={"video_id": video_id}
        )

        return len(results["ids"]) > 0

    def add_documents(self, documents):

        self.vector_store.add_documents(documents)

    def similarity_search(self, query, k=4):

        return self.vector_store.similarity_search(
            query,
            k=k,
        )

    def get_vector_store(self):

        return self.vector_store