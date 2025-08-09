from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

import os

data_path = "./data/"
chroma_path = "chroma_db"
embed_model = "mxbai-embed-large"

def main():
    # Indexing
    documents = []
    for filename in os.listdir(data_path):
        if filename.endswith(".pdf"):
            pdf_path =os.path.join(data_path, filename)
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())

    # Splitting the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    # Creating embeddings and store in Chroma
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=OllamaEmbeddings(model=embed_model),
        persist_directory=chroma_path
    )

    # For debugging
    # print("Success!")

if __name__ == "__main__":
    main()