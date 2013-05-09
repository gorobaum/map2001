import ponto

class Vetor(Ponto):
    def __init__(self, orig, dest):
        self.x = dest.x - orig.x
        self.y = dest.y - orig.y
        self.z = dest.z - orig.z
