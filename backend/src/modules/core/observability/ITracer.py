from abc import ABC, abstractmethod
from typing import Any

class ITracer(ABC):
    @abstractmethod
    def start_span(self, name: str, **attributes: Any) -> Any:
        """
        Start a new tracing span.

        Args:
            name (str): The name of the span.
            **attributes: Optional attributes or metadata to attach to the span.

        Returns:
            Any: The span object that can be used to set attributes or end the span.
        """
        pass

    @abstractmethod
    def set_attribute(self, key: str, value: Any) -> None:
        """
        Set an attribute on the current span.

        Args:
            key (str): The name of the attribute.
            value (Any): The value of the attribute.
        """
        pass

    @abstractmethod
    def end_span(self, span: Any) -> None:
        """
        End the specified span.

        Args:
            span (Any): The span object to end.
        """
        pass
