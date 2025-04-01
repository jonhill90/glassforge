import os
from mcp.client.chat import chat
from mcp.tool.builtin import FileTool
from openai import OpenAI

# Setup LLM client
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set workspace directory
workspace_dir = "/workspace"

# Load goal prompt
with open(os.path.join(workspace_dir, "mcp", "goal.md")) as f:
    goal = f.read()

# Create tools and tool context
file_tool = FileTool(workspace_dir=workspace_dir)
tools = {"file": file_tool}

# Simulate chat interaction
response = chat(goal, llm=llm, tools=tools)
print(response.content)

# New file: fastmcp_server.py
from mcp.server.fastmcp.server import FastMCP

server = FastMCP(name="glassforge-agent", instructions="Build the Glassforge framework using goal.md")

@server.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

# Example resource (could serve goal.md or others)
@server.resource("resource://goal")
def read_goal() -> str:
    with open("mcp/goal.md") as f:
        return f.read()

if __name__ == "__main__":
    server.run("stdio")