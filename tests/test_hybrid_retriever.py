import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.retrievers.dense_retriever import DenseRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever

from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService


def main():

    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    whoosh_service = WhooshService()

    dense = DenseRetriever(chroma_service)

    bm25 = BM25Retriever(whoosh_service)

    hybrid = HybridRetriever(
        dense,
        bm25,
    )

    video_id = "https://www.youtube.com/watch?v=UPtG_38Oq8o"

    query = "What is attention?"

    documents = hybrid.retrieve(
        query=query,
        video_id=video_id,
        k=5,
    )

    print("=" * 80)

    print(f"Retrieved {len(documents)} unique chunks")

    print("=" * 80)

    for i, document in enumerate(documents, start=1):

        print(f"\nChunk {i}")

        print(document.metadata)

        print()

        print(document.page_content[:300])

        print("-" * 80)


if __name__ == "__main__":
    main()