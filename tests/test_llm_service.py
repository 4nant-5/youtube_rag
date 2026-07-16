import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.services.llm_service import LLMService


def main():

    llm_service = LLMService()

    question = "What is Artificial Intelligence?"

    answer = llm_service.generate(question)

    print("=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(question)

    print()

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(answer)


if __name__ == "__main__":
    main()