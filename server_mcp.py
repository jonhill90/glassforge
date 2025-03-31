import json
from pathlib import Path
from datetime import datetime

MCP_FILE = Path("client_mcp.json")


def load_mcp():
    if not MCP_FILE.exists():
        raise FileNotFoundError("client_mcp.json not found.")
    with open(MCP_FILE, "r") as f:
        return json.load(f)


def build_prompt_context():
    mcp = load_mcp()
    context = f"""
You are helping a human develop a modular, self-reflective digital agent called Blackglass.

Current Goal:
{mcp.get("current_goal", "")}

Active File:
{mcp.get("active_file", "")}

Notes:
{chr(10).join(f"- {note}" for note in mcp.get("notes", []))}

Recent History:
{chr(10).join(f"- {item}" for item in mcp.get("history", []))}

Last Action:
{mcp.get("last_action", "")}

Last Result:
{mcp.get("last_result", "")}

Timestamp:
{mcp.get("updated", datetime.utcnow().isoformat())}

Provide actionable advice or code edits to help progress toward the goal.
"""
    return context.strip()


if __name__ == "__main__":
    print(build_prompt_context())
