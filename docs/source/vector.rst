Vec2D Class
===========

The ``Vec2D`` class provides mathematical vector operations.

Operation Examples
------------------

Addition
~~~~~~~~

.. code-block:: python

   v1 = Vec2D(1, 2)
   v2 = Vec2D(3, 4)
   result = v1 + v2  # Vector(4, 6)

Subtraction
~~~~~~~~~~~

.. code-block:: python

   v1 = Vec2D(5, 3)
   v2 = Vec2D(2, 1)
   result = v1 - v2  # Vector(3, 2)

Multiplication
~~~~~~~~~~~~~~

.. code-block:: python

   # Scalar multiplication
   v = Vec2D(2, 3)
   result = v * 3  # Vector(6, 9)

   # Dot product
   v1 = Vec2D(1, 2)
   v2 = Vec2D(3, 4)
   result = v1 * v2  # 11 (1*3 + 2*4)

   # Cross product
   v1 = Vec2D(1, 2)
   v2 = Vec2D(3, 4)
   result = v1.cross(v2)  # 7 (4 * 1 + 2 * 3)

Division
~~~~~~~~

.. code-block:: python

   v = Vec2D(6, 9)
   result = v / 3  # Vector(2, 3)

Comparison
~~~~~~~~~~

.. code-block:: python

   v1 = Vec2D(1, 2)
   v2 = Vec2D(1, 2)
   v3 = Vec2D(3, 4)
   v1 == v2  # True
   v1 == v3  # False

Indexing
~~~~~~~~

.. code-block:: python

   v = Vec2D(7, 8)
   x = v[0]  # 7
   y = v[1]  # 8

Iteration
~~~~~~~~~

.. code-block:: python

   v = Vec2D(3, 4)
   for component in v:
       print(component)  # Prints 3, then 4

String Representation
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   v = Vector(2, 5)
   print(v)        # Uses __str__: "(2; 5)"
   repr(v)         # Uses __repr__: "Vec2D(2; 5)"

