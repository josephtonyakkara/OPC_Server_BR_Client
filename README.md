# OPC_Server_BR_Client

## Project Structure

```
opcua_server_project/
│
├── main.py                  # Application entry point
├── config.py                # Configuration settings
│
├── server/
│   ├── opcua_server.py      # OPC UA server initialization and management
│   └── namespace.py         # OPC UA namespace definition and setup
│
├── models/
│   └── system_state.py      # Data models for system state
│
├── services/
│   └── variable_updater.py  # Service for updating OPC UA variables
│
└── utils/
    └── logger.py            # Logging utilities
```

### Directory Breakdown

- **server/**: Contains OPC UA server implementation and namespace management
- **models/**: Data models and system state definitions
- **services/**: Business logic for variable updates and other services
- **utils/**: Utility functions and helpers (logging, etc.)