PIXELS_PER_METER = 100  # 100 pixels = 1 meter

class FloorFriction:
    def __init__(self, mu):
        self.mu = mu  # coefficient of friction

    def friction_acceleration(self, g):
        friction_force = self.mu * g  
        return friction_force * PIXELS_PER_METER  # in pixels/s^2
    
    def stone(self, g):
        return self.friction_acceleration(g)
    
    def oil(self, g):
        return self.friction_acceleration(g)
    
    def ice(self, g):
        return self.friction_acceleration(g)
    
    
class EarthGravity:
    def __init__(self, g=9.81):
        self.g = g  # m/s^2
        self.acceleration = self.g * PIXELS_PER_METER # in pixels/s^2
    
    def force(self, mass):
        return mass * self.g
    
    def stone(self):
        floorFriction = FloorFriction(mu=0.6)
        return floorFriction.stone(self.g)
    
    def oil(self): 
        floorFriction = FloorFriction(mu=0.1)
        return floorFriction.oil(self.g)
    
    def ice(self):
        floorFriction = FloorFriction(mu=0.03)
        return floorFriction.ice(self.g)
        
class MoonGravity:
    def __init__(self, g=1.62):
        self.g = g  # m/s^2
        self.acceleration = self.g * PIXELS_PER_METER # in pixels/s^2

    def force(self, mass):
        return mass * self.g
    
    def stone(self):
        floorFriction = FloorFriction(mu=0.6)
        return floorFriction.stone(self.g)
    
    def oil(self): 
        floorFriction = FloorFriction(mu=0.1)
        return floorFriction.oil(self.g)
    
    def ice(self):
        floorFriction = FloorFriction(mu=0.03)
        return floorFriction.ice(self.g)
    
    
class SunGravity:
    def __init__(self, g=274):
        self.g = g  # m/s^2
        self.acceleration = self.g * PIXELS_PER_METER # in pixels/s^2

    def force(self, mass):
        return mass * self.g
    
    def stone(self):
        floorFriction = FloorFriction(mu=0.6)
        return floorFriction.stone(self.g)
    
    def oil(self): 
        floorFriction = FloorFriction(mu=0.1)
        return floorFriction.oil(self.g)
    
    def ice(self):
        floorFriction = FloorFriction(mu=0.03)
        return floorFriction.ice(self.g)