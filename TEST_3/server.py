# server.py
from asyncua import Server, ua
from asyncua.crypto.security_policies import SecurityPolicyType
from config import ENDPOINT, SECURITY_POLICIES

async def create_server() -> Server:
    server = Server()
    await server.init()
    server.set_endpoint(ENDPOINT)
    server.set_security_policy([SecurityPolicyType.NoSecurity])
    server.set_identity_tokens([ua.AnonymousIdentityToken])

    # Mandatory capability nodes
    await server.get_node(ua.NodeId(2735)).write_value(
        ua.Variant(10, ua.VariantType.UInt16)
    )
    await server.get_node(ua.NodeId(2267)).write_value(
        ua.Variant(255, ua.VariantType.Byte)
    )
    return server