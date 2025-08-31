# 1. Import the class from the src folder
from src.bcm import BodyControlModule
from src.engine import EngineControlUnit

def run_system_check(ecu_list: list):
    """loop through the list and call the power_on() method for each ECU in the list."""

    for ecu in ecu_list:
        ecu.power_on()
        print(f"ECU Power Status {ecu.power_status}... ")

# 2. Create an instance of our BCM with the required arguments
my_bcm = BodyControlModule(part_number="FPGA_1234", software_version="v2.3.0")
my_ecu = EngineControlUnit(part_number="FPGA_2345", software_version="v3.3.0")

# Running self test as per requirement 
my_bcm.run_self_test()
my_ecu.run_self_test()

# 3. Interact with our BCM object
print("--- Initial Status ---")
my_bcm.get_status()

print("\n--- Powering ON all the ECUs ---")
run_system_check([my_bcm, my_ecu])

# 4. Checking locking status changes
print("\n--- Action to Lock the door ---")
my_bcm.lock_doors()

print("\n--- call engine run method ---")
my_ecu.engine_run()

print("\n--- Powering OFF all the ECUs ---")
my_bcm.power_off()
my_ecu.power_off()

print("\n--- Final Status ---")
my_bcm.get_status()
