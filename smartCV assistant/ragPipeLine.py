# src/rag/pipeline.py
from src.rag.retriever import ResumeRetriever
from src.rag.generator import Generator

class RAGPipeline:
    def __init__(self):
        self.retriever = ResumeRetriever()
        self.generator = Generator()

    def run(self, job_description: str, query: str = None) -> str:
        self.retriever.build_index()  # In production: cache this
        relevant_docs = self.retriever.search(job_description)

        context = "\n\n".join([doc["content"] for doc in relevant_docs[:2]])
        query = query or "What are the candidate's key skills and experience relevant to this role?"
        
        return self.generator.generate_feedback(context, query)