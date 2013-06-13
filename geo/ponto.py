import math
import config.config as Config

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

    def __cmp__(self, p):
        difx = self.x - p.x
        if difx > Config.epsilon:
            print "returning x", difx
            return difx
        dify = self.y - p.y
        if dify > Config.epsilon:
            print "returning y", dify
            return dify
        difz = self.z - p.z
        if difz > Config.epsilon:
            print "returning z", difz
            return difz
        return 0

    def __repr__(self):
        return "[" + ("%.2f" % self.x) + ", " + ("%.2f" % self.y) + ", " + ("%.2f" % self.z) + "]"

    def __str__(self):
        return self.__repr__()

    def dist(self, p):
        return float(math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2 + (self.z - p.z) ** 2))

    def linearInterpolationXZ(self, p, x):
        razao = (p.z - self.z ) / (p.x - self.x)
        return (x - self.x)*razao + self.z

    def linearInterpolationYZ(self, p, x):
        razao = (x - self.x) / (p.x - self.x)
        return (p.y - self.y)*razao + self.y 

    def get(self, xyz):
        if xyz == "x":
            return self.x
        if xyz == "y":
            return self.y
        if xyz == "z":
            return self.z
        return None
