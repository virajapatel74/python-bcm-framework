from src.ecu import ECU

class BodyControlModule(ECU):
    """
    Represents a Body Control Module (BCM) in a vehicle.
    """
    def __init__(self, part_number, software_version):
        # --- Attributes ---
        super().__init__(part_number, software_version)
        self.door_locks = "UNLOCKED" # Default lock status

    def run_self_test(self):
        print(f"Running BCM self-test: Checking door lock sensors...")

    # --- Methods (Actions) ---
    def lock_doors(self):
        self.door_locks = "LOCKED"

    def unlock_doors(self):
        self.door_locks = "UNLOCKED"

    def get_status(self):
        print(f"--- BCM Status ---")
        print(f"  Part Number: {self.part_number}")
        print(f"  SW Version: {self.sw_version}")
        print(f"  Power: {self.power_status}")
        print(f"  Doors: {self.door_locks}")
        print(f"  DTC: {self.dtcs}")
        print(f"--------------------")
