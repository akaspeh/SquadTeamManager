from typing import Any, Callable
from contextvars import ContextVar
from backend.src.modules.core.observability.ICorrelationContext import ICorrelationContext

try:
    from opentelemetry import trace
except ImportError:
    trace = None


# Context-local storage for correlation ID
_correlation_id_var: ContextVar[str | None] = ContextVar(
    "correlation_id",
    default=None,
)


class ContextVarCorrelationContext(ICorrelationContext):
    """
    Context-based implementation of ICorrelationContext.

    This implementation uses Python's contextvars module to store
    and propagate correlation IDs across synchronous and asynchronous
    execution flows.

    It is safe to use with FastAPI, asyncio, and background tasks.
    Optionally integrates with OpenTelemetry by attaching the
    correlation ID to the active span.
    """

    def get_correlation_id(self) -> str:
        """
        Retrieve the current correlation ID from the context.

        If no correlation ID is present, an empty string is returned.

        Returns:
            str: The current correlation ID.
        """
        return _correlation_id_var.get() or ""

    def set_correlation_id(self, correlation_id: str) -> None:
        """
        Set a new correlation ID in the context.

        The correlation ID is stored in a context-local variable
        and, if OpenTelemetry is available, attached to the current span
        as an attribute.

        Args:
            correlation_id (str): The correlation ID to set.
        """
        _correlation_id_var.set(correlation_id)

        if trace:
            span = trace.get_current_span()
            if span and span.is_recording():
                span.set_attribute("correlation.id", correlation_id)

    def run_in_context(self, func: Callable[..., Any], **kwargs) -> Any:
        """
        Execute a function within the current correlation context.

        This method ensures that the correlation ID stored in the
        context is preserved during the execution of the callable.

        Args:
            func (Callable[..., Any]): The callable to execute.
            **kwargs: Additional keyword arguments to pass to the function.

        Returns:
            Any: The result of the executed function.
        """
        correlation_id = self.get_correlation_id()

        def _wrapped():
            if correlation_id:
                _correlation_id_var.set(correlation_id)
            return func(**kwargs)

        return _wrapped()
