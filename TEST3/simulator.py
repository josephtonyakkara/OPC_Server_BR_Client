# simulator.py
import asyncio
from asyncua import ua
from config import SIMULATION_INTERVAL, SIMULATION_STEP, INITIAL_TEMPERATURE

async def run_simulation(temperature_node):
    value = INITIAL_TEMPERATURE
    while True:
        value += SIMULATION_STEP
        await temperature_node.write_value(
            ua.Variant(value, ua.VariantType.Float)
        )
        await asyncio.sleep(SIMULATION_INTERVAL)