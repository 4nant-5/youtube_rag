import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.transcript_service import TranscriptService


def main():

    video_id = "dQw4w9WgXcQ"

    transcript = TranscriptService.get_transcript(video_id)
    print(f"Language: {transcript['language']}")
    
    print(f"Segments: {len(transcript['transcript'])}")

    print()

    print(transcript[:5])


if __name__ == "__main__":
    main()