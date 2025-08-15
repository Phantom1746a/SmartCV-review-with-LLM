# src/mcp/tools/email_tool.py
from src.mcp.protocol import MCPMessage

def send_email_tool(mcp_message: MCPMessage) -> MCPMessage:
    context = mcp_message["context"]
    recipient = context.get("hr_email", "hr@company.com")
    body = mcp_message["content"]

    # Simulate sending email
    print(f"[TOOL] Email sent to {recipient}: {body[:100]}...")

    return {
        "role": "tool",
        "content": f"Email successfully sent to {recipient}",
        "context": context,
        "tool_calls": None,
        "tool_responses": None
    }