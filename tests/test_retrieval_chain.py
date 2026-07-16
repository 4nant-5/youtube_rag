import sys
from pathlib import Path

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.chains.retrieval_chain import RetrievalChain

from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService
from src.services.reranker_service import RerankerService
from src.services.youtube_service import YouTubeService

from src.retrievers.dense_retriever import DenseRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever


def main():

    # -------------------------------
    # Services
    # -------------------------------

    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    whoosh_service = WhooshService()

    reranker_service = RerankerService()

    # -------------------------------
    # Retrievers
    # -------------------------------

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

    # -------------------------------
    # Retrieval Chain
    # -------------------------------

    retrieval_chain = RetrievalChain(
        hybrid_retriever,
        reranker_service,
    )

    # -------------------------------
    # Test Query
    # -------------------------------

    url = "https://www.youtube.com/watch?v=UPtG_38Oq8o"

    video_id = YouTubeService.extract_video_id(url)

    query = "What is attention?"

    documents = retrieval_chain.invoke(
        query=query,
        video_id=video_id,
        retrieval_k=10,
        rerank_k=5,
    )

    # -------------------------------
    # Results
    # -------------------------------

    print("=" * 100)
    print("RETRIEVAL CHAIN RESULTS")
    print("=" * 100)

    print(f"\nRetrieved {len(documents)} documents\n")

    for index, document in enumerate(documents, start=1):

        print(f"Rank {index}")

        print(document.metadata)

        print()

        print(document.page_content[:300])

        print("-" * 100)


if __name__ == "__main__":
    main()