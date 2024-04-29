class Button:
    def __init__(self, width, height, x, y, name):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.name = name

    def pressed(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
