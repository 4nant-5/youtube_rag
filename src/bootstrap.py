from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService
from src.services.whoosh_service import WhooshService
from src.services.indexing_service import IndexingService
from src.services.transcript_service import TranscriptService
from src.services.chunking_service import ChunkService
from src.services.reranker_service import RerankerService
from src.services.prompt_service import PromptService
from src.services.llm_service import LLMService

from src.retrievers.dense_retriever import DenseRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever

from src.chains.ingestion_chain import IngestionChain
from src.chains.retrieval_chain import RetrievalChain
from src.chains.generation_chain import GenerationChain


def create_application():
    """
    Creates and wires the complete Beacon application.
    """

    # -----------------------------
    # Core Services
    # -----------------------------
    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    whoosh_service = WhooshService()

    indexing_service = IndexingService(
        chroma_service,
        whoosh_service,
    )

    llm_service = LLMService()

    prompt_service = PromptService()

    reranker_service = RerankerService()

    # -----------------------------
    # Retrievers
    # -----------------------------
    dense_retriever = DenseRetriever(
        chroma_service,
    )

    bm25_retriever = BM25Retriever(
        whoosh_service,
    )

    hybrid_retriever = HybridRetriever(
        dense_retriever,
        bm25_retriever,
    )

    retrieval_chain = RetrievalChain(
        hybrid_retriever,
        reranker_service,
    )

    ingestion_chain = IngestionChain(
        TranscriptService(),
        ChunkService(),
        indexing_service,
    )

    generation_chain = GenerationChain(
        retrieval_chain,
        prompt_service,
        llm_service,
    )

    return {
        "ingestion_chain": ingestion_chain,
        "generation_chain": generation_chain,
    }