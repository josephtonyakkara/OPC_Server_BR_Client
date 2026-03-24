import asyncio
import struct
from asyncua import Server, ua
from asyncua.crypto.security_policies import SecurityPolicyType

async def main():

    server = Server()
    await server.init()

    # OPC UA endpoint
    server.set_endpoint("opc.tcp://0.0.0.0:5000")

    # No security
    server.set_security_policy([SecurityPolicyType.NoSecurity])

    server.set_identity_tokens([
        ua.AnonymousIdentityToken
    ])

    # Namespace
    uri = "http://simple.opcua.server"
    idx = await server.register_namespace(uri)

    objects = server.get_objects_node()

    # Structure
    device = await objects.add_object(idx, "Device")

    # Initial value
    value = 25

    # 🔥 BYTE SWAP FUNCTION
    def swap_uint16(val):
        return struct.unpack("<H", struct.pack(">H", val))[0]

    # Apply swap for initial value
    swapped_value = swap_uint16(value)

    myvar = await device.add_variable(
        idx,
        "Temperature",
        ua.Variant(swapped_value, ua.VariantType.UInt16)
    )
    await myvar.set_writable(True)

    # ---- FIX mandatory nodes ----
    await server.get_node(ua.NodeId(2735)).write_value(
        ua.Variant(10, ua.VariantType.UInt16)
    )

    await server.get_node(ua.NodeId(2267)).write_value(
        ua.Variant(255, ua.VariantType.Byte)
    )
    # ------------------------------

    await server.start()

    print("Server started at opc.tcp://<your-ip>:5000")
    print("Variable: Objects -> Device -> Temperature (UINT with byte swap)")

    try:
        value = 25
        while True:
            value += 1
            if value > 100:
                value = 0

            # 🔥 APPLY BYTE SWAP HERE
            swapped_value = swap_uint16(value)

            await myvar.write_value(
                ua.Variant(swapped_value, ua.VariantType.UInt16)
            )

            print(f"Original: {value} → Swapped: {swapped_value}")

            await asyncio.sleep(1)

    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())