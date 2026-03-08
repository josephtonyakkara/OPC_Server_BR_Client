"""OPC UA Namespace creation and variable definition module.

This module defines the OPC UA address space structure - the variables/nodes
that PLC clients can access and monitor.

Key Concepts:
    - Namespace: Container for related variables/nodes
    - Nodes: Variables that clients can read and write
    - Objects Node: Root container where all application variables are added
"""


async def create_namespace(server, idx, system_state):
    """Create OPC UA namespace with application-specific variables.
    
    This function:
        1. Gets the Objects node (root container for application variables)
        2. Creates a Temperature variable node
        3. Sets the variable as writable (clients can change its value)
        4. Returns a dictionary of created nodes for reference in the application
    
    Args:
        server: The OPC UA Server instance (created by create_server())
        idx: Namespace index (returned by register_namespace())
        system_state: SystemState instance containing the variable values
    
    Returns:
        dict: Dictionary mapping variable names to their OPC UA node objects
              Example: {"temperature": <NodeObject>}
              
    Note:
        - All variables start with values from system_state
        - Setting 'writable=True' allows PLC clients to modify the values
        - New variables should be added here and returned in the dictionary
    """
    # Get the Objects node - the root container in OPC UA address space
    # All application variables should be added as children of this node
    objects = server.get_objects_node()

    # Create a Temperature variable node
    # Parameters:
    #   idx = namespace index (identifies which namespace this variable belongs to)
    #   "Temperature" = the variable name (displayed to clients)
    #   system_state.temperature = initial value (25.0 from SystemState)
    temperature_node = await objects.add_variable(
        idx,
        "Temperature",
        system_state.temperature
    )

    # Allow PLC clients to write (modify) the temperature value
    # If writable=False, clients could only read the value
    await temperature_node.set_writable(True)

    # Return all created nodes for use in other parts of the application
    # This dictionary allows quick access to nodes for updating values
    return {
        "temperature": temperature_node
    }