import streamlit as st
from agent import search_and_summarize

st.set_page_config(page_title="WebGPT-Lite", layout="centered")
st.title("🌐 WebGPT-Lite: Smart Info Summarizer")

query = st.text_input("Ask me anything 🔍", "")

if st.button("Search & Summarize"):
    if query.strip():
        with st.spinner("Looking things up..."):
            result = search_and_summarize(query)
        st.success("Here's what I found:")
        st.markdown(result)