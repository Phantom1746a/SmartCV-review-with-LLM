# src/utils/parser.py
import os
from config.settings import settings

def read_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def load_documents_from_dir(directory):
    docs = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            content = read_text_file(filepath)
            docs.append({
                "id": filename,
                "content": content,
                "source": filepath
            })
    return docs