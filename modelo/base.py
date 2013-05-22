from geo.ponto import Ponto as P
import config.size as Tamanho

class Base:
    def __init__(self, *args):
        if len(args) == 6:
            self.initByPoints(args[0:4])
        elif len(args) == 3:
            self.initByCenter(args[0])
        self.h = args[-2]
        self.a = args[-1]

    def initByPoints(self, points):
        self.pontos = points

    def initByCenter(self, center):
        self.initCenterAux(center, Tamanho.coluna/2)

    def initCenterAux(self, center, larg):
        lista = []
        lista.append(center + P(0, -larg, 0))
        lista.append(center + P(-larg, 0, 0))
        lista.append(center + P(0, larg, 0))
        lista.append(center + P(larg, 0, 0))
        self.initByPoints(lista)
