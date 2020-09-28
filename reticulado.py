
import numpy as np


class Reticulado(object):
	"""Define un reticulado"""

	def __init__(self):
		super(Reticulado, self).__init__()
		
		self.xyz=np.zeros((0,3),dtype=np.double)
		self.Nodos = 0.
		self.barras = []
		self.cargas = {}
		self.restricciones = {}

	def agregar_nodo(self, x, y,z=0):
            self.xyz.resize((self.Nodos+1,3))
            self.xyz[Nodos,:]= [x,y,z]
            self.Nodos+=1
            return None
		
	def agregar_barra(self, barra):

		return None

	def obtener_coordenada_nodal(self, n): 

		return None

	def calcular_peso_total(self):

		return None

	def obtener_nodos(self):

		return None

	def obtener_barras(self):

		return None

	def agregar_restriccion(self, nodo, gdl, valor=0.0):

		returnNone

	def agregar_fuerza(self, nodo, gdl, valor):

		return None

	def ensamblar_sistema(self):

		return None

	def resolver_sistema(self):

		return None

	def recuperar_fuerzas(self):

		return None
    
    def __str__( self ):
        q= "informacion reticulado \n \n"
        q+=" los nodos son: \n"
        q+= f"{self.xyz}"
        return q
        