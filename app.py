import streamlit as st

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


def main():

    if "video_indexed" not in st.session_state:
        st.session_state.video_indexed = False

    # Sidebar
    response_language = sidebar.render()

    # Hero Section
    hero.render()

    # Feature Cards
    feature_cards.render()

    # Build Knowledge Base
    youtube_url, index_clicked = knowledge_base.render()

    # Ask Beacon
    question, ask_clicked = question_box.render()

    answer_panel.render()

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