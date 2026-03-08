"""System State model - holds application runtime data.

This module defines the SystemState class which stores all runtime data
that needs to be accessible across different parts of the application.

Purpose:
    - Centralized storage for application variables
    - Values are synchronized with OPC UA nodes
    - Can be easily extended with more variables
"""


class SystemState:
    """Stores the complete state of the system at runtime.
    
    This class holds all operational data that:
        1. Needs to be shared across different modules
        2. Is exposed to PLC clients via OPC UA
        3. Gets updated by services (e.g., variable_updater)
    
    Attributes:
        temperature (float): Current system temperature in Celsius
                           Initial value: 25.0°C
                           Updated by: variable_updater service
    
    Example:
        state = SystemState()
        print(state.temperature)  # Output: 25.0
        state.temperature = 30.5  # Update temperature
    
    Extending the class:
        Add new attributes in __init__ and create corresponding
        nodes in namespace.py to expose them to OPC UA clients.
    """
    
    def __init__(self):
        """Initialize system state with default values."""
        # Current temperature reading (in Celsius)
        # This value is synchronized with the Temperature OPC UA node
        # PLC clients can read and modify this value
        self.temperature = 25.0
    
    def __repr__(self):
        """String representation of the system state."""
        return f"SystemState(temperature={self.temperature}°C)"