# src/utils/embeddings.py
from sentence_transformers import SentenceTransformer
from config.settings import settings

class EmbeddingModel:
    def __init__(self, model_name=None):
        self.model = SentenceTransformer(model_name or settings.MODEL_NAME)

    def encode(self, texts):
        return self.model.encode(texts)