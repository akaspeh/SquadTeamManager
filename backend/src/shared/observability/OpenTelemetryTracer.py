from typing import Any
from opentelemetry import trace
from opentelemetry.trace import Span
from backend.src.modules.core.observability.ITracer import ITracer


class OpenTelemetryTracer(ITracer):
    """
    OpenTelemetry-based implementation of ITracer.

    This tracer delegates span management to the OpenTelemetry SDK
    and integrates with the active tracing context.
    """

    def __init__(self, tracer_name: str):
        """
        Initialize the OpenTelemetry tracer.

        Args:
            tracer_name (str): Logical name of the tracer, typically
                the service or module name.
        """
        self._tracer = trace.get_tracer(tracer_name)
        self._current_span: Span | None = None

    def start_span(self, name: str, **attributes: Any) -> Span:
        """
        Start a new tracing span.

        The span is created as a child of the currently active span,
        if one exists, and is set as the current span in the context.

        Args:
            name (str): The name of the span.
            **attributes: Optional attributes to attach to the span.

        Returns:
            Span: The created OpenTelemetry span instance.
        """
        span = self._tracer.start_span(name)

        for key, value in attributes.items():
            span.set_attribute(key, value)

        self._current_span = span
        return span

    def set_attribute(self, key: str, value: Any) -> None:
        """
        Set an attribute on the current active span.

        If no span is currently active, this method does nothing.

        Args:
            key (str): The name of the attribute.
            value (Any): The value of the attribute.
        """
        if self._current_span is not None:
            self._current_span.set_attribute(key, value)

    def end_span(self, span: Span) -> None:
        """
        End the specified tracing span.

        Args:
            span (Span): The span object to end.
        """
        span.end()

        if self._current_span is span:
            self._current_span = None
