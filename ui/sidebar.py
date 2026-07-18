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

        st.info("⚪ Ready")

    return response_language