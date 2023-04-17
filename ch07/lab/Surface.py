from Rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        self.image = filename
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.rect = Rectangle(x,y,h,w)

    def getRect(self):
        """
        return rectangle attribute
        args: self
        return: Rectangle 
        """
        return self.rect