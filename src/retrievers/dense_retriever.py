from src.services.chroma_service import ChromaService


class DenseRetriever:

    def __init__(self, chroma_service: ChromaService):
        self.vector_store = chroma_service.get_vector_store()

    def retrieve(
        self,
        query: str,
        video_id: str,
        k: int = 5,
    ):

        return self.vector_store.similarity_search(
            query=query,
            k=k,
            filter={
                "video_id": video_id
            }
        )