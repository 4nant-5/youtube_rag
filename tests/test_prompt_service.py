import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService
from src.services.reranker_service import RerankerService
from src.services.prompt_service import PromptService
from src.services.youtube_service import YouTubeService

from src.retrievers.dense_retriever import DenseRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever

from src.chains.retrieval_chain import RetrievalChain


def main():

    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    whoosh_service = WhooshService()

    reranker_service = RerankerService()

    prompt_service = PromptService()

    dense_retriever = DenseRetriever(chroma_service)

    bm25_retriever = BM25Retriever(whoosh_service)

    hybrid_retriever = HybridRetriever(
        dense_retriever,
        bm25_retriever,
    )

    retrieval_chain = RetrievalChain(
        hybrid_retriever,
        reranker_service,
    )

    url = "https://www.youtube.com/watch?v=UPtG_38Oq8o"

    video_id = YouTubeService.extract_video_id(url)

    documents = retrieval_chain.invoke(
        query="What is attention?",
        video_id=video_id,
    )

    prompt = prompt_service.build_prompt(
        question="What is attention?",
        documents=documents,
    )

    print(prompt)


if __name__ == "__main__":
    main()