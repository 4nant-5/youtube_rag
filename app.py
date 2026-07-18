import logging
import streamlit as st
from src.bootstrap import create_application
from ui import (
    hero,
    feature_cards,
    knowledge_base,
    question_box,
    sidebar,
    answer_panel,
)

st.set_page_config(
    page_title="Beacon",
    page_icon="🔦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Configure logging for the app
logging.basicConfig(level=logging.INFO)

@st.cache_resource
def load_application():
    """
    Creates the backend once and reuses it across Streamlit reruns.
    """
    return create_application()
def main():
    application = load_application()

    ingestion_chain = application["ingestion_chain"]
    generation_chain = application["generation_chain"]
    if "video_indexed" not in st.session_state:
        st.session_state.video_indexed = False

    # Sidebar
    response_language = sidebar.render()

    # Hero Section
    hero.render()

    # Feature Cards
    feature_cards.render()

    # Build Knowledge Base
    youtube_url, index_clicked = knowledge_base.render(ingestion_chain)

    # Ask Beacon
    question, ask_clicked = question_box.render()

    # If user asked a question, generate an answer
    if ask_clicked and st.session_state.get("video_indexed", False):

        if not question or question.strip() == "":
            st.error("Please enter a question before asking.")
        else:
            with st.spinner("Generating answer..."):
                try:
                    answer = generation_chain.generate(
                        question,
                        st.session_state.get("video_id"),
                        response_language,
                    )
                except Exception as exc:
                    st.error(f"Generation failed: {exc}")
                    answer = None

            st.session_state["answer"] = answer

    answer_panel.render(st.session_state.get("answer"))

    # -------------------------
    # Backend Integration Later
    # -------------------------

    # if index_clicked:
    #     ingestion_chain.run(youtube_url)

    # if ask_clicked:
    #     generation_chain.run(question)

    # Temporary debug
    # st.write(response_language)
    # st.write(youtube_url)
    # st.write(index_clicked)
    # st.write(question)
    # st.write(ask_clicked)


if __name__ == "__main__":
    main()