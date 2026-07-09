from urllib.parse import urlparse, parse_qs
from yt_dlp import YoutubeDL

class YouTubeService:
    """Service responsible for YouTube URL processing."""

    @staticmethod
    def validate_url(url: str) -> bool:
        """Validate whether the URL belongs to YouTube."""

        parsed_url = urlparse(url)

        return parsed_url.netloc in (
            "www.youtube.com",
            "youtube.com",
            "youtu.be",
        )

    @staticmethod
    def extract_video_id(url: str) -> str:
        """Extract the video ID from a YouTube URL."""

        parsed_url = urlparse(url)

        if parsed_url.netloc == "youtu.be":
            return parsed_url.path.lstrip("/")

        query = parse_qs(parsed_url.query)

        return query.get("v", [None])[0]
    
    @staticmethod
    def get_video_metadata(url: str) -> dict:
        """
        Fetch metadata for a single YouTube video without downloading it.
        """

        video_id = YouTubeService.extract_video_id(url)

        clean_url = f"https://www.youtube.com/watch?v={video_id}"

        ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "noplaylist": True,
            "extract_flat": False,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(clean_url, download=False)

        thumbnail = info.get("thumbnail")

        # Fallback in case thumbnail is missing
        if not thumbnail:
            thumbnails = info.get("thumbnails", [])
            if thumbnails:
                thumbnail = thumbnails[-1].get("url")

        return {
            "video_id": video_id,
            "title": info.get("title", "Unknown Title"),
            "channel": info.get("channel", "Unknown Channel"),
            "duration": info.get("duration", 0),
            "thumbnail": thumbnail,
            "view_count": info.get("view_count", 0),
        }