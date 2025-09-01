from src.ecu import ECU
from src.keyfob import KeyFob
from src.states import (
    LockState,
    DriveState,
    AuthenticationState,
    PowerState
)
from src.exceptions import InvalidStateError

class BodyControlModule(ECU):
    """
    Represents a Body Control Module (BCM) in a vehicle.
    """
    def __init__(self, part_number, software_version, registered_key_fob_id ):
        # --- Attributes ---
        super().__init__(part_number, software_version)
        self.door_locks = LockState.UNLOCKED
        self.drive_state = DriveState.PARK
        self.authentication_state = AuthenticationState.UNAUTHENTICATED
        self.registered_key_fob_id = registered_key_fob_id

    def run_self_test(self):
        print(f"Running BCM self-test: Checking door lock sensors...")

    # --- Methods (Actions) ---
    def lock_doors(self):
        if not (self.power_status == PowerState.ON and
                self.authentication_state == AuthenticationState.AUTHENTICATED and
                self.drive_state == DriveState.PARK):
            raise InvalidStateError('BCM is not in a valid state to lock doors.')

        # If we get here, all conditions passed
        print("BCM: Locking doors.")
        self.door_locks = LockState.SINGLE_LOCKED

    def unlock_doors(self):
        self.door_locks = LockState.UNLOCKED

    def authenticate(self, key_fob):
        """
        Accept a key_fob object as an argument.
        Compare the key_fob.id_code with the BCM's self.registered_key_fob_id.
        Update the BCM's self.authentication_state based on whether the codes match.
        Return True for success and False for failure.
        """
        if key_fob.id_code == self.registered_key_fob_id:
            self.authentication_state = AuthenticationState.AUTHENTICATED
            return True
        self.authentication_state = AuthenticationState.UNAUTHENTICATED
        return False

    def get_status(self):
        print(f"--- BCM Status ---")
        print(f"  Part Number: {self.part_number}")
        print(f"  SW Version: {self.sw_version}")
        print(f"  Power: {self.power_status}")
        print(f"  Doors: {self.door_locks}")
        print(f"  DTC: {self.dtcs}")
        print(f"--------------------")
