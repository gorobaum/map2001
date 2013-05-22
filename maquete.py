from geo.ponto import Ponto
from modelo.base import Base
from modelo.rampa import Rampa
import geo.operacoes as Operacoes
import config.size as Tamanho
import math

ycomum = 10
av1 = 16 * Tamanho.coluna
av2 = 10 * Tamanho.coluna
av3 = 8 * Tamanho.coluna
av4 = 6 * Tamanho.coluna
am1 = 13 * Tamanho.coluna
am2 = 9 * Tamanho.coluna
am3 = 7.5 * Tamanho.coluna
am4 = 6 * Tamanho.coluna

bases = []
bases.append(Base(Ponto(-7.5 * Tamanho.coluna, ycomum, 0), av1, am1))
bases.append(Base(Ponto(-2.5 * Tamanho.coluna, ycomum, 0), av2, am2))
bases.append(Base(Ponto(2.5 * Tamanho.coluna, ycomum, 0), av3, am3))
bases.append(Base(Ponto(7.5 * Tamanho.coluna, ycomum, 0), av4, am4))

for b in bases:
    print "Proxima Base..."
    pTopos = []
    for p in b.pontos:
        topo = Operacoes.descobreNovoPonto(p, b.h, b.a)
        pTopos.append(topo)
        tam = p.dist(topo)
        print ("  %s\t%s\tsize: %s" % (p, topo, tam))
    b.topos = pTopos
    print "angulos da base, com o anterior"
    for i in range(4):
        print math.degrees(Operacoes.anguloEntre(b.pontos[i], b.topos[i], b.pontos[i-1]))

    print "angulos da base, com o proximo"
    for i in range(4):
        print math.degrees(Operacoes.anguloEntre(b.pontos[i], b.topos[i], b.pontos[i-3]))
    print b.pontos[1].dist(b.pontos[2])


