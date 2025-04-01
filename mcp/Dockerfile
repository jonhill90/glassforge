FROM python:3.11-slim

WORKDIR /workspace

# Install system packages
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Copy in requirements early for caching
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the MCP agent code
COPY . /workspace/mcp

CMD ["python", "/workspace/mcp/fastmcp_server.py"]

# Create fastmcp_server.py
RUN echo 'from mcp.server.fastmcp.server import FastMCP\n\nserver = FastMCP(name="glassforge-agent", instructions="Build the Glassforge framework using goal.md")\n\n@server.tool()\ndef hello(name: str) -> str:\n    return f"Hello, {name}!"\n\n@server.resource("resource://goal")\ndef read_goal() -> str:\n    with open("mcp/goal.md") as f:\n        return f.read()\n\nif __name__ == "__main__":\n    server.run("stdio")' > /workspace/mcp/fastmcp_server.py