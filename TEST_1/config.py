"""Configuration settings for the OPC UA Server application.

This module centralizes all configuration values used throughout the application.
Modify these settings to customize server behavior.
"""

# ============================================================================
# SERVER ENDPOINT CONFIGURATION
# ============================================================================

# Network endpoint where the server listens for client connections
# Format: opc.tcp://ip_address:port
# 0.0.0.0 = Listen on all available network interfaces
# 5000 = Port number (any available port can be used)
# Change to your actual IP for remote connections, e.g., "opc.tcp://192.168.1.100:5000"
ENDPOINT = "opc.tcp://0.0.0.0:5000"

# ============================================================================
# NAMESPACE CONFIGURATION
# ============================================================================

# Unique identifier for the custom namespace
# This URI identifies your namespace in the OPC UA address space
# Format: URI (http://...)
# Used to distinguish your variables from other OPC UA servers
NAMESPACE_URI = "http://simple.opcua.server"

# ============================================================================
# SERVICE CONFIGURATION
# ============================================================================

# Interval (in seconds) for updating OPC UA variables
# Controls how often the variable_updater service refreshes values
# Lower values = more frequent updates (higher CPU usage)
# Higher values = less frequent updates (less responsive)
# Example: 1 second = update once per second
UPDATE_INTERVAL = 1  # seconds