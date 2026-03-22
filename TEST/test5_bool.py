import asyncio
from asyncua import Server, ua
from asyncua.crypto.security_policies import SecurityPolicyType

async def main():

    server = Server()
    await server.init()

    # OPC UA endpoint
    server.set_endpoint("opc.tcp://0.0.0.0:5000")

    # No security
    server.set_security_policy([SecurityPolicyType.NoSecurity])

    # Identity (correct)
    server.set_identity_tokens([
        ua.AnonymousIdentityToken
    ])

    # Namespace
    uri = "http://simple.opcua.server"
    idx = await server.register_namespace(uri)

    objects = server.get_objects_node()

    # 🔥 ADD STRUCTURE (important for B&R)
    device = await objects.add_object(idx, "Device")

    # 🔥 BOOLEAN variable
    myvar = await device.add_variable(
        idx,
        "Temperature",
        ua.Variant(True, ua.VariantType.Boolean)
    )
    await myvar.set_writable(True)

    # ---- FIX mandatory nodes ----

    node = server.get_node(ua.NodeId(2735))
    await node.write_value(ua.Variant(10, ua.VariantType.UInt16))

    node = server.get_node(ua.NodeId(2267))
    await node.write_value(ua.Variant(255, ua.VariantType.Byte))

    # ------------------------------

    await server.start()

    print("Server started at opc.tcp://<your-ip>:5000")
    print("Variable: Objects -> Device -> Temperature (BOOL)")

    try:
        # 🔥 Toggle value (important for testing)
        value = True
        while True:
            value = not value
            await myvar.write_value(
                ua.Variant(value, ua.VariantType.Boolean)
            )
            await asyncio.sleep(1)

    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())