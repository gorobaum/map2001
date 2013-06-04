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
tamBaseColuna = 4

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
    
basesColunas = []
i = 0
print "Agora calculando a posicao das bases das Colunas..."
print ""
for r in rampas:
    print "Proxima Coluna..."
    basesColunas.append(Operacoes.achaBaseDaColuna(r.pontosAparencia, tamBaseColuna))
    print "\tPontos da Base: %s" % (basesColunas[i])
    i += 1
    print ""

topoAparenteColunas = []
i = 0
print "Agora calculando a posicao do topo real das Colunas..."
print ""
for r in rampas:
	print "Proxima Coluna..."	
	topoAparenteColunas.append(Operacoes.achaAlturaAparenteDaColuna(r.pontosAparencia, basesColunas[i]))
	print "\tPontos do Topo: %s" % (topoAparenteColunas[i])
	i += 1
	print ""

rampasTopoColuna = []
i = 0
print "Calculando o topo real das Colunas..."
print ""
for r in rampas:
	print "Proxima Coluna..."
	rampaTopo = Rampa(topoAparenteColunas[i][0], topoAparenteColunas[i][3], tamBaseColuna)
	rampasTopoColuna.append(Operacoes.arrumaColuna(rampaTopo.pontosAparencia, razao))
	print "\tPontos do Topo Real: %s" % (rampasTopoColuna[i])
	i += 1
	print ""