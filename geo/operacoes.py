from geo.ponto import Ponto
from geo.vetor import Vetor
from config.observador import Observador
import math

def descobreNovoPonto(base, alturaReal, alturaFicticia):
    p = Ponto(base.x, base.y, alturaFicticia)
    r = Ponto(base.x, base.y, alturaReal)
    v = Vetor(Observador.posicao, p)
    razao = float(r.z - p.z) / v.z
    novoV = v * razao
    novoPonto = p + novoV
    return novoPonto

def entortaRampa(listaPontosAparentes, listaAlturasReais):
    i = 0
    retL = []
    for p in listaPontosAparentes:
        v = Vetor(Observador.posicao, p)
        print v
        alt = listaAlturasReais[i]
        i += 1
        razao = float(alt - p.z) / v.z
        novoV = v * razao
        novoPonto = p + novoV
        retL.append(novoPonto)
    return retL

def anguloEntre(base, topo, p3):
    c = base.dist(topo)
    b = base.dist(p3)
    a = topo.dist(p3)

    frac = (b ** 2 + c**2 - a**2) / (2*b*c)
    return math.acos(frac)
