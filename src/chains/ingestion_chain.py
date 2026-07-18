from src.services.youtube_service import YouTubeService
from src.services.transcript_service import TranscriptService
from src.services.document_service import DocumentService
from src.services.chunking_service import ChunkService
from src.services.chroma_service import ChromaService
from src.services.indexing_service import IndexingService


class IngestionChain:

    def __init__(
        self,
        transcript_service: TranscriptService,
        chunk_service: ChunkService,
        indexing_service: IndexingService,
    ):

        self.transcript_service = transcript_service
        self.chunk_service = chunk_service
        self.indexing_service = indexing_service

    def invoke(self, youtube_url: str):
        video_id = YouTubeService.extract_video_id(youtube_url)

        if not video_id:
            raise ValueError("Invalid YouTube URL or missing video id")

        if self.indexing_service.video_exists(video_id):

            return {
                "status": "skipped",
                "video_id": video_id,
                "already_indexed": True,
                "chunks_indexed": self.indexing_service.get_indexed_chunk_count(video_id),
            }

        # Fetch transcript and fail fast if unavailable
        transcript_data = self.transcript_service.get_transcript(video_id)

        transcript = transcript_data["transcript"]
        language = transcript_data.get("language")

        document = DocumentService.transcript_to_documents(
            transcript,
            video_id,
        )

        chunks = self.chunk_service.split_documents(document)

        self.indexing_service.index_documents(chunks)

        return {
            "status": "indexed",
            "video_id": video_id,
            "already_indexed": False,
            "chunks_indexed": len(chunks),
            "language": language,
        }