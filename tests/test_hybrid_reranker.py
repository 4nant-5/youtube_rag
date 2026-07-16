import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService
from src.services.youtube_service import YouTubeService
from src.services.reranker_service import RerankerService

from src.retrievers.dense_retriever import DenseRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever


def main():

    # from src.config.settings import CHROMA_DB_PATH

    # print("=" * 80)
    # print("CHROMA PATH")
    # print(CHROMA_DB_PATH)
    # print("=" * 80)
    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )
    chroma_service.debug_list_videos()

    whoosh_service = WhooshService()

    dense_retriever = DenseRetriever(
        chroma_service
    )

    bm25_retriever = BM25Retriever(
        whoosh_service
    )

    hybrid_retriever = HybridRetriever(
        dense_retriever,
        bm25_retriever,
    )

    reranker = RerankerService()

    url = "https://www.youtube.com/watch?v=UPtG_38Oq8o"

    video_id = YouTubeService.extract_video_id(url)

    # print("=" * 80)
    # print("VIDEO DEBUG")
    # print("=" * 80)

    # print("Video ID:", video_id)

    # print("Video Exists:", chroma_service.video_exists(video_id))

    # print("Indexed Chunks:", chroma_service.get_indexed_chunk_count(video_id))

    # print("=" * 80)

    query = "What is attention?"

    documents = hybrid_retriever.retrieve(
        query=query,
        video_id=video_id,
        k=10,
    )

    print(f"\nHybrid returned {len(documents)} documents.\n")

    reranked_documents = reranker.rerank(
        query=query,
        documents=documents,
        top_k=5,
    )

    print("=" * 100)

    print("FINAL RANKED DOCUMENTS")

    print("=" * 100)

    for index, document in enumerate(
        reranked_documents,
        start=1,
    ):

        print(f"\nRank {index}")

        print(document.metadata)

        print()

        print(document.page_content[:300])

        print("-" * 100)


if __name__ == "__main__":
    main()