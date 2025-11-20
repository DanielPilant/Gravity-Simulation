PIXELS_PER_METER = 100  # 100 pixels = 1 meter

class StoneFloorFriction:
    def __init__(self, mu=0.6):
        self.mu = mu  # coefficient of friction

    def friction_acceleration(self, g):
        friction_force = self.mu * g  
        return friction_force * PIXELS_PER_METER  # in pixels/s^2

class OilFloorFriction:
    def __init__(self, mu=0.1):
        self.mu = mu  # coefficient of friction

    def friction_acceleration(self, g):
        friction_force = self.mu * g  
        return friction_force * PIXELS_PER_METER  # in pixels/s^2

class EarthGravity:
    def __init__(self, g=9.81):
        self.g = g  # m/s^2

    def force(self, mass):
        return mass * self.g

    def acceleration(self):
        return self.g * PIXELS_PER_METER # in pixels/s^2
    
    def stone(self):
        stone_friction = StoneFloorFriction()
        g = self.g
        return stone_friction.friction_acceleration(g)

    def oil(self):
        oil_friction = OilFloorFriction()
        g = self.g
        return oil_friction.friction_acceleration(g)
    
class MoonGravity:
    def __init__(self, g=1.62):
        self.g = g  # m/s^2

    def force(self, mass):
        return mass * self.g

    def acceleration(self):
        return self.g * PIXELS_PER_METER # in pixels/s^2
    
    
class sunGravity:
    def __init__(self, g=274):
        self.g = g  # m/s^2

    def force(self, mass):
        return mass * self.g

    def acceleration(self):
        return self.g * PIXELS_PER_METER # in pixels/s^2