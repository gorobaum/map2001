from geo.ponto import Ponto as P
import geo.operacoes as Op
import config.size as Tamanho

class Rampa:
    def __init__(self, *args):
        if len(args) == 6:
            self.initByPoints(args[0:4], [args[4], args[4], args[5], args[5]])
        elif len(args) == 4:
            self.initByAnotherRampa(args[0], args[1], args[2], args[3])

    def initByPoints(self, points, alturasreais):
        self.pontosF = points
        self.pontosR = Op.entortaRampaPorZ(points, alturasreais)

    def initByAnotherRampa(self, rampa, comprimentoRampa, difZF, difZR):
        pontosR = []
        pontosR.append(rampa.pontosR[-1] - P(0, 0, 2))
        pontosR.append(rampa.pontosR[-2] - P(0, 0, 2))
        pontosF = []
        pontosF.append(Op.novoPontoPorY(pontosR[0], rampa.pontosF[-1].y))
        pontosF.append(Op.novoPontoPorY(pontosR[1], rampa.pontosF[-2].y))

        pontosF.append(pontosF[1] + P(comprimentoRampa, 0, difZF))
        pontosF.append(pontosF[0] + P(comprimentoRampa, 0, difZF))

        pontosR.append(Op.novoPontoPorZ(pontosF[-2], pontosR[0].z + difZR))
        pontosR.append(Op.novoPontoPorZ(pontosF[-1], pontosR[1].z + difZR))

        self.pontosR = pontosR
        self.pontosF = pontosF
