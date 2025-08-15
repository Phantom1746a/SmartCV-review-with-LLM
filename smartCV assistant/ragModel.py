# src/rag/retriever.py
import faiss
import numpy as np
import pickle
from typing import List, Dict
from src.utils.embeddings import EmbeddingModel
from src.utils.parser import load_documents_from_dir
from config.settings import settings

class ResumeRetriever:
    def __init__(self):
        self.embedding_model = EmbeddingModel()
        self.index = None
        self.doc_store = []  # To map FAISS IDs to documents

    def build_index(self, directory=settings.RESUME_DIR):
        self.doc_store = load_documents_from_dir(directory)
        sentences = [doc["content"] for doc in self.doc_store]
        embeddings = self.embedding_model.encode(sentences)
        embeddings = np.array(embeddings).astype("float32")

        # Build FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

        print(f"Indexed {len(self.doc_store)} resumes.")

    def search(self, query: str, k=3) -> List[Dict]:
        query_embedding = self.embedding_model.encode([query])
        query_embedding = np.array(query_embedding).astype("float32")
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx in indices[0]:
            if idx != -1:
                results.append(self.doc_store[idx])
        return results