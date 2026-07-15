import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService


def main():

    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    video_id = "dQw4w9WgXcQ"   # Replace with one you've already indexed

    if chroma_service.video_exists(video_id):
        print("Video already indexed.")
    else:
        print("Video not indexed.")


if __name__ == "__main__":
    main()