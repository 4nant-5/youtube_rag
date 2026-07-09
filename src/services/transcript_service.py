from youtube_transcript_api import YouTubeTranscriptApi


class TranscriptService:
    """Service responsible for transcript extraction."""

    @staticmethod
    def get_transcript(video_id: str):

        api = YouTubeTranscriptApi()

        transcript_list = api.list(video_id)

        # Prefer manually created transcript
        try:
            transcript = transcript_list.find_manually_created_transcript(
                [t.language_code for t in transcript_list]
            )
        except Exception:
            # Otherwise use auto-generated transcript
            transcript = transcript_list.find_generated_transcript(
                [t.language_code for t in transcript_list]
            )

        return {
            "language": transcript.language_code,
            "transcript": transcript.fetch().to_raw_data(),
        }