from abc import ABC, abstractmethod
from typing import Any

class IMetricCollector(ABC):
    @abstractmethod
    def increment(self, metric_name: str, value: int = 1, **tags: Any) -> None:
        """
        Increment a counter metric by a specified value.

        Args:
            metric_name (str): The name of the metric to increment.
            value (int, optional): The amount to increment by. Defaults to 1.
            **tags: Additional tags or metadata associated with the metric.
        """
        pass

    @abstractmethod
    def gauge(self, metric_name: str, value: float, **tags: Any) -> None:
        """
        Record a gauge metric with the given value.

        Args:
            metric_name (str): The name of the gauge metric.
            value (float): The current value of the gauge.
            **tags: Additional tags or metadata associated with the metric.
        """
        pass

    @abstractmethod
    def timing(self, metric_name: str, value: float, **tags: Any) -> None:
        """
        Record a timing metric (duration) in milliseconds or seconds.

        Args:
            metric_name (str): The name of the timing metric.
            value (float): The duration to record.
            **tags: Additional tags or metadata associated with the metric.
        """
        pass
