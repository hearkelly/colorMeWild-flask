import random


class Color:

    def __init__(self):
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.rgbTuple = (self.red, self.green, self.blue)

    def __str__(self):
        return '#%02x%02x%02x' % self.rgbTuple

    def __repr__(self):
        return f"({self.red}, {self.green}, {self.blue})"
