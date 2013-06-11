from geo.ponto import Ponto
from geo.reta import Reta
from modelo.base import Base
from modelo.rampa import Rampa
from modelo.plano import Plano
import geo.operacoes as Operacoes
import config.size as Tamanho
from config.observador import Observador
import math

p1 = Ponto(1, 1, 1)
p2 = Ponto(3, 1, 1)
p3 = Ponto(1, 3, 1)

plano = Plano(p1, p2, p3)

pr1 = Ponto(2, 2, 2)
pr2 = Ponto(2, 2, -2)

r = Reta(pr1, pr2)

print "", plano.intersecReta(r)