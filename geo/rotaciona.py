import math
from ponto import Ponto
from vetor import Vetor

class MaeMatriz:
    def __mul__(self, t):
        if isinstance(t, Vetor):
            v = [t.x, t.y, t.z, 0]
        else:
            v = [t.x, t.y, t.z, 1]
        result = []
        for l in self.m:
            result.append(v[0] * l[0] + v[1] * l[1] + v[2] * l[2] + v[3] * l[3])
        x = t.__class__(result[0], result[1], result[2])
        return x

class RotacionaX(MaeMatriz):
    def __init__(self, tetaEntrada):
		teta = math.radians(tetaEntrada)
		linha1 = [1, 0, 0, 0]
		linha2 = [0, math.cos(teta), -math.sin(teta), 0]
		linha3 = [0, math.sin(teta), math.cos(teta), 0]
		linha4 = [0, 0, 0, 1]
		self.m = [linha1, linha2, linha3, linha4]

class RotacionaY(MaeMatriz):
    def __init__(self, tetaEntrada):
		teta = math.radians(tetaEntrada)
		linha1 = [math.cos(teta), 0, math.sin(teta),0]
		linha2 = [0, 1, 0, 0]
		linha3 = [-1 * math.sin(teta), 0, math.cos(teta), 0]
		linha4 = [0, 0, 0, 1]
		self.m = [linha1, linha2, linha3, linha4]

class RotacionaZ(MaeMatriz):
	def __init__(self, tetaEntrada):
		teta = math.radians(tetaEntrada)
		linha1 = [math.cos(teta), -math.sin(teta), 0, 0]
		linha2 = [math.sin(teta), math.cos(teta), 0, 0]
		linha3 = [0, 0, 1, 0]
		linha4 = [0, 0, 0, 1]
		self.m = [linha1, linha2, linha3, linha4]

class Translada(MaeMatriz):
	def __init__(self, x, y, z):
		linha1 = [1, 0, 0, x]
		linha2 = [0, 1, 0, y]
		linha3 = [0, 0, 1, z]
		linha4 = [0, 0, 0, 1]
		self.m = [linha1, linha2, linha3, linha4]
