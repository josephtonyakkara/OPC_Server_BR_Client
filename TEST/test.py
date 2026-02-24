import asyncio
from asyncua import Server

async def main():
    # Create server
    server = Server()
    await server.init()

    # IMPORTANT: allow external PLC connection
    server.set_endpoint("opc.tcp://0.0.0.0:5000")

    # No security (for lab testing)
    from asyncua.crypto.security_policies import SecurityPolicyType
    server.set_security_policy([SecurityPolicyType.NoSecurity])
    server.set_security_IDs(["Anonymous"])

    # Create namespace
    uri = "http://simple.opcua.server"
    idx = await server.register_namespace(uri)

    # Get Objects node
    objects = server.get_objects_node()

    # Add one variable directly under Objects
    myvar = await objects.add_variable(idx, "Temperature", 25.0)

    # Make it writable (optional)
    await myvar.set_writable(True)

    # Start server
    await server.start()
    print("Server started at opc.tcp://<your-ip>:4840")
    print("Variable: Objects → Temperature")

    try:
        while True:
            await asyncio.sleep(1)
    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())