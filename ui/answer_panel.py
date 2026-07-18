import streamlit as st


def render(answer=None):
    """Render the answer panel."""

    st.divider()

    st.subheader("✨ Beacon Response")

    with st.container(border=True):

        if answer:
            st.markdown(answer)
        else:
            st.info("Ask a question to receive an AI-generated response.")