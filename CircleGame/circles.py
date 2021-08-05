import math

class Circle:
    position = (0, 0)
    radius = 50
    color = (255, 255, 255)
    max_speed = 30

    def __init__(self, position=(0, 0), radius=10, color=(255, 255, 255), max_speed=10):
        self.position = position
        self.radius = radius
        self.color = color
        self.max_speed = max_speed

    def move_by(self, x_axis, y_axis):
        self.position = (self.position[0] + x_axis*self.max_speed, self.position[1] + y_axis*self.max_speed)

    def collides(self, other):
        if math.sqrt((other.position[0] - self.position[0])**2 + (other.position[1] - self.position[1])**2) \
                < (self.radius + other.radius):
            return True
        return False

    def withing_range(self, other, multiplier=2):
        """Returns true if is withing range of radius of another circle multiplied by a multiplier"""
        if math.sqrt((other.position[0] - self.position[0])**2 + (other.position[1] - self.position[1])**2) \
                < (self.radius + other.radius*multiplier):
            return True
        return False