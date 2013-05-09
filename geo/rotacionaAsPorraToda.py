import math

class MatrizLouca:
	def rotacionaEmX(tetaEntrada):
		teta = tetaEntrada * 180 / math.pi
		linha1 = [1, 0, 0, 0]
		linha2 = [0, math.cos(self.teta), -1 * math.sin(self.teta), 0]
		linha3 = [0, math.sin(self.teta), math.cos(self.teta), 0]
		linha4 = [0, 0, 0, 1]
		return m = [linha1, linha2, linha3, linha4]

	def rotacionaEmY(tetaEntrada):
		teta = tetaEntrada * 180 / math.pi
		linha1 = [math.cos(self.teta), 0, math.sin(self.teta),0]
		linha2 = [0, 1, 0, 0]
		linha3 = [-1 * math.sin(self.teta), 0, math.cos(self.teta), 0]
		linha4 = [0, 0, 0, 1]
		return m = [linha1, linha2, linha3, linha4]

	def rotacionaEmZ(tetaEntrada):
		teta = tetaEntrada * 180 / math.pi
		linha1 = [math.cos(self.teta), -1 * math.sin(self.teta), 0, 0]
		linha2 = [math.sin(self.teta), math.cos(self.teta), 0, 0]
		linha3 = [0, 0, 1, 0]
		linha4 = [0, 0, 0, 1]
		return m = [linha1, linha2, linha3, linha4]

	def translada(x, y, z):
		linha1 = [1, 0, 0, x]
		linha2 = [0, 1, 0, y]
		linha3 = [0, 0, 1, z]
		linha4 = [0, 0, 0, 1]
		return m = [linha1, linha2, linha3, linha4]