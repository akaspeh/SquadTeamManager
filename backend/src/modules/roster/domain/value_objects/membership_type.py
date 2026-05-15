from dataclasses import dataclass
import re


@dataclass(frozen=True)
class MembershipType:
    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError("MembershipType cannot be empty")

        if len(self.value) > 32:
            raise ValueError("MembershipType too long")

        if not re.match(r"^[a-zA-Z0-9_ -]+$", self.value):
            raise ValueError("Invalid MembershipType format")

    def normalized(self) -> str:
        return self.value.strip().lower().replace(" ", "_")