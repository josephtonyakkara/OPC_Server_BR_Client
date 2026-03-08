import asyncio

from server.opcua_server import create_server
from server.namespace import create_namespace
from models.system_state import SystemState
from services.variable_updater import update_variables
from utils.logger import setup_logger


async def main():

    logger = setup_logger()

    # Create application state
    system_state = SystemState()

    # Create OPC UA server
    server, idx = await create_server()

    # Create OPC UA namespace
    nodes = await create_namespace(server, idx, system_state)

    # Start server
    await server.start()

    logger.info("OPC UA Server started")
    logger.info("Endpoint: opc.tcp://<your-ip>:5000")

    # Start background updater
    asyncio.create_task(update_variables(system_state, nodes, logger))

    try:
        while True:
            await asyncio.sleep(1)

    finally:
        await server.stop()


if __name__ == "__main__":
    asyncio.run(main())