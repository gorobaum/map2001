from ponto import Ponto
from math import sqrt

class Vetor(Ponto):
    def __init__(self, *args):
        if len(args) == 2:
            self.macaco(args[0], args[1])
        else:
            self.gordo(args[0], args[1], args[2])

    def macaco(self, orig, dest):
        self.x = dest.x - orig.x
        self.y = dest.y - orig.y
        self.z = dest.z - orig.z

    def gordo(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def length(self):
        return sqrt(self.x ** 2 + self.y **2 + self.z ** 2)

    def normalize(self):
        l = self.length()
        return Vetor(self.x / l, self.y / l, self.z / l)
