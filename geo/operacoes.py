from geo.ponto import Ponto
from geo.vetor import Vetor
from config.observador import Observador
import math

def descobreNovoPonto(base, alturaReal, alturaFicticia):
    p = Ponto(base.x, base.y, alturaFicticia)
    r = Ponto(base.x, base.y, alturaReal)
    v = Vetor(Observador.posicao, base)
    razao = float(r.z - p.z) / v.z
    novoV = v * razao
    novoPonto = p + novoV
    return novoPonto
