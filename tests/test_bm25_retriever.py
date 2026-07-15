import sys
from pathlib import Path

from src.services.youtube_service import YouTubeService

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.retrievers.bm25_retriever import BM25Retriever
from src.services.whoosh_service import WhooshService


def main():

    url = "https://www.youtube.com/watch?v=J5_-l7WIO_w"

    video_id = YouTubeService.extract_video_id(url)

    whoosh_service = WhooshService()

    retriever = BM25Retriever(whoosh_service)

    query = "transformer"   # Use a keyword you know exists

    results = retriever.retrieve(
    query="transformers",
    video_id=video_id,
    k=5,
)

    print("=" * 80)
    print(f"Retrieved {len(results)} chunks")
    print("=" * 80)

    for i, document in enumerate(results, start=1):

        print(f"\nChunk {i}")

        print(document.metadata)

        print()

        print(document.page_content[:300])

        print("-" * 80)


if __name__ == "__main__":
    main()