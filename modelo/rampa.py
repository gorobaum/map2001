from geo.ponto import Ponto as P
import config.size as Tamanho

class Rampa:
    def __init__(self, *args):
        if len(args) == 4:
            self.initByPoints(args[0:4])
        elif len(args) == 3:
            self.initAux(args[0], args[1], args[2])

    def initByPoints(self, points):
        self.pontosAparencia = points

    def initAux(self, p1, p2, larg):
        lista = []
        lista.append(p1)
        lista.append(p1 + P(0, larg, 0))
        lista.append(p2 + P(0, larg, 0))
        lista.append(p2)
        self.initByPoints(lista)

    def setPontosReal(self, listap):
        self.pontosReal = listap
