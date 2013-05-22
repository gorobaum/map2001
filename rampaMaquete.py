from geo.ponto import Ponto
from modelo.base import Base
from modelo.rampa import Rampa
import geo.operacoes as Operacoes
import config.size as Tamanho
import math

ycomum = 10
rLarg = 5

comprimento = 10
difAlt = 5

rampas = []
rampas.append(Rampa(Ponto(-2 * comprimento, ycomum, 50), Ponto(- comprimento, ycomum, 40), rLarg))
rampas.append(Rampa(Ponto(- comprimento, ycomum, 35),    Ponto(0, ycomum, 25), rLarg))
rampas.append(Rampa(Ponto(0, ycomum, 20),                Ponto(comprimento, ycomum, 30), rLarg))
rampas.append(Rampa(Ponto(comprimento, ycomum, 25),       Ponto(2 * comprimento, ycomum, 15), rLarg))

for r in rampas:
    print "Proxima Rampa..."
    print r.pontos
    print " ", Operacoes.entortaRampa(r.pontos, [60, 60, 60, 60])
    


