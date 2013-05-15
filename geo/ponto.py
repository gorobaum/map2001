class Ponto:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, p):
        return Ponto(self.x + p.x, self.y + p.y, self.z + p.z)

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __str__(self):
        return self.__repr__()
