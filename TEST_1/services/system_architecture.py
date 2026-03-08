"""
System Architecture Documentation
Displays the project structure, layer responsibilities, and data flow
"""


def print_project_structure():
    """Print the project directory structure"""
    structure = """
opcua_server_project/
│
├── main.py
├── config.py
│
├── server/
│   ├── opcua_server.py
│   └── namespace.py
│
├── models/
│   └── system_state.py
│
├── services/
│   ├── variable_updater.py
│   └── system_architecture.py
│
└── utils/
    └── logger.py
    """
    print(structure)


def print_layer_responsibilities():
    """Print the responsibility of each architectural layer"""
    print("\n" + "="*60)
    print("ARCHITECTURAL LAYERS & RESPONSIBILITIES")
    print("="*60)
    
    layers = [
        ("main.py", "Application startup"),
        ("opcua_server.py", "Server configuration"),
        ("namespace.py", "OPC UA data model"),
        ("system_state.py", "Internal state"),
        ("variable_updater.py", "Runtime logic"),
        ("logger.py", "Logging"),
    ]
    
    print(f"\n{'Layer':<25} {'Responsibility':<35}")
    print("-" * 60)
    for layer, responsibility in layers:
        print(f"{layer:<25} {responsibility:<35}")


def print_data_flow_architecture():
    """Print the data flow and architectural hierarchy"""
    flow = """
DATA FLOW & ARCHITECTURE HIERARCHY
===================================

PLC (OpcUa_Any Client)
        │
        ▼
Python OPC UA Server
        │
        ├── Server Layer
        │   └── opcua_server.py
        │
        ├── Namespace Layer
        │   └── namespace.py
        │
        ├── Application State
        │   └── system_state.py
        │
        └── Services (logic)
            ├── variable_updater.py
            └── logger.py
    """
    print(flow)


def print_complete_architecture():
    """Print complete architecture overview"""
    print("\n" + "#"*60)
    print("# OPCUA SERVER PROJECT - COMPLETE ARCHITECTURE")
    print("#"*60)
    
    print_project_structure()
    print_layer_responsibilities()
    print_data_flow_architecture()


if __name__ == "__main__":
    print_complete_architecture()
