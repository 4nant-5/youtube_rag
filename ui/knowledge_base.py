import streamlit as st


def render():
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

    index_clicked = st.button(
        "📥 Index Video",
        use_container_width=True,
    )

    return youtube_url, index_clicked