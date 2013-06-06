from __future__ import division
from geo.ponto import Ponto
from geo.vetor import Vetor
from geo.reta import Reta
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
    pontosDaBase.append(Ponto(centroDaRampa.x - distCentroBase, centroDaRampa.y, 0))
    pontosDaBase.append(Ponto(centroDaRampa.x, centroDaRampa.y + distCentroBase, 0))
    pontosDaBase.append(Ponto(centroDaRampa.x + distCentroBase, centroDaRampa.y, 0))
    pontosDaBase.append(Ponto(centroDaRampa.x, centroDaRampa.y - distCentroBase, 0))
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

def topoRealColuna(topoAparente, rampa):
    f_esqd = (rampa.pontosF[0] + rampa.pontosF[1]) * 0.5
    f_dirt = (rampa.pontosF[2] + rampa.pontosF[3]) * 0.5
    f_cima = (rampa.pontosF[1] + rampa.pontosF[2]) * 0.5
    f_baxo = (rampa.pontosF[3] + rampa.pontosF[0]) * 0.5

    reta_fe = Reta(Observador.posicao, f_esqd)
    reta_fd = Reta(Observador.posicao, f_dirt)
    reta_fc = Reta(Observador.posicao, f_cima)
    reta_fb = Reta(Observador.posicao, f_baxo)

    lado_e = Reta(rampa.pontosR[0], rampa.pontosR[1])
    lado_d = Reta(rampa.pontosR[2], rampa.pontosR[3])
    lado_c = Reta(rampa.pontosR[1], rampa.pontosR[2])
    lado_b = Reta(rampa.pontosR[3], rampa.pontosR[0])

    esqd = reta_fe.intersect(lado_e)
    dirt = reta_fd.intersect(lado_d)
    cima = reta_fc.intersect(lado_c)
    baxo = reta_fb.intersect(lado_b)

    print "esq, dir, cima, baixo"
    print esqd, dirt, cima, baxo

    
    retaH = Reta(esqd, dirt)
    retaV = Reta(cima, baxo)

    pontosRetorno = []
    for i in range(4):
        pTopo = topoAparente[i]
        retaO = Reta(Observador.posicao, pTopo)
        p = Ponto(0, 0, 0)
        if i % 2 == 0:
            p = retaO.intersect(retaH)
        else:
            p = retaO.intersect(retaV)
        pontosRetorno.append(p)
    return pontosRetorno
