import asyncio
from asyncua import Server, ua
from asyncua.crypto.security_policies import SecurityPolicyType

async def main():
    server = Server()
    await server.init()

    # Listening on all interfaces (0.0.0.0)
    server.set_endpoint("opc.tcp://0.0.0.0:5002")
    server.set_security_policy([SecurityPolicyType.NoSecurity])

    uri = "http://simple.opcua.server"
    idx = await server.register_namespace(uri)

    # Create the folder/object
    objects = server.get_objects_node()
    device = await objects.add_object(idx, "Device")

    # 🔥 CONSTANT VALUE (Float)
    # This value is set once and never changed by the script
    constant_temp = 25.0
    myvar = await device.add_variable(
        idx,
        "Temperature",
        ua.Variant(constant_temp, ua.VariantType.Float)
    )
    
    # Optional: Keep it writable so CLIENTS can change it, 
    # but the server script won't touch it.
    await myvar.set_writable(True)

    # Mandatory nodes for some UA clients
    await server.get_node(ua.NodeId(2735)).write_value(ua.Variant(10, ua.VariantType.UInt16))
    await server.get_node(ua.NodeId(2267)).write_value(ua.Variant(255, ua.VariantType.Byte))

    await server.start()
    
    print(f"Server started at opc.tcp://0.0.0.0:5002")
    print(f"Temperature is set to a constant: {constant_temp}")

    try:
        # Instead of a loop that changes values, we use an infinite 
        # sleep to keep the server process alive.
        while True:
            await asyncio.sleep(3600)  # Sleep for an hour, then repeat
    except asyncio.CancelledError:
        pass
    finally:
        await server.stop()
        print("Server stopped.")

if __name__ == "__main__":
    asyncio.run(main())