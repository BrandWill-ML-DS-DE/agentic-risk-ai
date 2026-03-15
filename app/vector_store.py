from langchain_community.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.schema import Document

embedding = OllamaEmbeddings(model="llama3")

def build_vector_store(texts):
    docs = [Document(page_content=t) for t in texts]
    return FAISS.from_documents(docs, embedding)

def retrieve_context(vector_store, query):
    return vector_store.similarity_search(query, k=3)