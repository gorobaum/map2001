from geo.ponto import Ponto
from modelo.base import Base
import geo.operacoes as Operacoes

bases = []
bases.append(Base(Ponto(-25, 15, 0), 20, 30))
bases.append(Base(Ponto(0, 15, 0), 30, 55))
bases.append(Base(Ponto(30, 15, 0), 25, 35))
bases.append(Base(Ponto(50, 15, 0), 19, 21))

for b in bases:
    print "Proxima Base..."
    for p in b.pontos:
        print ("  %s" % p)
        print ("   %s" % Operacoes.descobreNovoPonto(p, b.h, b.a))
