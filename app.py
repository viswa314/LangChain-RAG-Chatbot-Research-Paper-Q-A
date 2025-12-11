import streamlit as st
from backend.loader import load_docs
from backend.embeddings import create_vectorstore
from backend.chain import build_chain
from utils.prompts import SYSTEM_PROMPT

st.set_page_config(page_title="LangChain RAG Chatbot", layout="wide")
st.title("🧠 LangChain RAG Chatbot – Research Paper Q&A")

if "chain" not in st.session_state:
    with st.spinner("Initializing RAG pipeline..."):
        docs = load_docs()
        vs = create_vectorstore(docs)
        st.session_state.chain = build_chain(vs)
        st.session_state.system_prompt = SYSTEM_PROMPT

query = st.chat_input("Ask a question about the document...")
if query:
    result = st.session_state.chain.invoke({"input": query})
    st.chat_message("user").write(query)
    st.chat_message("assistant").write(result["answer"])
