import math

class Ponto:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, p):
        return Ponto(self.x + p.x, self.y + p.y, self.z + p.z)

    def __sub__(self, p):
        return Ponto(self.x - p.x, self.y - p.y, self.z - p.z)

    def __mul__(self, scalar):
        return Ponto(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __div__(self, scalar):
        val = 1.0 / scalar
        return self.__mul__(val)

    def __repr__(self):
        return "(" + ("%.2f" % self.x) + ", " + ("%.2f" % self.y) + ", " + ("%.2f" % self.z) + ")"

    def __str__(self):
        return self.__repr__()

    def dist(self, p):
        return float(math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2))

    def linearInterpolationXZ(self, p, x):
        razao = (p.z - self.z ) / (p.x - self.x)
        return (x - self.x)*razao + self.z

    def linearInterpolationXY(self, p, y):
        razao = (p.z - self.z ) / (p.y - self.y)
        return (y - self.y)*razao + self.z    
