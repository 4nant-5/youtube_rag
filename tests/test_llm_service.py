import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.services.llm_service import LLMService


def main():

    llm_service = LLMService()

    prompt = """
    Explain Artificial Intelligence in two sentences.
    """

    answer = llm_service.generate(prompt)

    print("=" * 80)
    print("PROMPT")
    print("=" * 80)
    print(prompt)

    print()

    print("=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(answer)


if __name__ == "__main__":
    main()