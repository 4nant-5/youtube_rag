import streamlit as st

LANGUAGES = [
    "English",
    "Hindi",
    "French",
    "German",
    "Spanish",
    "Japanese",
    "Chinese",
]


def render():
    """Render the application sidebar."""

    with st.sidebar:

        st.header("⚙️ Settings")

        response_language = st.selectbox(
            "🌍 Response Language",
            LANGUAGES,
        )

        st.divider()

        st.subheader("📊 Status")

        video_indexed = st.session_state.get("video_indexed", False)
        video_id = st.session_state.get("video_id")
        chunks = st.session_state.get("chunks_indexed", 0)
        indexing = st.session_state.get("indexing", False)

        if indexing:
            st.info("🔄 Indexing in progress...")
        elif video_indexed:
            st.success("✅ Video indexed")
            st.write(f"Video ID: {video_id}")
            st.write(f"Chunks indexed: {chunks}")
        else:
            st.info("⚪ Ready")

    return response_language