import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.whoosh_service import WhooshService


def main():

    whoosh = WhooshService()
    # with whoosh.index.searcher() as searcher:

    #     for doc in searcher.all_stored_fields():
    #         print(doc)
    #         break
    results = whoosh.search(
        "attention"
    )

    print("=" * 80)

    print(f"Retrieved {len(results)} documents")

    print("=" * 80)

    for document in results:

        print(document.metadata)

        print()

        print(document.page_content[:300])

        print("-" * 60)


if __name__ == "__main__":
    main()