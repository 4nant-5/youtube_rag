from src.services.youtube_service import YouTubeService
from src.services.transcript_service import TranscriptService
from src.services.document_service import DocumentService
from src.services.chunking_service import ChunkService
from src.services.chroma_service import ChromaService
from src.services.indexing_service import IndexingService


class IngestionChain:

    def __init__(self,indexing_service: IndexingService):

        self.indexing_service = indexing_service
        self.chunk_service = ChunkService()

    def invoke(self, youtube_url: str):

        video_id = YouTubeService.extract_video_id(youtube_url)

        if self.indexing_service.video_exists(video_id):

            return {
                "status": "skipped",
                "video_id": video_id,
                "already_indexed": True,
                "chunks_indexed": self.indexing_service.get_indexed_chunk_count(video_id),
            }

        transcript_data = TranscriptService.get_transcript(video_id)

        transcript = transcript_data["transcript"]

        document = DocumentService.transcript_to_documents(
            transcript,
            video_id,
        )

        chunks = ChunkService().split_documents(
            document
        )

        self.indexing_service.index_documents(chunks)

        return {
            "status": "indexed",
            "video_id": video_id,
            "already_indexed": False,
            "chunks_indexed": len(chunks),
        }