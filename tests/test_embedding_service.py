import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.embedding_service import EmbeddingService
def main():

    embedding_service = EmbeddingService()

    model = embedding_service.get_embedding_model()

    embedding = model.embed_query(
        "What is Retrieval Augmented Generation?"
    )

    print(f"Embedding Dimension: {len(embedding)}")

    print()

    print(embedding[:10])


if __name__ == "__main__":
    main()