import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.document_service import DocumentService
from src.services.transcript_service import TranscriptService
from src.services.youtube_service import YouTubeService


def main():

    url = "https://www.youtube.com/watch?v=J5_-l7WIO_w&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0&index=20"

    # Extract only the video ID
    video_id = YouTubeService.extract_video_id(url)

    # Fetch transcript
    transcript_data = TranscriptService.get_transcript(video_id)

    print(transcript_data["language"])

    transcript = transcript_data["transcript"]

    # Convert transcript to LangChain Document
    document = DocumentService.transcript_to_document(
        transcript,
        video_id
    )

    print("=" * 50)
    print("Document Type")
    print("=" * 50)
    print(type(document))

    print("\n" + "=" * 50)
    print("Metadata")
    print("=" * 50)
    print(document.metadata)

    print("\n" + "=" * 50)
    print("Document Preview")
    print("=" * 50)
    print(document.page_content[:500])


if __name__ == "__main__":
    main()