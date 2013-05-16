from geo.ponto import Ponto
from geo.vetor import Vetor
import geo.operacoes as Operacoes
from config.observador import Observador
import math

# descobre onde fica o ponto do topo da linha
# cujo ponto da base fica em (0, 10, 0)
# para ele ter 30 cm mas aparentar ter 55 cm
print Operacoes.descobreNovoPonto(Ponto(0, 10, 0), 30, 55)
