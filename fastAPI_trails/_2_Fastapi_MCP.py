from mcp.server.fastmcp import FastMCP
import httpx
from typing import Optional

mcp = FastMCP("Items CRUD")
API_BASE = "http://localhost:8000"

@mcp.tool()
async def create_item(name: str, price: float, description: Optional[str] = None) -> dict:
    """Create a new item."""
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{API_BASE}/items/", json={
            "name": name, "price": price, "description": description
        })
        r.raise_for_status()
        return r.json()

@mcp.tool()
async def list_items(skip: int = 0, limit: int = 100) -> list:
    """List all items with pagination."""
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE}/items/", params={"skip": skip, "limit": limit})
        r.raise_for_status()
        return r.json()

@mcp.tool()
async def get_item(item_id: int) -> dict:
    """Get a single item by ID."""
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE}/items/{item_id}")
        r.raise_for_status()
        return r.json()

@mcp.tool()
async def update_item(item_id: int, name: Optional[str] = None,
                     description: Optional[str] = None,
                     price: Optional[float] = None) -> dict:
    """Update fields on an existing item."""
    payload = {k: v for k, v in {"name": name, "description": description, "price": price}.items() if v is not None}
    async with httpx.AsyncClient() as client:
        r = await client.put(f"{API_BASE}/items/{item_id}", json=payload)
        r.raise_for_status()
        return r.json()

@mcp.tool()
async def delete_item(item_id: int) -> dict:
    """Delete an item by ID."""
    async with httpx.AsyncClient() as client:
        r = await client.delete(f"{API_BASE}/items/{item_id}")
        r.raise_for_status()
        return r.json()

if __name__ == "__main__":
    mcp.run()  # stdio transport by default
    