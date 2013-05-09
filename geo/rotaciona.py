import math

class MaeMatriz:
    def __mul__(self, t):
        if isinstance(t, Ponto):
            v = [t.x, t.y, t.z, 1]
        else:
            v = [t.x, t.y, t.z, 0]
        result = []
        return result

class RotacionaX(MaeMatriz):
    def __init__(self, tetaEntrada):
		teta = tetaEntrada * 180 / math.pi
		linha1 = [1, 0, 0, 0]
		linha2 = [0, math.cos(self.teta), -1 * math.sin(self.teta), 0]
		linha3 = [0, math.sin(self.teta), math.cos(self.teta), 0]
		linha4 = [0, 0, 0, 1]
		self.m = [linha1, linha2, linha3, linha4]

class RotacionaY(MaeMatriz):
    def __init__(self, tetaEntrada):
		teta = tetaEntrada * 180 / math.pi
		linha1 = [math.cos(self.teta), 0, math.sin(self.teta),0]
		linha2 = [0, 1, 0, 0]
		linha3 = [-1 * math.sin(self.teta), 0, math.cos(self.teta), 0]
		linha4 = [0, 0, 0, 1]
		self.m = [linha1, linha2, linha3, linha4]

class RotacionaZ(MaeMatriz):
	def __init__(self, tetaEntrada):
		teta = tetaEntrada * 180 / math.pi
		linha1 = [math.cos(self.teta), -1 * math.sin(self.teta), 0, 0]
		linha2 = [math.sin(self.teta), math.cos(self.teta), 0, 0]
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
