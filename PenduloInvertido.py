from math import sin
from math import cos
from math import pi

class PenduloInvertido:
    """
    Clase que modela el comportamiento del pendulo Invertido

    Su constructor toma como parametros iniciales:
        1_Angulo inicial
        2_Velocidad angular inicial
        3_Masa del carro (en kg)
        4_Masa de la barra (en kg)
        5_Longitud de la barra (en m)
        6_Gravedad (en m/s**2)

    Las funciones -aceleracion_angular-
                  -velocidad_angular-
                  -f_angulo-
        calculan las aceleraciones, velocidades
        y posiciones angulares respectivamente
        y guardan esos valores en 3 listas
    """

    def __init__(self,angulo_inicial,vel_inicial,M,m,l, g = 9.8):
        self.angulo = angulo_inicial
        self.angulos = []
        self.velocidades = []
        self.angulos.append(self.angulo)
        self.vel_angular = vel_inicial
        self.velocidades.append(self.vel_angular)
        self.masa_carrito = M
        self.masa_barra = m
        self.gravedad = g
        self.long_barra = l

    def aceleracion_angular(self, t, vel, F, tita):
        self.acel_angular = self.gravedad*sin(tita)+cos(tita)*((-F-self.masa_barra*self.long_barra*vel**2*sin(tita))/(self.long_barra*((4/3)-(self.masa_barra*cos(tita)*cos(tita))/(self.masa_barra+self.masa_carrito))))
        return self.acel_angular

    def velocidad_angular(self,dt):
        self.vel_angular += self.acel_angular*dt
        self.velocidades.append(self.vel_angular)
        return self.vel_angular

    def f_angulo(self,dt):
        self.angulo += self.vel_angular*dt + (1/2)*self.acel_angular*(dt**2)
        self.angulos.append(self.angulo)
        return self.angulo