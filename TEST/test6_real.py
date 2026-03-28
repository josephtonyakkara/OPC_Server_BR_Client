import asyncio
from asyncua import Server, ua
from asyncua.crypto.security_policies import SecurityPolicyType

async def main():

    server = Server()
    await server.init()

    server.set_endpoint("opc.tcp://0.0.0.0:5002")

    server.set_security_policy([SecurityPolicyType.NoSecurity])

    server.set_identity_tokens([
        ua.AnonymousIdentityToken
    ])

    uri = "http://simple.opcua.server"
    idx = await server.register_namespace(uri)

    objects = server.get_objects_node()

    # SAME STRUCTURE
    device = await objects.add_object(idx, "Device")

    # 🔥 REAL (Float)
    myvar = await device.add_variable(
        idx,
        "Temperature",
        ua.Variant(25.0, ua.VariantType.Float)
    )
    await myvar.set_writable(True)

    # Mandatory nodes
    await server.get_node(ua.NodeId(2735)).write_value(
        ua.Variant(10, ua.VariantType.UInt16)
    )

    await server.get_node(ua.NodeId(2267)).write_value(
        ua.Variant(255, ua.VariantType.Byte)
    )

    await server.start()

    print("Server started at opc.tcp://<your-ip>:5002")

    try:
        value = 25.0
        while True:
            value += 0.5
            await myvar.write_value(
                ua.Variant(value, ua.VariantType.Float)
            )
            await asyncio.sleep(1)

    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())