class Rectangle:
  def __init__(self,x,y,h,w):
    self.x = abs(x)
    self.y = abs(y)
    self.height = abs(h)
    self.width = abs(w)
  def __str__(self):
    """
    creates a string that contains the x,y vaules and height and width
    args: x,y,h,w
    return: string
    """
    string = f"x: {self.x} y: {self.y} h: {self.h} w: {self.w}"
    return string
    