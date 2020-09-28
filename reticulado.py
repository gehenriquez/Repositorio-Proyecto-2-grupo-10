
import numpy as np


class Reticulado(object):
	"""Define un reticulado"""

	def __init__(self):
		super(Reticulado, self).__init__()
		
		self.xyz = np.zeros((1,3), dtype=np.double)
		self.Nodos = 0
		self.barras = []
		self.cargas = {}
		self.restricciones = {}

	def agregar_nodo(self, x, y,z=0):
        self.xyz.resize ((self.Nodos+1,3))
        self.xyz[Nodos,:]= [x,y,z]
        self.Nodos+=1
		return None
		
	def agregar_barra(self, barra):
		"""Implementar"""
		return

	def obtener_coordenada_nodal(self, n): 
		"""Implementar"""
		return 

	def calcular_peso_total(self):
		"""Implementar"""
		return 

	def obtener_nodos(self):
		"""Implementar"""
		return 

	def obtener_barras(self):
		"""Implementar"""
		return 

	def agregar_restriccion(self, nodo, gdl, valor=0.0):
		"""Implementar"""
		return

	def agregar_fuerza(self, nodo, gdl, valor):
		"""Implementar"""
		return

	def ensamblar_sistema(self):
		"""Implementar"""
		return

	def resolver_sistema(self):
		"""Implementar"""
		return

	def recuperar_fuerzas(self):
		"""Implementar"""
		return
    
    def __str__(self):
        q= "informacion reticulado \n \n"
        q+=" los nodos son: \n"
        q+= f"{self.xyz}"
        return q
        