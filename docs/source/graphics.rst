Graphics
========

LogNGraph provides a simple interface for drawing primitives using Pygame.

Creating a Window
-----------------

.. code-block:: python

   from logngraph.graph import Window

   # Basic window
   window = Window(title="My Window", width=800, height=600)

   # Advanced window
   window = Window(
       title="My Window",
       width=800,
       height=600,
       resizable=True,
       fullscreen=False,
       vsync=True
   )

Drawing Primitives
------------------

Shapes
~~~~~~

.. code-block:: python

   # Rectangle
   window.rect((x, y), (width, height), color="#ff0000", width=0)

   # Circle
   window.circle((center_x, center_y), radius, color="#00ff00", width=0)

   # Line
   window.line((start_x, start_y), (end_x, end_y), color="#0000ff", width=1)

   # Polygon
   window.polygon((x1, y1), (x2, y2), (x3, y3), color="#ffff00", width=0)

Text
~~~~

.. code-block:: python

   window.write(
       x, y,
       text="Hello World",
       color="#ffffff",
       bg_color=None,  # Transparent background
       antialias=True,
       size=24,
       font="Arial"
   )

Transformations
---------------

.. code-block:: python

   # Translation
   window.translate(dx, dy)  # Move origin

   # Rotation
   window.rotate(angle)      # Rotate around current origin

   # Scaling
   window.scale(sx, sy)      # Scale coordinates

   # Reset transformations
   window.reset_transform()

Window Management
-----------------

.. code-block:: python

   # Update display
   window.update()

   # Handle events (returns False when window should close)
   running = window.handle_events()

   # Screenshot
   window.screenshot("screenshot.png")

   # Get window size
   width, height = window.get_size()

   # Set window title
   window.set_title("New Title")

Color System
------------

LogNGraph supports multiple color formats:

- Hex strings: "#ff0000", "#f00"
- Color names: "red", "blue", "green"

Basically what PyGame supports.
