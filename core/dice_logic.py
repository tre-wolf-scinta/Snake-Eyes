# core/dice_logic
import random

class Dice:

  def __init__(self, sides: int):
    if not isinstance(sides, int) or isinstance(sides, bool):
      raise TypeError(f"Sides must be a non-boolean integer. Received {type(sides).__name__}")
    if sides <= 1:
      raise ValueError("Number of sides cannot be less than 2")

    self.sides = sides

  def roll(self)->:
    return random.randint(1, self.sides)
    
  def __str__(self):
    return f"D{self.sides}"