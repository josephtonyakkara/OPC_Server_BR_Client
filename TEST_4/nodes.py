# nodes.py
from asyncua import Server, ua
from config import NAMESPACE_URI, INITIAL_TEMPERATURE

async def build_address_space(server: Server):
    idx = await server.register_namespace(NAMESPACE_URI)
    objects = server.get_objects_node()

    device = await objects.add_object(idx, "Device")
    temperature_node = await device.add_variable(
        idx, "Temperature",
        ua.Variant(INITIAL_TEMPERATURE, ua.VariantType.Float)
    )
    await temperature_node.set_writable(True)
    return temperature_node