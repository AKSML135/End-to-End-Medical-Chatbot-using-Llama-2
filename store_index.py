from src.helper import load_pdf, text_split, download_huggingface_embeddings
import pinecone
from langchain.vectorstores import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

#loading pdf, chunking it and loading with mini lm embedding model
doc = load_pdf("data/")
text_chunks = text_split(doc)
embed_model = download_huggingface_embeddings()

#Initialising Pinecone with api key and environment and using created index
pinecone.init(api_key  = PINECONE_API_KEY, environment= PINECONE_API_ENV)
index_name = "medical-chatbot"

#Creating Embeddings for Each of The Text Chunks & storing
docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embed_model, index_name=index_name)
