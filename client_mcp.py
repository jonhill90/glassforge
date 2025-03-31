import json
import typer
from datetime import datetime
from pathlib import Path

app = typer.Typer()
MCP_FILE = Path("client_mcp.json")


def load_mcp():
    if not MCP_FILE.exists():
        typer.echo("client_mcp.json not found.")
        raise typer.Exit()
    with open(MCP_FILE, "r") as f:
        return json.load(f)


def save_mcp(data):
    data["updated"] = datetime.utcnow().isoformat()
    with open(MCP_FILE, "w") as f:
        json.dump(data, f, indent=2)
    typer.echo("MCP updated.")


@app.command()
def goal(text: str):
    """Set the current development goal."""
    data = load_mcp()
    data["current_goal"] = text
    save_mcp(data)


@app.command()
def file(path: str):
    """Set the currently active file."""
    data = load_mcp()
    data["active_file"] = path
    save_mcp(data)


@app.command()
def note(text: str):
    """Add a note to the MCP."""
    data = load_mcp()
    data["notes"].append(text)
    save_mcp(data)


@app.command()
def history(item: str):
    """Add an item to the dev history."""
    data = load_mcp()
    data["history"].append(item)
    save_mcp(data)


@app.command()
def show():
    """Display the current MCP state."""
    data = load_mcp()
    typer.echo(json.dumps(data, indent=2))


if __name__ == "__main__":
    app()
