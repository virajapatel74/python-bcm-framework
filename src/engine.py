from src.ecu import ECU

class EngineControlUnit (ECU):
    """
    Represents a Engine Control Unit in a vehicle.
    """
    def __init__(self, part_number, software_version):
        # --- Attributes ---
        super().__init__(part_number, software_version)
        self.engine_state  = "OFF" # Default lock status

    def run_self_test(self):
        print(f"Running ECU self-test: Checking engine status...")

    # --- Methods (Actions) ---
    def engine_run(self):
        self.engine_state = "RUNNING"
        print(f"Engine State: {self.engine_state}...")
