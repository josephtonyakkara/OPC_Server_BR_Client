async def create_namespace(server, idx, system_state):
    objects = server.get_objects_node()

    # Create variable
    temperature_node = await objects.add_variable(
        idx,
        "Temperature",
        system_state.temperature
    )

    await temperature_node.set_writable(True)

    return {
        "temperature": temperature_node
    }