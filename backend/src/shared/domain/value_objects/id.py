from dataclasses import dataclass
import uuid


@dataclass(frozen=True)
class ID:
    value: str

    @staticmethod
    def new() -> "ID":
        return ID(str(uuid.uuid4()))

    def __str__(self) -> str:
        return self.value
