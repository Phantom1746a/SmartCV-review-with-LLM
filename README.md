
# 🧠 SmartCV Assistant: RAG + MCP Resume Intelligence System

A modular AI-powered resume analyzer that combines **Retrieval-Augmented Generation (RAG)** with **Model Context Protocol (MCP)** principles to deliver context-aware, secure, and tool-integrated candidate insights.

Perfect for HR automation, ATS enhancement, and demonstrating modern LLM engineering practices.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-green)
![MCP](https://img.shields.io/badge/MCP-Simulated-orange)
![Modular](https://img.shields.io/badge/Architecture-Modular-brightgreen)

---

## 🚀 Overview

SmartCV Assistant retrieves relevant candidate resumes using semantic search, generates AI-powered feedback via LLMs, and securely routes results to external tools (e.g., email, Slack) using **MCP-inspired structured context handling**.

This project demonstrates:
- Advanced RAG pipeline design
- Simulated **Model Context Protocol (MCP)** for secure tool communication
- Modular, production-ready Python architecture
- Responsible AI with auditable context flow

> 🔍 *Ideal for AI Engineers, NLP Developers, and LLM Ops roles.*

---

## 📸 Example Output

When analyzing a resume for an **NLP Engineer** role:

```text



smartcv_assistant/
├── src/
│   ├── rag/             # Retrieval + Generation
│   │   ├── retriever.py → FAISS + BERT
│   │   ├── generator.py → LLM feedback
│   │   └── pipeline.py  → RAG orchestration
│   │
│   ├── mcp/             # Model Context Protocol
│   │   ├── protocol.py  → TypedDict schema
│   │   ├── tools/       → Email, Slack, etc.
│   │   └── handler.py   → Tool routing
│   │
│   └── utils/           → Embeddings, parsing
│
├── data/
│   ├── resumes/         → .txt resume files
│   └── job_descriptions/
│
└── main.py              → Entry point
