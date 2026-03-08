import asyncio
import config


async def update_variables(system_state, nodes, logger):

    while True:

        # simulate temperature change
        system_state.temperature += 0.5

        await nodes["temperature"].write_value(system_state.temperature)

        logger.info(f"Temperature updated: {system_state.temperature}")

        await asyncio.sleep(config.UPDATE_INTERVAL)