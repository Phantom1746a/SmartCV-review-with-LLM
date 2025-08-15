# src/mcp/protocol.py
from typing import TypedDict, Literal

class MCPMessage(TypedDict):
    role: Literal["user", "assistant", "tool"]
    content: str
    context: dict
    tool_calls: list | None
    tool_responses: list | None

# src/mcp/handler.py
from src.mcp.protocol import MCPMessage
from src.mcp.tools.email_tool import send_email_tool
from src.mcp.tools.slack_tool import post_slack_message

TOOL_REGISTRY = {
    "send_email": send_email_tool,
    "post_slack": post_slack_message,
}

class MCPHandler:
    def __init__(self):
        self.tool_history = []

    def route(self, mcp_message: MCPMessage) -> MCPMessage:
        if not mcp_message.get("tool_calls"):
            return mcp_message

        results = []
        for tool_call in mcp_message["tool_calls"]:
            tool_name = tool_call["name"]
            if tool_name in TOOL_REGISTRY:
                print(f"[MCP] Routing to tool: {tool_name}")
                response = TOOL_REGISTRY[tool_name](mcp_message)
                self.tool_history.append(response)
                results.append(response["content"])
            else:
                results.append(f"Tool {tool_name} not found.")

        return {
            "role": "assistant",
            "content": "\n".join(results),
            "context": mcp_message["context"],
            "tool_calls": None,
            "tool_responses": results
        }    