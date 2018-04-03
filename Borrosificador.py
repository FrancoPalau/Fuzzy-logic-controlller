from math import sin
from math import cos
from math import pi

class Borrosificador:
    """
    Clase que se encarga de borrosificar los valores de entrada (angulo y velocidad)
    segun los conjuntos borrosos definidos en cada funcion.

    Su constructor no toma parametros

    La funcion -calc_pert_tita()-
        _recibe el valor de tita y a que conjunto pertenece
        _retorna el valor de pertenencia segun el conjunto

    La funcion -calc_pert_vel()_
        _recibe el valor de la velocidad y a que conjunto pertenece
        _retorna el valor de pertenencia segun el conjunto

    La funcion -calc_centro_fuerza()-
        _recibe un conjunto
        _retorna el centro de dicho conjunto segun los
            conjuntos borrosos de la variable "Fuerza"
    """

    def __init__(self):
        pass

    def calc_triangular(self,a,b,c,x):

        if x < a:
            return 0
        elif (a <= x) and (x <= b):
            return (x-a)/(b-a)
        elif (b <= x) and (x <= c):
            return (c-x)/(c-b)
        else:
            return 0

    def cal_pert_tita(self, valor, conjunto):

        if conjunto == "NG":
            return self.calc_triangular(-5 * pi / 4, -pi / 2, -pi / 4, valor)
        elif conjunto == "NP":
            return self.calc_triangular(-pi / 2, -pi / 4, 0, valor)
        elif conjunto == "Z":
            return self.calc_triangular(-pi / 4, 0, pi / 4, valor)
        elif conjunto == "PP":
            return self.calc_triangular(0, pi / 4, pi / 2, valor)
        elif conjunto == "PG":
            return self.calc_triangular(pi / 4, pi / 2, 5 * pi / 4, valor)

    def calc_pert_vel(self,valor,conjunto):

        if conjunto == "NG":
            return self.calc_triangular(-1.5, -1.0, -0.5, valor)
        elif conjunto == "NP":
            return self.calc_triangular(-1.0, -0.5, 0, valor)
        elif conjunto == "Z":
            return self.calc_triangular(-0.5, 0, 0.5, valor)
        elif conjunto == "PP":
            return self.calc_triangular(0, 0.5, 1.0, valor)
        elif conjunto == "PG":
            return self.calc_triangular(0.5, 1.0, 1.5, valor)

    def calc_centro_fuerza(self, conjunto):

        if conjunto == "NG":
            return -10
        elif conjunto == "NP":
            return -5
        elif conjunto == "Z":
            return 0
        elif conjunto == "PP":
            return 5
        elif conjunto == "PG":
            return 10
