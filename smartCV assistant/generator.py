# src/rag/generator.py
from transformers import pipeline, set_seed
from typing import List, Dict

class Generator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)
        set_seed(42)

    def generate_feedback(self, context: str, question: str) -> str:
        prompt = f"""
        Based on the following resume information:
        {context}

        Question: {question}
        Answer:
        """
        outputs = self.generator(prompt, max_new_tokens=200, num_return_sequences=1)
        return outputs[0]["generated_text"][len(prompt):].strip()