"""Variable Update Service - Continuously updates OPC UA variables.

This module handles the background service that updates system variables
periodically, simulating real-world sensor data or PLC updates.

Purpose:
    - Simulate continuous data updates from sensors/PLC
    - Update OPC UA nodes with new values
    - Allow PLC clients to always see the latest data
"""

import asyncio
import config


async def update_variables(system_state, nodes, logger):
    """Background service for updating OPC UA variables.
    
    This function runs indefinitely in the background, periodically updating:
        1. Application state values (SystemState)
        2. OPC UA node values (what clients see)
    
    Flow:
        1. Increment system_state.temperature by 0.5°C
        2. Write the new value to the OPC UA Temperature node
        3. Log the update for monitoring
        4. Wait for UPDATE_INTERVAL seconds
        5. Repeat steps 1-4 indefinitely
    
    Args:
        system_state: SystemState instance containing runtime values
        nodes: Dictionary of OPC UA node objects (e.g., {"temperature": node})
        logger: Logger instance for recording updates
    
    Note:
        - This is run as a background task via asyncio.create_task()
        - It runs in parallel with the main server loop
        - The sleep time is configurable via config.UPDATE_INTERVAL
    """
    while True:
        # Simulate temperature sensor reading
        # In a real application, this would read from an actual sensor
        # or receive data from a PLC
        system_state.temperature += 0.5
        logger.debug(f"Updated system_state.temperature to {system_state.temperature}")

        # Write the new temperature value to the OPC UA Temperature node
        # This synchronizes the internal state with what PLC clients see
        # Clients monitoring the Temperature node will receive this update
        await nodes["temperature"].write_value(system_state.temperature)
        logger.info(f"Temperature updated to OPC UA server: {system_state.temperature}°C")

        # Wait before the next update
        # This controls how frequently variables are updated
        # Configured in config.py (default: 1 second)
        await asyncio.sleep(config.UPDATE_INTERVAL)