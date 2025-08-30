Examples
========

Basic Logging
-------------

.. code-block:: python

   from logngraph import get_logger
   from logngraph.log.levels import DEBUG, INFO, ERROR

   logger = get_logger(__name__, level=DEBUG, filename="app.log")

   def process_data(data):
       logger.debug(f"Processing data: {data}")
       try:
           result = complex_operation(data)
           logger.info(f"Operation successful: {result}")
           return result
       except Exception as e:
           logger.error(f"Operation failed: {e}")
           return None


Simple Drawing
--------------

.. code-block:: python

   from logngraph import Window

   window = Window("Shapes Demo", 400, 400)

   # Draw a face
   window.fill("#87ceeb")  # Sky blue background
   window.circle((200, 200), 100, "#ffd700")  # Face
   window.circle((170, 170), 15, "#000000")   # Left eye
   window.circle((230, 170), 15, "#000000")   # Right eye
   window.polygon((200, 200), (180, 230), (220, 230), color="#ff0000")  # Nose

   window.update()

   # Keep window open
   while window.running:
       window.handle_events()


Key binding & Vec2D
-----------------------

.. code-block:: python

   from logngraph import Window, get_logger
   from logngraph.log.levels import INFO
   from logngraph.vector import Vec2D

   logger = get_logger(__name__, level=INFO)

   class App:
       def __init__(self):
           self.window = Window("Interactive Demo", 600, 400, resizable=True)
           self.circle_pos = Vec2D(300, 200)
           self.logger = logger

       def on_k(self):
           self.window.screenshot("verycoolscreenshot.png")
           self.circle_pos.x += 2
           self.circle_pos.x %= self.window.width  # Width changes if window is resized
           self.circle_pos = self.circle_pos.rotate(2, Vec2D(300, 200))
           self.logger.info("Saved screenshot")

       def run(self):
           self.logger.info("Starting interactive demo")
           self.window.bind_keydown("k", self.on_k)
           while self.window.running:
               self.window.fill("#2c3e50")
               self.window.circle(self.circle_pos, 30, "#e74c3c")

               # Handle events, e.g. window close or key press
               self.window.handle_events()

               self.window.update()

           self.logger.info("Demo ended")


   if __name__ == "__main__":
       app = App()
       app.run()



