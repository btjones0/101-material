# When defining new types, we'll typically start off with a capital
# letter.
class Point:
   """A class to model a 2D point.

   Attributes: x and y"""

   def __init__(self, x, y): # This is where the magic happens!
      self.x = x
      self.y = y
