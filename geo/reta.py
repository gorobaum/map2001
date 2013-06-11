import math
from geo.ponto import Ponto
from geo.vetor import Vetor
import config.config as Config

class Reta:
    def __init__(self, p1, p2):
        self.p = p1
        self.v = Vetor(p1, p2)

    def intersect(self, reta):
        if Config.debug:
            print "intersect"
        p1 = self.p
        p2 = reta.p
        v1 = self.v
        v2 = reta.v
        alpha2 = 0
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

        if v1.z != 0:
            alpha1 = (p.z - p1.z) / float(v1.z)
        elif v1.y != 0:
            alpha1 = (p.y - p1.y) / float(v1.y)
        elif v1.x != 0:
            alpha1 = (p.x - p1.x) / float(v1.x)
        else:
            raise BaseException("vetor nulo na definicao da reta?")

        pv = p1 + v1 * alpha1

        if p != pv:
            raise BaseException("as retas nao se interceptam")
        return p

