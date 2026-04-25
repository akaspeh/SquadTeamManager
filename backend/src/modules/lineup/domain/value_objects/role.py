from enum import Enum


class Role(str, Enum):
    FLEX = "flex"
    ANCHOR = "anchor"
    LURKER = "lurker"
    IGL = "igl"
    Pusher = "pusher"