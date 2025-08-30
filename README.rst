LogNGraph
=========

*A Python 3.12 package for easily drawing primitives and saving log files*

Functionality
=============

⚠️ You're entering WIP territory ⚠️

Logs
----

1. Create Logger instance:

   .. code:: python

      from logngraph.log import get_logger
      from logngraph.log.levels import *
      logger = get_logger(__name__, filename="my_log_file.txt", level=TRACE)  # Look for everything
                                                            # By default, log level is INFO

   get_logger parameters:

   - name: Name of the module/logger
   - filename: Filename of the log file
   - level: Logging level
   - file_level: Like level, but for file. If None, will be the same as level.
   - file_colors: If True, will write colorful text to the log file. (Can not be colorful in some editors)

2. Then just log!

   .. code:: python

      logger.trace("When you need to know EVERY detail")
      logger.debug("Diagnosing or troubleshooting an issue")
      logger.info("Something has happened, e.g. started a server")
      logger.warn("Something unexpected has happened,"
                  " but code will continue running")
      logger.error("App hit an issue that prevents a certain "
                   "function from working, e.g. payment system is offline"
                   "but the program can still continue running")
      logger.fatal("Something crucial has stopped working, e.g"
                   "lost connection to the main server, can't"
                   "continue running")

That's it!

You can also change the log level:

.. code:: python

   from logngraph.log.levels import *
   logger.set_level(WARNING)
   logger.set_file_level(INFO)

Here's a hierarchy of log levels:

- TRACE   - e.g. what packets client received from the server
- DEBUG   - e.g. game server froze, and you need to see why
- INFO    - e.g. someone said something in chat, and you saved it in logs
- WARNING - e.g. lost connection to the server temporarily
- ERROR   - e.g. lost connection to the server completely (timeout, etc.)
- FATAL   - e.g. client could not find models for the characters
- NONE    - e.g. you don't want logs (disabled)

Write to file happens when one of the log methods is called

Graphics
--------

1. Create a Window instance:

   .. code:: python

      from logngraph.graph import Window
      window = Window(title="Window title", width=800, height=800, resizable=True)

2. Draw primitives:

   .. code:: python

      window.fill("#000000")  # fills whole window with color
      window.rect((10, 10), (250, 50), color="#ff00ff")  # from (10, 10) with width, height (250, 50)
      window.circle((25, 20), 15)   # at (25, 20) with radius 15
      window.line((0, 0), (800, 900), color="#0000ff")  # from (0, 0) to (800, 900)
      window.polygon((750, 750), (800, 400), (35, 600), color="#ff0000")
      # Also you can display text!
      window.write(60, 150, text="Hello, World!", color="#ffffff", bg_color="#000000", antialias=True, size=32, font="Arial")
      # And, you can rotate and translate!
      window.translate(500, 100)
      # Now (0, 0) is (500, 100) for new primitives you want to draw!
      window.rotate(45)  # degrees
      # Now everything after this will be rotated 45 degrees!

3. And update the screen:

   .. code:: python

      window.update()

   Don't forget to ``window.handle_events()``!

4. You can also save the screen:

   .. code:: python

      window.screenshot("screenshot.png")

That's all!

Installation
============

Use pip:

.. code:: bash

   pip install logngraph
