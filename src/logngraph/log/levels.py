"""
Logging level constants for the LogNGraph package.

This module defines standard logging levels used throughout the LogNGraph package.
The levels follow a hierarchical structure where lower numerical values indicate
more verbose logging.

Constants:
    | TRACE (int): Level 0 - Most detailed information for tracing program execution.
    | DEBUG (int): Level 1 - Diagnostic information useful for debugging.
    | INFO (int): Level 2 - General information about program execution.
    | WARNING (int): Level 3 - Indicates potential issues that don't prevent execution.
    | ERROR (int): Level 4 - Errors that affect functionality but allow continued operation.
    | FATAL (int): Level 5 - Critical errors that prevent further operation.
    | NONE (int): Level 6 - Special value to disable all logging.

Example:
    >>> from logngraph.log import get_logger
    >>> from logngraph.log.levels import INFO, DEBUG
    >>> logger = get_logger(__name__, level=DEBUG)
    >>> logger.set_level(INFO)

Note:
    These levels follow the standard syslog severity levels with the addition of
    TRACE for ultra-verbose logging and NONE for disabling logs.
"""

__all__ = [
    "TRACE",
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "FATAL",
    "NONE",
]

TRACE = 0
"""int: Level 0 - Most detailed information for tracing program execution."""

DEBUG = 1
"""int: Level 1 - Diagnostic information useful for debugging."""

INFO = 2
"""int: Level 2 - General information about program execution."""

WARNING = 3
"""int: Level 3 - Indicates potential issues that don't prevent execution."""

ERROR = 4
"""int: Level 4 - Errors that affect functionality but allow continued operation."""

FATAL = 5
"""int: Level 5 - Critical errors that prevent further operation."""

NONE = 6
"""int: Level 6 - Special value to disable all logging."""
