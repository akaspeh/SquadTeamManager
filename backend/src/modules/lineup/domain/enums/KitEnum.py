from enum import Enum

class KitEnum(str, Enum):
    SQUAD_LEADER = "Squad Leader"
    MEDIC = "Medic"
    MORTAR = "Mortar"
    LOGISTIC = "Logistic"
    PILOT = "Pilot"
    CREWMAN = "Crewman"

    RIFLEMAN = "Rifleman"
    RAIDER = "Raider"
    AUTOMATIC_RIFLEMAN = "Automatic Rifleman"

    GRENADIER = "Grenadier"
    LIGHT_ANTI_TANK = "Light Anti Tank"
    MARKSMAN = "Marksman"
    SCOUT = "Scout"

    SNIPER = "Sniper"
    MACHINE_GUNNER = "Machine Gunner"
    HEAVY_ANTI_TANK = "Heavy Anti Tank"
    COMBAT_ENGINEER = "Combat Engineer"
    DRONE_OPERATOR = "Drone Operator"
