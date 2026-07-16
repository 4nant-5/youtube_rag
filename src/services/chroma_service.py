from langchain_chroma import Chroma

from src.config.settings import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
)


class ChromaService:
    """
    Service responsible for interacting with ChromaDB.
    """

    def __init__(self, embedding_model):

        self.vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=embedding_model,
            persist_directory=str(CHROMA_DB_PATH),
        )

    def add_documents(self, documents):

        self.vector_store.add_documents(documents)

    def similarity_search(
        self,
        query: str,
        video_id: str,
        k: int = 4,
    ):
        """
        Perform semantic search restricted to a single video.
        """

        return self.vector_store.similarity_search(
            query=query,
            k=k,
            filter={
                "video_id": video_id
            },
        )

    def video_exists(
        self,
        video_id: str,
    ) -> bool:
        """
        Check whether a video's chunks already exist.
        """

        results = self.vector_store.get(
            where={
                "video_id": video_id
            }
        )

        return len(results["ids"]) > 0

    def get_indexed_chunk_count(
        self,
        video_id: str,
    ) -> int:
        """
        Return the number of indexed chunks for a video.
        """

        results = self.vector_store.get(
            where={
                "video_id": video_id
            }
        )

        return len(results["ids"])

    def get_vector_store(self):

        return self.vector_store

    def debug_list_videos(self):
        """
        Print all unique video IDs currently stored in Chroma.
        """

        collection = self.vector_store.get()

        print("=" * 80)
        print("VIDEOS STORED IN CHROMA")
        print("=" * 80)

        video_ids = set()

        for metadata in collection["metadatas"]:

            video_ids.add(metadata["video_id"])

        for video_id in sorted(video_ids):
            print(video_id)

        print("=" * 80)