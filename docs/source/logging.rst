Logging
=======

LogNGraph provides a comprehensive logging system with multiple levels and file output.

Creating a Logger
-----------------

.. code-block:: python

   from logngraph.log import get_logger
   from logngraph.log.levels import *

   # Basic logger
   logger = get_logger(__name__)

   # Advanced logger with file output
   logger = get_logger(
       __name__,
       filename="app.log",
       level=DEBUG,
       file_level=INFO,
       file_colors=True
   )

Log Levels
----------

LogNGraph supports these log levels (from most to least verbose):

- TRACE: For extremely detailed debugging information
- DEBUG: For diagnostic information useful for troubleshooting
- INFO: For general information about application progress
- WARN: For unexpected but non-critical issues
- ERROR: For errors that affect functionality but allow continued operation
- FATAL: For critical errors that prevent further operation
- NONE: Disable logging

Logging Methods
---------------

.. code-block:: python

   logger.trace("Detailed trace information")
   logger.debug("Debug information")
   logger.info("Informational message")
   logger.warn("Warning message")
   logger.error("Error message")
   logger.fatal("Fatal error message")

Configuration
-------------

You can change log levels dynamically:

.. code-block:: python

   logger.set_level(INFO)          # Change console level
   logger.set_file_level(DEBUG)    # Change file level

Advanced Features
-----------------

- Colored output in terminals and files (where supported)
- Multiple loggers with different settings
