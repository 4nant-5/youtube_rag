from langchain_core.documents import Document

from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService


class IndexingService:
    """
    Coordinates indexing across all retrieval backends.
    """

    def __init__(
        self,
        chroma_service: ChromaService,
        whoosh_service: WhooshService,
    ):

        self.chroma_service = chroma_service
        self.whoosh_service = whoosh_service

    def video_exists(self, video_id: str) -> bool:

        return self.chroma_service.video_exists(video_id)

    def get_indexed_chunk_count(self, video_id: str) -> int:

        return self.chroma_service.get_indexed_chunk_count(video_id)

    # def index_documents(
    #     self,
    #     chunks: list[Document],
    # ):

    #     self.chroma_service.add_documents(chunks)

    #     self.whoosh_service.add_documents(chunks)

    def index_documents(
    self,
    chunks: list[Document],
):

        print("=" * 80)
        print("FIRST DOCUMENT BEFORE INDEXING")
        print("=" * 80)

        print(chunks[0])

        print()

        print("Metadata:")
        print(chunks[0].metadata)

        print("=" * 80)

        self.chroma_service.add_documents(chunks)

        self.whoosh_service.add_documents(chunks)