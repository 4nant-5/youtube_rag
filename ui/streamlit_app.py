import streamlit as st
import sys
from pathlib import Path

# Ensure project root is on sys.path so `src` package is importable when
# running the test as a script: `python tests/test_youtube_service.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.services.youtube_service import YouTubeService

st.set_page_config(
    page_title="YouTube Multimodal RAG",
    page_icon="🎥",
    layout="wide",
)

st.title("🎥 YouTube Multimodal RAG")

url = st.text_input("Enter YouTube URL")

if st.button("Fetch Video"):

    if not YouTubeService.validate_url(url):
        st.error("Invalid YouTube URL")

    else:

        metadata = YouTubeService.get_video_metadata(url)

        st.success("Video Found!")

        st.write(metadata)

        st.image(metadata["thumbnail"], width=350)

        st.write(f"### {metadata['title']}")

        st.write(f"**Channel:** {metadata['channel']}")

        st.write(f"**Duration:** {metadata['duration']} seconds")

        st.write(f"**Views:** {metadata['view_count']:,}")