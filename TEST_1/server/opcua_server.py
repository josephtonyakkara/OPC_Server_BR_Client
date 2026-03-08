"""OPC UA Server initialization and configuration module.

This module sets up the OPC UA server with endpoint configuration, 
security policies, and namespace registration.

Key Concepts:
    - Endpoint: The network address and port where the server listens
    - Namespace: A logical grouping of variables/nodes in the OPC UA address space
    - Security Policy: Authentication and encryption settings for client connections
"""

from asyncua import Server
from asyncua.ua import AnonymousIdentityToken
from asyncua.crypto.security_policies import SecurityPolicyType
import config


async def create_server():
    """Initialize and configure an OPC UA server.
    
    This function:
        1. Creates a new OPC UA server instance
        2. Initializes the server asynchronously
        3. Sets the network endpoint (IP:Port)
        4. Configures security policy (NoSecurity for testing)
        5. Sets identity tokens (Anonymous for testing)
        6. Registers a custom namespace for application-specific variables
    
    Returns:
        tuple: (server, namespace_index)
            - server: Initialized OPC UA Server object ready to accept connections
            - namespace_index: Integer index for registering variables in the custom namespace
            
    Example:
        server, idx = await create_server()
        # Now you can use 'idx' when adding variables/nodes to the namespace
    """
    # Create a new OPC UA server instance
    server = Server()
    
    # Initialize the server asynchronously
    # This sets up internal structures and event handlers
    await server.init()

    # Set the network endpoint where clients will connect
    # Format: opc.tcp://ip_address:port
    # 0.0.0.0 means listen on all available network interfaces
    server.set_endpoint(config.ENDPOINT)

    # Configure security settings
    # NoSecurity = no encryption or authentication (for testing/local networks only)
    # In production, use proper security policies
    server.set_security_policy([SecurityPolicyType.NoSecurity])
    
    # Set authentication method
    # "Anonymous" = clients don't need credentials (for testing only)
    # In production, implement user/password or certificate authentication
    server.set_identity_tokens([AnonymousIdentityToken])

    # Register custom namespace for application variables
    # This creates a separate namespace where we can add our custom nodes
    # The returned 'idx' is used when adding variables to identify which namespace they belong to
    idx = await server.register_namespace(config.NAMESPACE_URI)

    return server, idx