import streamlit as st


def render():
    """Render the question input section."""

    st.subheader("💬 Ask Beacon")

    st.caption(
        "Ask anything about the indexed video."
    )
    if not st.session_state.get("video_indexed", False):
        st.info("📹 Please index a YouTube video before asking questions.")
    question = st.text_area(
        label="Question",
        label_visibility="collapsed",
        placeholder=(
            "Example:\n"
            "• Summarize this lecture\n"
            "• Explain Retrieval-Augmented Generation\n"
            "• What are the key takeaways?"
        ),
        height=140,
    )

    ask_clicked = st.button(
        "🚀 Ask Beacon",
        disabled=not st.session_state.get("video_indexed", False),
        use_container_width=True,
    )

    return question, ask_clicked