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

def entortaRampaPorZ(listaPontosAparentes, listaAlturasReais):
    i = 0
    retL = []
    for p in listaPontosAparentes:
        v = Vetor(Observador.posicao, p)
        alt = listaAlturasReais[i]
        i += 1
        razao = float(alt - p.z) / v.z
        novoV = v * razao
        novoPonto = p + novoV
        retL.append(novoPonto)
    return retL

def entortaRampaPorY(listaPontosAparentes, listaYReais):
    i = 0
    retL = []
    for p in listaPontosAparentes:
        v = Vetor(Observador.posicao, p)
        y = listaYReais[i]
        i += 1
        razao = float(y - p.y) / v.y
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

def alturaDasBases(tamBase, listaAlturasReais):
    m = 0;
    if (listaAlturasReais[0] == listaAlturasReais[2]):
        return listaAlturasReais[0]
    elif (listaAlturasReais[0] < listaAlturasReais[2]):
        m = 1
    else:
        m = -1
    tamLadoBase = tamBase/2
    tamLadoRampa = m*(listaAlturasReais[2] - listaAlturasReais[0])
    posicoes = []
    posicoes.append(tamLadoRampa/2 - tamLadoBase)
    posicoes.append(tamLadoRampa/2 + tamLadoBase)
    alturaRealDoTopoDaBase = []
    alturaRealDoTopoDaBase.append(posicoes[0]*100/tamLadoRampa)
    alturaRealDoTopoDaBase.append(posicoes[1]*100/tamLadoRampa)
    return alturaRealDoTopoDaBase