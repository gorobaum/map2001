import math
from geo.ponto import Ponto
from geo.vetor import Vetor

class Plano:
	def __init__(self, p1, p2, p3):
		self.p = p1
		self.v1 = (p2 - p1)
		self.v2 = (p3 - p1)

	def intersecReta(self, r):
		print "aeae", r.v
		alfa3 = (self.p.z-r.p.z)/(self.v2.z-(r.v.z*self.v2.x/r.v.x)-((self.v1.z-(r.v.z*self.v1.x/r.v.x))*(self.v2.y-(r.v.y*self.v2.x/r.v.x))/(self.v1.y-(r.v.y*self.v1.x/r.v.x))))
		alfa2 = ((self.p.y-r.p.y)+alfa3*(self.v2.y-(r.v.y*self.v2.x/r.v.x)))/(self.v1.y-(r.v.y*self.v1.x/r.v.x))
		alfa1 = ((self.p.x-r.p.x)+alfa2*(self.v1.x)+alfa3*(self.v2.x))/(r.v.x)
		return r.p + r.v*alfa1