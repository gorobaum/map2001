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
cp = comprimento
difAlt = 5
tamBaseColuna = 4

rampas = []
rampas.append(Rampa(Ponto(-2 * cp, ycomum, 30), Ponto(-2 * cp, ycomum+rLarg, 30), Ponto(- cp, ycomum+rLarg, 26), Ponto(-cp, ycomum, 26), 30, 28))
rampas.append(Rampa(rampas[-1], cp, -3, 0))
rampas.append(Rampa(rampas[-1], cp, 3, -3))
rampas.append(Rampa(rampas[-1], cp, -3, -6))

i = 0
for r in rampas:
    print "Posicao real da rampa %s = %s" %(i, rampas[i].pontosF)
    print ""
    i += 1

print "Posicao do observador: %s" % Observador.posicao
print ""
j = 1
for r in rampas:
    print "######################"
    print "#  Rampa numero %s ..." % j 
    print "######################"
    print "listPoint%s = []" % j
    for i in range(4):
        print "listPoint%s.append([%s, %s, %s])" % (j, r.pontosR[-i].x, r.pontosR[-i].y, r.pontosR[-i].z)
    for i in range(4):
        print "listPoint%s.append([%s, %s, %s])" % (j, r.pontosR[-i].x, r.pontosR[-i].y, r.pontosR[-i].z+0.01)
    print "box = rs.AddBox(listPoint%s)" % (j)
    j += 1
    print ""
    
basesColunas = []
rhinoColunas = []
i = 0
print "Agora calculando a posicao das bases das Colunas..."
print ""
for r in rampas:
    print "Proxima Coluna..."
    b_aux = Operacoes.achaBaseDaColuna(r.pontosF, tamBaseColuna)
    basesColunas.append(b_aux)
    print "\tPontos da Base: %s" % (b_aux)
    print ""

topoAparenteColunas = []
i = 0
print "Agora calculando a posicao do topo real das Colunas..."
print ""
for r in rampas:
	print "Proxima Coluna..."	
	topoAparenteColunas.append(Operacoes.achaAlturaAparenteDaColuna(r.pontosF, basesColunas[i]))
	print "\tPontos do Topo: %s" % (topoAparenteColunas[i])
	i += 1
	print ""

rampasTopoColuna = []
i = 0
print "Calculando o topo real das Colunas..."
print ""
for r in rampas:
	print "Proxima Coluna..."
	topoColunaReal = Operacoes.pegaCentroRampa(r.pontosR)
	print "\tPontos do Topo Real: %s" % (topoColunaReal)
	i += 1
	print ""
