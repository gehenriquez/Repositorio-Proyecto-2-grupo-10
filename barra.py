import numpy as np

g = 9.81 #kg*m/s^2


class Barra(object):

    """Constructor para una barra.
    Los datos en orden son: nodo_i, nodo_j, radio, espesor, Modulo E, densidad, fluencia"""
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni = ni
        self.nj = nj
        self.R = R
        self.t = t
        self.E = E
        self.ρ = ρ
        self.σy = σy

    def obtener_conectividad(self):
        return [self.ni,self.nj]

    def calcular_area(self):
        """Calcula el area de una barra de seccion circular"""
        return np.pi*(self.R**2-(self.R-self.t)**2)

    def calcular_largo(self, barra):
        i=barra.obtener_coordenada_nodal(self.ni)
        j=barra.obtener_coordenada_nodal(self.nj)
        z=i-j
        return np.sqrt(z[0]**2+z[1]**2)

    def calcular_peso(self, barra):
            """Entrega el peso de una barra  """

            return self.ρ*self.calcular_largo(barra)*self.calcular_area()* g