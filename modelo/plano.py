import math
from geo.ponto import Ponto
from geo.vetor import Vetor
import config.config as Config
import geo.operacoes as Operacoes

class Plano:
    def __init__(self, p1, p2, p3):
        self.p = p1
        self.v1 = Vetor(p1, p2)
        self.v2 = Vetor(p1, p3)

    def intersectReta(self, r):
        if Config.debug:
            print "intersect plano e reta"
            print self.v1, self.v2, r.v

        if Operacoes.determinante(self.v1, self.v2, r.v) == 0:
            raise BasicException("plano e reta sao paralelos")
        
        vp1 = self.v1
        vp2 = self.v2
        vr = r.v
        pp = self.p
        pr = r.p


        interrog = None
        for coord in ['x', 'y', 'z']:
            if vp1.get(coord) != 0:
                interrog = coord
                break
        vp1o = vp1 / vp1.get(interrog)

        vr_interrog = vr.get(interrog)
        pr_interrog = pr.get(interrog)

        z = vp2 - vp1o * vp2.get(interrog)
        # z eh diferente de zero em uma coordenada pelo menos pq os vetores
        # sao l.i.
        estrela = None
        for coord in ['x', 'y', 'z']:
            if z.get(coord) != 0:
                estrela = coord
                break
        j = z / z.get(estrela)        
        vr_estrela = vr.get(estrela)
        pr_estrela = pr.get(estrela)
        pp_estrela = pp.get(estrela)
        vp1o_estrela = vp1o.get(estrela)
        
        g = j * vr_estrela - j * vr_interrog * vp1o_estrela - vr + vp1o * vr_interrog
        
        acabate = None
        for coord in ['x', 'y', 'z']:
            if g.get(coord) != 0:
                abacate = coord
                break

        aux1 = (pr + pp - vp1o * pr_interrog - j * pr_estrela - j * pp_estrela - j * pr_interrog * vp1o_estrela)
        alpha3 = aux1.get(abacate) / g.get(abacate)

        novop = r.p + r.v * alpha3
        return novop






