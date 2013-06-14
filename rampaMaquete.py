#! /usr/bin/python

from geo.ponto import Ponto
from modelo.base import Base
from modelo.rampa import Rampa
import geo.operacoes as Operacoes
import config.size as Tamanho
from config.observador import Observador
import math
import sys
import config.config as Config

ycomum = 10
rLarg = 5

comprimento = 13
cp = comprimento
difAlt = 5
tamBaseColuna = 4

if len(sys.argv) > 1:
    for param in sys.argv[1:]:
        if param == "-d" or param == "--debug":
            Config.debug = True

debug = Config.debug

rampas = []
rampas.append(Rampa(Ponto(-2 * cp, ycomum, 26), Ponto(-2 * cp, ycomum+rLarg, 26), Ponto(- cp, ycomum+rLarg, 22), Ponto(-cp, ycomum, 22), 26, 24))
rampas.append(Rampa(rampas[-1], cp, 2, -4))
rampas.append(Rampa(rampas[-1], cp, 4, -4))
rampas.append(Rampa(rampas[-1], cp, -4, 0))

i = 0
for r in rampas:
    if debug:
        print "Posicao real da rampa %s = %s" %(i, rampas[i].pontosF)
        print ""
    i += 1

if debug:
    print "Posicao do observador: %s" % Observador.posicao
    print ""
j = 1
print "import rhinoscriptsyntax as rs"
print ""
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
if debug:
    print "Agora calculando a posicao das bases das Colunas..."
    print ""
for r in rampas:
    if debug:
        print "Proxima Coluna..."
    b_aux = Operacoes.achaBaseDaColuna(r.pontosF, tamBaseColuna)
    basesColunas.append(b_aux)
    if debug:
        print "\tPontos da Base: %s" % (b_aux)
        print ""

topoAparenteColunas = []
i = 0
if debug:
    print "Agora calculando a posicao do topo real das Colunas..."
    print ""
for r in rampas:
    if debug:
        print "Proxima Coluna..."    
    topoAparenteColunas.append(Operacoes.achaAlturaAparenteDaColuna(r.pontosF, basesColunas[i]))
    if debug:
        print "\tPontos do Topo: %s" % (topoAparenteColunas[i])
    i += 1
    if debug:
        print ""

rampasTopoColuna = []
i = 0
if debug:
    print "Calculando o topo real das Colunas..."
    print ""
for r in rampas:
    if debug:
        print "Proxima Coluna..."
    topoColunaReal = Operacoes.topoRealColuna(topoAparenteColunas[i], r)
    rampasTopoColuna.append(topoColunaReal)
    if debug:
        print "\tPontos do Topo Real: %s" % (topoColunaReal)
    i += 1
    if debug:
        print ""

for i in range(4):
    print "##################"
    print "# coluna %s" % i
    print "##################"

    basesColunas[i].reverse()
    
    rampasTopoColuna[i].reverse()
    a = [] + basesColunas[i] + rampasTopoColuna[i]
    basesColunas[i].reverse()
    rampasTopoColuna[i].reverse()

    print "colunaPoints%s = []" % i
    for j in range(8):
        print "colunaPoints%s.append([%s, %s, %s])" % (i, a[j].x, a[j].y, a[j].z)
    print "box = rs.AddBox(colunaPoints%s)" % (i)
    
