from enum import Enum

class KitCategoryEnum(str, Enum):
    SPECIALIST = "Specialist"
    FIRE_SUPPORT = "Fire Support"
    DIRECT_COMBAT = "Direct Combat"
    COMMAND_AND_SUPPORT = "Command and Support"