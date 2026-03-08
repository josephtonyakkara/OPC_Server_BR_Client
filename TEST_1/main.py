"""Main entry point for the OPC UA Server application.

This module orchestrates the startup and configuration of an OPC UA (OPC Unified Architecture)
server that communicates with PLC (Programmable Logic Controller) clients.

Flow:
    1. Display system architecture overview
    2. Initialize logger for tracking
    3. Create application state (SystemState)
    4. Initialize OPC UA server with security settings
    5. Register namespace and create OPC UA variables/nodes
    6. Start the server and listen for client connections
    7. Run variable updater service in background
    8. Keep server running until interrupted
"""

import asyncio
from server.opcua_server import create_server
from server.namespace import create_namespace
from models.system_state import SystemState
from services.variable_updater import update_variables
from services.system_architecture import print_complete_architecture
from utils.logger import setup_logger


async def main():
    """Main asynchronous function for OPC UA server initialization and execution.
    
    Steps:
        1. Print complete architecture overview to console
        2. Setup logging system for tracking events
        3. Create SystemState instance for storing application data
        4. Initialize OPC UA server (creates server object and registers namespace)
        5. Create namespace with OPC UA variables/nodes
        6. Start the server (begins listening for client connections)
        7. Create background task for variable updates
        8. Run infinite loop to keep server alive
    """
    # Display architecture on startup - helps developers understand the project structure
    print_complete_architecture()
    
    # Initialize logger for tracking server events, errors, and information
    logger = setup_logger()
    logger.info("Starting OPC UA Server initialization...")

    # Create application state object - holds all runtime data (temperature, etc)
    system_state = SystemState()
    logger.info("SystemState initialized")

    # Create OPC UA server - initializes asyncio server and registers custom namespace
    server, idx = await create_server()
    logger.info(f"OPC UA Server created with namespace index: {idx}")

    # Create OPC UA namespace - adds variable nodes (Temperature, etc) to the server
    # These nodes are what PLC clients can read and write to
    nodes = await create_namespace(server, idx, system_state)
    logger.info(f"Namespace created with {len(nodes)} nodes")

    # Start the OPC UA server - begins listening for client connections
    await server.start()
    logger.info("OPC UA Server started successfully")
    logger.info("Server Endpoint: opc.tcp://<your-ip>:5000")

    # Start background updater service - continuously updates OPC UA variables
    # This runs in parallel with the main loop
    asyncio.create_task(update_variables(system_state, nodes, logger))
    logger.info("Variable updater service started")

    try:
        # Keep the server running indefinitely
        # This loop allows the server to handle client requests continuously
        while True:
            await asyncio.sleep(1)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        logger.info("Server shutdown requested")
    finally:
        # Clean shutdown - stop the server and close connections
        logger.info("Stopping OPC UA Server...")
        await server.stop()
        logger.info("OPC UA Server stopped")


if __name__ == "__main__":
    """Application entry point - runs the async main function."""
    asyncio.run(main())