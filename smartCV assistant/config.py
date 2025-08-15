# config/settings.py
import os

class Settings:
    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    LLM_MODEL = "gpt-2"  # Placeholder; use Hugging Face or OpenAI API in practice
    EMBEDDING_DIM = 384
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    RESUME_DIR = "../data/resumes"
    JOB_DESC_DIR = "../data/job_descriptions"
    FAISS_INDEX_PATH = "faiss_index.bin"

settings = Settings()