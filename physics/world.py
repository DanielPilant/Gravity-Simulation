PIXELS_PER_METER = 100  # 100 pixels = 1 meter

class EarthGravity:
    def __init__(self, g=9.81):
        self.g = g  # m/s^2

    def force(self, mass):
        return mass * self.g

    def acceleration(self):
        return self.g * PIXELS_PER_METER # in pixels/s^2
