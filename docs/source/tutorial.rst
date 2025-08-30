Tutorial
========

This guide will help you get started with LogNGraph.

Quick Start
-----------

Basic logging example:

.. code-block:: python

   from logngraph import get_logger
   from logngraph.log.levels import INFO

   logger = get_logger(name, level=INFO)
   logger.info("Application started")


Basic graphics example:

.. code-block:: python

   from logngraph import Window

   window = Window(title="My App", width=800, height=600)
   window.fill("#2c3e50")
   window.rect((100, 100), (200, 150), color="#e74c3c")
   window.update()

   # Main loop
   while window.running:
       window.handle_events()


Complete Example
----------------

.. code-block:: python

   from logngraph import get_logger, Window
   from logngraph.log.levels import DEBUG, INFO

   # Setup logging
   logger = get_logger(name, filename="app.log", level=DEBUG)
   logger.info("Starting application")

   # Setup graphics
   window = Window(title="Demo", width=800, height=600, resizable=True)

   try:
       # Draw something
       window.fill("#34495e")
       window.circle((400, 300), 50, color="#f39c12")
       window.update()

       # Main loop
       while window.running:
           window.handle_events()

   except Exception as e:
       logger.error(f"Error in application: {e}")
   finally:
       logger.info("Application closed")

