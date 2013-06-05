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

def achaAlturaAparenteDaColuna(pontosF, listaBase):
    listaTopo = []
    i = 0
    midH = [ (pontosF[0] + pontosF[1]) * 0.5, (pontosF[2] + pontosF[3]) * 0.5 ]
    midV = [ (pontosF[1] + pontosF[2]) * 0.5, (pontosF[3] + pontosF[0]) * 0.5 ]
    i = 0
    for p in listaBase:
        difX = midH[0].x - midH[1].x
        difZ = midH[0].z - midH[1].z
        dif1 = midH[0].x - p.x
        if (i%2 == 1):
            dif2 = difZ * dif1 / float(difX)
            listaTopo.append(Ponto(p.x, p.y, midH[0].z - dif2))
        else:
            listaTopo.append(Ponto(p.x, p.y, midV[0].z))
        i += 1

    return listaTopo

def arrumaColuna(pontosR):
    meiox = (pontosR[0].x - pontosR[2].x) / 2
    meioz = (pontosR[0].z - pontosR[2].z) / 2
    meioy = pontosR[0].linearInterpolationYZ(pontosR[2], meiox)
    print "MEIOS = [%s, %s, %s]" % (meiox, meioy, meioz)
    centroDaRampa = Ponto(pontosR[0].x - meiox, pontosR[0].y - meioy, pontosR[0].z - meioz)
    print "Posicao real da rampa %s" %(pontosR)
    return centroDaRampa