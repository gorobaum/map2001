class Ponto:
    def __init__(self):
        self.x, self.y, self.z = 0, 0, 0
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, p):
        result = Ponto()
        result.x = self.x + p.x
        result.y = self.y + p.y
        result.z = self.z + p.z
        return result
