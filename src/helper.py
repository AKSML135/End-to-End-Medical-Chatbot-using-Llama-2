from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import CTransformers
import os

#Extract data from the PDF
def load_pdf(data):
    loader = DirectoryLoader(data,glob="*.pdf",loader_cls= PyPDFLoader)
    documents = loader.load()
    return documents 

#created text chunks
def text_split(doc):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(doc)
    return text_chunks

#download embedding model
def download_huggingface_embeddings():
    embedding_model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")
    return embedding_model

