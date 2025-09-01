from enum import Enum

class DriveState(Enum):
    """
    Represents a Drive States of Engine Control Unit.
    """
    # --- Attributes ---
    PARK = 0
    REVERSE = 1
    NEUTRAL = 2
    DRIVE = 3


class LockState(Enum):
    """
    Represents a Lock Status of the vechicle.
    """
    # --- Attributes ---
    UNLOCKED = 0
    SINGLE_LOCKED = 1
    DOUBLE_LOCKED = 2


class AuthenticationState(Enum):
    """
    Represents a Authentication Status of Key fob.
    """
    # --- Attributes ---
    UNAUTHENTICATED = 0
    AUTHENTICATED = 1


class PowerState(Enum):
    """
    Represents the Power Status of the ECU in question.
    """
    # --- Attributes ---
    OFF = 0
    ON = 1


class EngineState(Enum):
    """
    Represents the Engine Status of the vehicle.
    """
    # --- Attributes ---
    OFF = 0
    RUNNING = 1
