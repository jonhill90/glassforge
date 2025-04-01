from mcp.server.fastmcp.server import FastMCP
from mcp.server.fastmcp.resources import FunctionResource
from pydantic.networks import AnyUrl

server = FastMCP(
    name="glassforge-agent",
    instructions="Build the Glassforge framework using goal.md"
)

@server.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"

server.add_resource(FunctionResource(
    uri=AnyUrl("resource://goal"),
    name="Goal",
    description="The current Glassforge goal",
    mime_type="text/plain",
    fn=lambda: open("goal.md").read()
))

if __name__ == "__main__":
    print("🔍 Registered Resources:", [r.uri for r in server._resource_manager.list_resources()])
    server.run("stdio")