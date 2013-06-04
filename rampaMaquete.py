from geo.ponto import Ponto
from modelo.base import Base
from modelo.rampa import Rampa
import geo.operacoes as Operacoes
import config.size as Tamanho
from config.observador import Observador
import math

ycomum = 10
rLarg = 5

comprimento = 10
difAlt = 5
tamBase = 3

rampas = []
rampas.append(Rampa(Ponto(-2 * comprimento, ycomum, 30), Ponto(- comprimento, ycomum, 25), rLarg))
rampas.append(Rampa(Ponto(- comprimento, ycomum, 23),    Ponto(0, ycomum, 20), rLarg))
rampas.append(Rampa(Ponto(0, ycomum, 18),                Ponto(comprimento, ycomum, 23), rLarg))
rampas.append(Rampa(Ponto(comprimento, ycomum, 21),       Ponto(2 * comprimento, ycomum, 17), rLarg))

alturas = []
alturas.append( [30, 30, 26, 26] )
alturas.append( [25, 25, 25, 25] )
alturas.append( [24, 24, 22, 22] )
alturas.append( [21, 21, 19, 19] )


i = 0
print "Posicao do observador: %s" % Observador.posicao
print ""
for r in rampas:
    print "Proxima Rampa..."
    print "\tPontos Apar: %s" % (r.pontosAparencia)
    r.setPontosReal(Operacoes.entortaRampaPorZ(r.pontosAparencia, alturas[i]))
    print "\tPontos Real: %s" % (r.pontosReal)
    i += 1
    print ""
    
alturasDaBase = []
j = 0
for r in rampas:
	alturasDaBase[j] = Operacoes.alturasDaBase(tamBase, r.pontosReal)
	j += 1


