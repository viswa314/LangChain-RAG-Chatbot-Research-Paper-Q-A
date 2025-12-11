from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path


def load_docs():
    pdf_path = Path("data/Sarcasm_Aware_Neural_Translation_for_Informal_Social_Media_Texts_in_Low_Resource_Languages.pdf")
    docs = PyMuPDFLoader(str(pdf_path)).load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)
