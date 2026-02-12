from abc import ABC, abstractmethod
from typing import Any

class ICorrelationContext(ABC):
    @abstractmethod
    def get_correlation_id(self) -> str:
        """
        Retrieve the current correlation ID from the context.

        Returns:
            str: The current correlation ID.
        """
        pass

    @abstractmethod
    def set_correlation_id(self, correlation_id: str) -> None:
        """
        Set a new correlation ID in the context.

        Args:
            correlation_id (str): The correlation ID to set.
        """
        pass

    @abstractmethod
    def run_in_context(self, func: Any, **kwargs) -> Any:
        """
        Execute a function within the correlation context,
        ensuring the correlation ID is propagated.

        Args:
            func (Any): The callable to execute.
            **kwargs: Additional keyword arguments to pass to the function.

        Returns:
            Any: The result of the executed function.
        """
        pass
