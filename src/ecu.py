from abc import ABC, abstractmethod

class ECU(ABC):
    """
    Represents a ECU in a vehicle.
    """
    def __init__(self, part_number, software_version):
        # --- Attributes ---
        self.part_number = part_number
        self.sw_version = software_version
        self.power_status = "OFF" # Default power status
        self.dtcs = [] # Default lock status

    @abstractmethod
    def run_self_test(self):
        pass # The parent has no code, it's just a rule

    # --- Methods (Actions) ---
    def power_on(self):
        print(f"ECU {self.part_number}: Powering ON...")
        self.power_status = "ON"

    def power_off(self):
        print(f"ECU {self.part_number}: Powering OFF...")
        self.power_status = "OFF"

    def read_dtcs(self):
        return self.dtcs
