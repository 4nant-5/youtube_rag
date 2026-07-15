import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.youtube_service import YouTubeService
from src.services.transcript_service import TranscriptService
from src.services.document_service import DocumentService
from src.services.chunking_service import ChunkService
from src.services.whoosh_service import WhooshService


def main():

    url = "https://www.youtube.com/watch?v=J5_-l7WIO_w&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=20"

    video_id = YouTubeService.extract_video_id(url)

    transcript_data = TranscriptService.get_transcript(video_id)

    transcript = transcript_data["transcript"]

    documents = DocumentService.transcript_to_documents(
        transcript,
        video_id,
    )

    chunk_service = ChunkService()

    chunks = chunk_service.split_documents(
        documents
    )

    whoosh = WhooshService()

    whoosh.add_documents(chunks)

    print(f"Indexed {len(chunks)} chunks.")


if __name__ == "__main__":
    main()