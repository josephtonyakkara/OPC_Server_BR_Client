from asyncua import Server
from asyncua.crypto.security_policies import SecurityPolicyType
import config


async def create_server():
    server = Server()
    await server.init()

    server.set_endpoint(config.ENDPOINT)

    # Disable security (for testing)
    server.set_security_policy([SecurityPolicyType.NoSecurity])
    server.set_identity_tokens(["Anonymous"])

    idx = await server.register_namespace(config.NAMESPACE_URI)

    return server, idx