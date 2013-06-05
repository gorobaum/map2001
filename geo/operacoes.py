from __future__ import division
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

def novoPontoPorX(ponto, x):
    v = Vetor(Observador.posicao, ponto)
    razao = float(x - ponto.x) / v.x
    novoV = v * razao
    novoPonto = ponto + novoV
    return novoPonto

def novoPontoPorY(ponto, y):
    v = Vetor(Observador.posicao, ponto)
    razao = float(y - ponto.y) / v.y
    novoV = v * razao
    novoPonto = ponto + novoV
    return novoPonto

def novoPontoPorZ(ponto, z):
    v = Vetor(Observador.posicao, ponto)
    razao = float(z - ponto.z) / v.z
    novoV = v * razao
    novoPonto = ponto + novoV
    return novoPonto

def entortaRampaPorZ(listaPontosAparentes, listaAlturasReais):
    i = 0
    retL = []
    for p in listaPontosAparentes:
        novoPonto = novoPontoPorZ(p, listaAlturasReais[i])
        i += 1
        retL.append(novoPonto)
    return retL

def anguloEntre(base, topo, p3):
    c = base.dist(topo)
    b = base.dist(p3)
    a = topo.dist(p3)

    frac = (b ** 2 + c**2 - a**2) / (2*b*c)
    return math.acos(frac)

def achaBaseDaColuna(listaPontosAparentes, tamBase):
    meiox = (listaPontosAparentes[3].x - listaPontosAparentes[0].x)/2
    meioy = (listaPontosAparentes[1].y - listaPontosAparentes[0].y) / 2
    distCentroBase = tamBase/2
    centroDaRampa = Ponto(listaPontosAparentes[0].x + meiox, listaPontosAparentes[0].y + meioy, 0)
    pontosDaBase = []
    pontosDaBase.append(Ponto(centroDaRampa.x - distCentroBase, centroDaRampa.y - distCentroBase, 0))
    pontosDaBase.append(Ponto(centroDaRampa.x - distCentroBase, centroDaRampa.y + distCentroBase, 0))
    pontosDaBase.append(Ponto(centroDaRampa.x + distCentroBase, centroDaRampa.y + distCentroBase, 0))
    pontosDaBase.append(Ponto(centroDaRampa.x + distCentroBase, centroDaRampa.y - distCentroBase, 0))
    return pontosDaBase

def achaAlturaAparenteDaColuna(listaPontosAparentes, listaBase):
    listaTopo = []
    i = 0
    for p in listaBase:
        alturaTopo = listaPontosAparentes[i%2].linearInterpolationYZ(listaPontosAparentes[i%2+2], p.y)
        listaTopo.append(Ponto(p.x, p.y, alturaTopo))
        i += 1

    return listaTopo

def arrumaColuna(listaPontosAparentes, razao):
    i = 0
    retL = []
    for p in listaPontosAparentes:
        v = Vetor(Observador.posicao, p)
        print "RAZAO = %s" % razao
        novoV = v * razao
        novoPonto = p + v
        retL.append(novoPonto)
    return retL
