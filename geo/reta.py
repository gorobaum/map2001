import math
from geo.ponto import Ponto
from geo.vetor import Vetor

class Reta:
    def __init__(self, p1, p2):
        self.p = p1
        self.v = Vetor(p1, p2)

    def intersectZ(self, reta):
        p1 = self.p
        p2 = reta.p
        v1 = self.v
        v2 = reta.v
        print p1, p2, v1, v2
        aux0 = (p2.z - p1.z) / float(v1.z)
        aux1 = (p2.y - p1.y) / float(v1.y) - aux0
        aux2 = v2.z / float(v1.z) - v2.y / float(v1.y)
        alpha2 = aux1 / float(aux2)

        p = p2 + v2 * alpha2
        print p
        return p
    
    def intersect(self, reta):
        p1 = self.p
        p2 = reta.p
        v1 = self.v
        v2 = reta.v
        alpha2 = 0
        print p1, p2, v1, v2
        if v1.x != 0:
            aux0 = (p2.x - p1.x) / float(v1.x)
            aux1 = (p2.y - p1.y) / float(v1.y) - aux0
            aux2 = v2.x / float(v1.x) - v2.y / float(v1.y)
            alpha2 = aux1 / float(aux2)
        else:
            aux0 = (p2.z - p1.z) / float(v1.z)
            aux1 = (p2.y - p1.y) / float(v1.y) - aux0
            aux2 = v2.z / float(v1.z) - v2.y / float(v1.y)
            alpha2 = aux1 / float(aux2)


        p = p2 + v2 * alpha2
        print p
        return p
