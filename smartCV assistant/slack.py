# src/mcp/tools/slack_tool.py
from src.mcp.protocol import MCPMessage

def post_slack_message(mcp_message: MCPMessage) -> MCPMessage:
    context = mcp_message["context"]
    channel = context.get("slack_channel", "#candidates")
    message = mcp_message["content"]

    print(f"[TOOL] Posting to Slack channel {channel}: {message[:100]}...")

    return {
        "role": "tool",
        "content": f"Posted to {channel}",
        "context": context,
        "tool_calls": None,
        "tool_responses": None
    }