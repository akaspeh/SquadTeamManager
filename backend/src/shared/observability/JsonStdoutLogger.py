import sys
import json
import datetime
from backend.src.modules.core.observability.ILogger import ILogger


class JsonStdoutLogger(ILogger):
    def __init__(self, service: str, environment: str):
        self._service = service
        self._env = environment

    def _log(self, level: str, message: str, **context):
        payload = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "level": level,
            "service": self._service,
            "env": self._env,
            "message": message,
            **context,
        }

        # ensure_ascii=False чтобы не ломать unicode
        log_line = json.dumps(payload, ensure_ascii=False)

        print(log_line, file=sys.stdout, flush=True)

    def info(self, message: str, **context):
        self._log("INFO", message, **context)

    def warning(self, message: str, **context):
        self._log("WARNING", message, **context)

    def error(self, message: str, **context):
        self._log("ERROR", message, **context)

    def debug(self, message: str, **context):
        self._log("DEBUG", message, **context)

    def critical(self, message: str, **context):
        self._log("CRITICAL", message, **context)
