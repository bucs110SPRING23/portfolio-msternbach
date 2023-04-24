
class Mysterybox:
  def __init__(self, item):
    """
    Initialize the mysterybox
    args: item - what item mystery box drops
    """
    self.item = item
    self.is_open = False
    self.itemnum = 1

class Goomba:
  def __init__(self, x):
    """
    Initialize the enemy object
    """
    self.is_touched = False
    self.position = x 
    self.is_moving = False

class Player:
  def __init__(self, direction,speed,jump):
    """
    Initialize the player object
    args: direction, speed, jump
    """
    self.direction = direction
    self.speed = speed
    self.jump = jump