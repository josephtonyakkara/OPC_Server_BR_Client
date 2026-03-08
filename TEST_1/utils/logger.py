"""Logger utility for the OPC UA Server application.

This module provides logging functionality for tracking server events,
errors, and important information during operation.

Logging Levels:
    DEBUG: Detailed information for debugging (lowest priority)
    INFO: General informational messages
    WARNING: Warning messages for potentially problematic situations
    ERROR: Error messages for serious problems
    CRITICAL: Critical messages for system failures (highest priority)

Usage:
    logger = setup_logger()
    logger.info("Server started")
    logger.error("Connection failed")
"""

import logging


def setup_logger():
    """Initialize and configure the application logger.
    
    This function:
        1. Sets the logging level to INFO (shows info and above)
        2. Formats log messages with timestamp and level
        3. Creates and returns a logger instance for the OPC UA server
    
    Log Format:
        "2026-03-09 10:30:45,123 [INFO] Your message here"
        timestamps are included automatically
    
    Returns:
        logging.Logger: Configured logger instance with name 'opcua_server'
        
    Example:
        logger = setup_logger()
        logger.info("Application started")  # INFO level message
        logger.warning("Low memory")        # WARNING level message
        logger.error("Connection failed")   # ERROR level message
    """
    # Configure the basic logging system
    # This sets up how all messages will be formatted and where they go
    logging.basicConfig(
        # Set minimum log level to INFO
        # This means DEBUG messages won't be shown (only INFO and above)
        level=logging.INFO,
        
        # Format string: %(asctime)s = timestamp, %(levelname)s = log level, %(message)s = message
        # Example output: "2026-03-09 10:30:45,123 [INFO] Server started"
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    
    # Create and return a logger instance named "opcua_server"
    # This name appears in error messages and helps identify the source
    return logging.getLogger("opcua_server")