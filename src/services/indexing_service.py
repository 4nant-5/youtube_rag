import logging

from langchain_core.documents import Document

from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService

logger = logging.getLogger(__name__)


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

        if not chunks:
            logger.warning("index_documents called with empty chunk list")
            return

        logger.info("Indexing %d chunks (first chunk metadata: %s)", len(chunks), chunks[0].metadata)

        try:
            self.chroma_service.add_documents(chunks)
        except Exception as exc:
            logger.exception("Chroma indexing failed: %s", exc)
            raise

        try:
            self.whoosh_service.add_documents(chunks)
        except Exception as exc:
            logger.exception("Whoosh indexing failed: %s", exc)
            raise