import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.services.youtube_service import YouTubeService


def main():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    print("Valid URL:", YouTubeService.validate_url(url))

    print("Video ID:", YouTubeService.extract_video_id(url))

    metadata = YouTubeService.get_video_metadata(url)

    print(metadata)


if __name__ == "__main__":
    main()