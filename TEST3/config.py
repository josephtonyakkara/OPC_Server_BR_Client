# config.py
ENDPOINT = "opc.tcp://0.0.0.0:5002"
NAMESPACE_URI = "http://simple.opcua.server"
SECURITY_POLICIES = ["NoSecurity"]
IDENTITY_TOKENS = ["Anonymous"]
SIMULATION_INTERVAL = 1.0      # seconds
SIMULATION_STEP = 0.5          # degrees per tick
INITIAL_TEMPERATURE = 25.0