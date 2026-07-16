import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parent.parent)
)

from src.services.reranker_service import RerankerService


def main():

    reranker = RerankerService()

    query = "What is attention?"

    chunk = """
    Attention allows each token to attend to
    every other token in the sequence.
    """

    score = reranker.score(
        query=query,
        document=chunk,
    )

    print()

    print("=" * 80)

    print(f"Score: {score}")

    print("=" * 80)


if __name__ == "__main__":
    main()