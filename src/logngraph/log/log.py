from logngraph.log.levels import *
from datetime import datetime
import sys
import re
import threading

__all__ = [
    "get_logger",
    "Logger",
]

_loggers = {}
_lock = threading.Lock()


def _remove_ansi_escape_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def get_logger(name: str, filename: str = None, level: int = INFO, file_level: int | None = None,
               file_colors: bool = False) -> "Logger":
    """
    Get or create a named logger instance.

    :param name: Name of the logger
    :param filename: Filename of the log file (optional)
    :param level: Logging level (can be changed using Logger.set_level)
    :param file_colors: Write colors to file
    :param file_level: If not None, must be level. Level for file. If None, file_level is the same as level.

    :returns: Logger instance
    """

    with _lock:
        if name not in _loggers:
            _loggers[name] = Logger(name, filename, level, file_colors, file_level)
        return _loggers[name]


class Logger:
    _file_handles = {}
    _file_locks = {}
    _stdout_lock = threading.Lock()

    def __init__(self, name: str, filename: str = None, level: int = INFO, file_colors: bool = False,
                 file_level: int | None = None) -> None:
        """
        Logger class. Use get_logger to get or create a named logger instance.
        """

        self.name = name
        self.filename = filename
        self.file = open(filename, "w") if filename else None
        self.stdout = sys.stdout
        self.level = level
        self.file_level = file_level

        self.fc = file_colors

        if filename:
            if filename not in Logger._file_handles:
                f = open(filename, 'a')
                Logger._file_handles[filename] = f
                Logger._file_locks[filename] = threading.Lock()

    @property
    def dtstr(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f")[:-3]

    def set_level(self, level: int) -> bool:
        if 0 <= level <= 6:
            self.level = level
            return True
        return False

    def set_file_level(self, level: int | None) -> bool:
        if 0 <= level <= 6 or not level:
            self.file_level = level
            return True
        return False

    def print(self, text: str, level: int) -> None:
        if self.filename:
            if (self.file_level and self.file_level <= level) or not self.file_level:
                with Logger._file_locks[self.filename]:
                    if self.fc:
                        Logger._file_handles[self.filename].write(text)
                    else:
                        Logger._file_handles[self.filename].write(_remove_ansi_escape_codes(text))
                    Logger._file_handles[self.filename].flush()

        if self.level <= level:
            with Logger._stdout_lock:
                self.stdout.write(text)
                self.stdout.flush()

    def trace(self, msg: str) -> None:
        if self.file_level or self.level <= TRACE:
            log = f"\x1b[38;5;123mTRACE: {self.dtstr}: [{self.name}]: {msg}\x1b[0m\n"
            self.print(log, TRACE)

    def debug(self, msg: str) -> None:
        if self.file_level or self.level <= DEBUG:
            log = f"\x1b[38;5;11mDEBUG: {self.dtstr}: [{self.name}]: {msg}\x1b[0m\n"
            self.print(log, DEBUG)

    def info(self, msg: str) -> None:
        if self.file_level or self.level <= INFO:
            log = f"\x1b[38;5;251mINFO:  {self.dtstr}: [{self.name}]: {msg}\x1b[0m\n"
            self.print(log, INFO)

    def warn(self, msg: str) -> None:
        if self.file_level or self.level <= WARNING:
            log = f"\x1b[38;5;208m\x1b[1mWARN:  {self.dtstr}: [{self.name}]: {msg}\x1b[0m\n"
            self.print(log, WARNING)

    def error(self, msg: str) -> None:
        if self.file_level or self.level <= ERROR:
            log = f"\x1b[38;5;196m\x1b[1mERROR: {self.dtstr}: [{self.name}]: {msg}\x1b[0m\n"
            self.print(log, ERROR)

    def fatal(self, msg: str) -> None:
        if self.file_level or self.level <= FATAL:
            log = f"\x1b[38;5;124m\x1b[1mFATAL: {self.dtstr}: [{self.name}]: {msg}\x1b[0m\n"
            self.print(log, FATAL)

    def close(self) -> None:
        """Close the file handle if this is the last logger using it"""
        if self.filename:
            with _lock:
                # Count how many loggers are using this file
                users = sum(1 for logger in _loggers.values()
                            if logger.filename == self.filename)

                if users <= 1:
                    if self.filename in Logger._file_handles:
                        Logger._file_handles[self.filename].close()
                        del Logger._file_handles[self.filename]
                        del Logger._file_locks[self.filename]

    def __del__(self) -> None:
        self.close()


if __name__ == "__main__":
    # Testing field
    logger = Logger(__name__, "test.log", TRACE)
    logger.trace("trace")
    logger.debug("debug")
    logger.info("info")
    logger.warn("warn")
    logger.error("error")
    logger.fatal("fatal")
