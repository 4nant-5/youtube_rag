import sys
from pathlib import Path


# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config.settings import CHROMA_DB_PATH
from src.services.indexing_service import IndexingService
from src.services.whoosh_service import WhooshService
from src.chains.ingestion_chain import IngestionChain
from src.services.embedding_service import EmbeddingService
from src.services.chroma_service import ChromaService


def main():

    from src.config.settings import CHROMA_DB_PATH

    print("=" * 80)
    print("CHROMA PATH")
    print(CHROMA_DB_PATH)
    print("=" * 80)

    embedding_service = EmbeddingService()

    chroma_service = ChromaService(
        embedding_service.get_embedding_model()
    )

    whoosh_service = WhooshService()

    indexing_service = IndexingService(
        chroma_service,
        whoosh_service,
    )

    ingestion_chain = IngestionChain(
        indexing_service
    )

    result = ingestion_chain.invoke(
        "https://www.youtube.com/watch?v=UPtG_38Oq8o"
    )

    print(result)


if __name__ == "__main__":
    main()