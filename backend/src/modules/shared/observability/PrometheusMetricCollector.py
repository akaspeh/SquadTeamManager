from typing import Any
from prometheus_client import Counter, Gauge, Histogram
from backend.src.modules.core.observability.IMetricCollector import IMetricCollector


class PrometheusMetricCollector(IMetricCollector):
    """
    Prometheus-based implementation of IMetricCollector.

    This collector uses the `prometheus_client` library to register
    counters, gauges, and histograms and exposes them via the `/metrics`
    HTTP endpoint for scraping by Prometheus.

    Metric instances are created lazily on first use and cached
    for subsequent updates.
    """

    def __init__(self):
        """
        Initialize the Prometheus metric collector.

        Internal registries are used to cache created Prometheus
        metric objects (Counter, Gauge, Histogram) to avoid
        re-registration and duplication.
        """
        self._counters: dict[str, Counter] = {}
        self._gauges: dict[str, Gauge] = {}
        self._histograms: dict[str, Histogram] = {}

    def increment(self, metric_name: str, value: int = 1, **tags: Any) -> None:
        """
        Increment a Prometheus counter metric by a specified value.

        Counters are monotonically increasing and are typically used
        to track the number of events such as requests, errors,
        retries, or processed messages.

        A counter is created on first use and reused thereafter.
        Tag keys are mapped to Prometheus label names.

        Args:
            metric_name (str): The name of the counter metric.
            value (int, optional): The amount to increment the counter by.
                Defaults to 1.
            **tags: Label key-value pairs associated with the metric.
        """
        counter = self._counters.get(metric_name)
        if not counter:
            counter = Counter(
                metric_name,
                f"Counter metric {metric_name}",
                labelnames=list(tags.keys()),
            )
            self._counters[metric_name] = counter

        counter.labels(**tags).inc(value)

    def gauge(self, metric_name: str, value: float, **tags: Any) -> None:
        """
        Record a Prometheus gauge metric with the given value.

        Gauges represent values that can increase or decrease over time,
        such as memory usage, queue size, or the number of active
        connections.

        A gauge is created on first use and reused thereafter.
        Tag keys are mapped to Prometheus label names.

        Args:
            metric_name (str): The name of the gauge metric.
            value (float): The current value of the gauge.
            **tags: Label key-value pairs associated with the metric.
        """
        gauge = self._gauges.get(metric_name)
        if not gauge:
            gauge = Gauge(
                metric_name,
                f"Gauge metric {metric_name}",
                labelnames=list(tags.keys()),
            )
            self._gauges[metric_name] = gauge

        gauge.labels(**tags).set(value)

    def timing(self, metric_name: str, value: float, **tags: Any) -> None:
        """
        Record a timing metric using a Prometheus histogram.

        Histograms are typically used to observe durations such as
        request latency, job execution time, or external service
        call latency.

        The unit of the recorded value (seconds or milliseconds)
        must be consistent across the application and should be
        documented by convention.

        A histogram is created on first use and reused thereafter.
        Tag keys are mapped to Prometheus label names.

        Args:
            metric_name (str): The name of the timing metric.
            value (float): The duration value to observe.
            **tags: Label key-value pairs associated with the metric.
        """
        histogram = self._histograms.get(metric_name)
        if not histogram:
            histogram = Histogram(
                metric_name,
                f"Timing metric {metric_name}",
                labelnames=list(tags.keys()),
            )
            self._histograms[metric_name] = histogram

        histogram.labels(**tags).observe(value)
