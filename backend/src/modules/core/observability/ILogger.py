from abc import ABC, abstractmethod

class ILogger(ABC):
    @abstractmethod
    def debug(self, message: str, **context) -> None:
        """
        Log a debug-level message.

        Args:
            message (str): The message to log.
            **context: Additional context or metadata to include.
        """
        pass

    @abstractmethod
    def info(self, message: str, **context) -> None:
        """
        Log an info-level message.

        Args:
            message (str): The message to log.
            **context: Additional context or metadata to include.
        """
        pass

    @abstractmethod
    def warning(self, message: str, **context) -> None:
        """
        Log a warning-level message.

        Args:
            message (str): The message to log.
            **context: Additional context or metadata to include.
        """
        pass

    @abstractmethod
    def error(self, message: str, **context) -> None:
        """
        Log an error-level message.

        Args:
            message (str): The message to log.
            **context: Additional context or metadata to include.
        """
        pass

    @abstractmethod
    def critical(self, message: str, **context) -> None:
        """
        Log a critical-level message.

        Args:
            message (str): The message to log.
            **context: Additional context or metadata to include.
        """
        pass
