# main.py
import asyncio
from server import create_server
from nodes import build_address_space
from simulator import run_simulation

async def main():
    server = await create_server()
    temperature_node = await build_address_space(server)

    await server.start()
    print(f"Server started at {server.endpoint}")

    try:
        await run_simulation(temperature_node)
    finally:
        await server.stop()
        print("Server stopped.")

if __name__ == "__main__":
    asyncio.run(main())