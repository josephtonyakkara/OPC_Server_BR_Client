import asyncio
from asyncua import Server, ua
from asyncua.crypto.security_policies import SecurityPolicyType

async def main():

    server = Server()
    await server.init()

    # OPC UA endpoint
    server.set_endpoint("opc.tcp://0.0.0.0:5002")

    # No security
    server.set_security_policy([SecurityPolicyType.NoSecurity])

    # ✅ UPDATED (replace deprecated method)
    server.set_identity_tokens([
    ua.AnonymousIdentityToken
])

    # Namespace
    uri = "http://simple.opcua.server"
    idx = await server.register_namespace(uri)

    objects = server.get_objects_node()

    # Example variable (INT type)
    myvar = await objects.add_variable(idx, "Temperature", ua.Variant(25, ua.VariantType.Int16))
    await myvar.set_writable(True)

    # ---- FIX mandatory nodes ----

    # MaxBrowseContinuationPoints
    node = server.get_node(ua.NodeId(2735))
    await node.write_value(ua.Variant(10, ua.VariantType.UInt16))

    # ServiceLevel
    node = server.get_node(ua.NodeId(2267))
    await node.write_value(ua.Variant(255, ua.VariantType.Byte))

    # ------------------------------

    await server.start()

    print("Server started at opc.tcp://<your-ip>:5002")
    print("Variable: Objects -> Temperature")

    try:
        while True:
            await asyncio.sleep(1)

    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())