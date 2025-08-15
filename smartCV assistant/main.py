# src/main.py
from src.rag.pipeline import RAGPipeline
from src.mcp.handler import MCPHandler
from src.mcp.protocol import MCPMessage

def main():
    # Step 1: Run RAG to get insights
    rag = RAGPipeline()
    job_desc = "We are looking for a Python developer with NLP and FastAPI experience."
    feedback = rag.run(job_description=job_desc, query="Summarize the candidate's qualifications for this role.")

    # Step 2: Prepare MCP message
    mcp_message: MCPMessage = {
        "role": "assistant",
        "content": feedback,
        "context": {
            "hr_email": "recruiter@smartcv.ai",
            "slack_channel": "#hiring-tech",
            "job_role": "NLP Engineer",
            "candidate_id": "CV-1029"
        },
        "tool_calls": [
            {"name": "send_email"},
            {"name": "post_slack"}
        ],
        "tool_responses": None
    }

    # Step 3: Route via MCP
    handler = MCPHandler()
    result = handler.route(mcp_message)

    print("\n[MCP RESULT]:", result["content"])

if __name__ == "__main__":
    main()