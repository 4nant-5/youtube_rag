import time
import streamlit as st

from src.services.youtube_service import YouTubeService


def render(ingestion_chain):
    """Render the knowledge base section."""

    st.divider()

    st.subheader("📹 Build Knowledge Base")

    st.caption(
        "Paste a YouTube video URL to create an AI-searchable knowledge base. "
        "Once indexing is complete, you can ask questions about the video."
    )

    youtube_url = st.text_input(
        label="YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
    )

    index_disabled = st.session_state.get("indexing", False)

    index_clicked = st.button(
        "📥 Index Video",
        disabled=index_disabled,
        use_container_width=True,
    )

    if index_clicked:

        if not youtube_url:
            st.error("Please enter a YouTube URL.")
            return youtube_url, False

        if not YouTubeService.validate_url(youtube_url):
            st.error("Invalid YouTube URL.")
            return youtube_url, False

        video_id = YouTubeService.extract_video_id(youtube_url)

        # Prevent duplicate indexing of same video
        if st.session_state.get("video_indexed", False) and st.session_state.get("video_id") == video_id:
            st.info("Video already indexed")
            return youtube_url, False

        try:
            st.session_state["indexing"] = True
            start = time.time()

            with st.spinner("Indexing video — this may take a while..."):
                result = ingestion_chain.invoke(youtube_url)

            duration = time.time() - start

        except Exception as exc:
            st.error(f"Indexing failed: {exc}")
            st.session_state["indexing"] = False
            return youtube_url, False

        finally:
            st.session_state["indexing"] = False

        # Persist indexing results in session state
        st.session_state["video_indexed"] = True
        st.session_state["video_id"] = result.get("video_id")
        st.session_state["chunks_indexed"] = result.get("chunks_indexed", 0)
        st.session_state["language"] = result.get("language")
        st.session_state["index_time"] = duration

        if result.get("already_indexed"):
            st.info("Video was already indexed previously.")
        else:
            st.success("Video indexed successfully")
            st.write(f"{st.session_state['chunks_indexed']} chunks indexed")
            st.write(f"Indexing time: {st.session_state['index_time']:.1f}s")
            if st.session_state.get("language"):
                st.write(f"Language detected: {st.session_state.get('language')}")

    return youtube_url, index_clicked