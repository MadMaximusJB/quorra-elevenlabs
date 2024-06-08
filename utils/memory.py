import faiss
import numpy as np
import openai
from config import OPENAI_API_KEY, EMBEDDING_ENGINE
from datetime import datetime

openai.api_key = OPENAI_API_KEY

class Memory:
    def __init__(self):
        self.index = faiss.IndexFlatL2(1536)  # Dimension of the embeddings
        self.metadata = []  # List to store metadata for each entry

    def add_to_memory(self, text, response):
        embedding = self.get_embedding(text)
        timestamp = datetime.now().isoformat()
        self.metadata.append({'text': text, 'response': response, 'timestamp': timestamp})
        self.index.add(np.array([embedding], dtype=np.float32))
        return self.index.ntotal

    def get_embedding(self, text):
        response = openai.Embedding.create(
            input=text,
            engine=EMBEDDING_ENGINE
        )
        return response['data'][0]['embedding']

    def search_memory(self, query, top_k=5):
        query_embedding = self.get_embedding(query)
        D, I = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)
        return I

    def retrieve_metadata(self, ids):
        return [self.metadata[i] for i in ids.flatten()]

memory = Memory()
