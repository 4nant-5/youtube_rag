import streamlit as st


FEATURES = [
    {
        "icon": "🎥",
        "title": "Index Videos",
        "description": (
            "Convert educational YouTube videos into a searchable "
            "knowledge base."
        ),
    },
    {
        "icon": "🧠",
        "title": "AI Answers",
        "description": (
            "Generate context-aware answers grounded in the indexed content."
        ),
    },
    {
        "icon": "🌍",
        "title": "Multilingual",
        "description": (
            "Receive answers in your preferred language."
        ),
    },
    {
        "icon": "⚡",
        "title": "Hybrid Retrieval",
        "description": (
            "Combine semantic and keyword search for accurate retrieval."
        ),
    },
]


def render():
    """Render the feature cards."""

    st.subheader("✨ Why Beacon?")

    columns = st.columns(len(FEATURES))

    for column, feature in zip(columns, FEATURES):
        with column:
            with st.container(border=True):
                st.markdown(f"## {feature['icon']}")
                st.markdown(f"**{feature['title']}**")
                st.caption(feature["description"])