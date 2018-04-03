import matplotlib.pyplot as plt
from PenduloInvertido import *
from Borrosificador import *

if __name__ == '__main__':

    fig, axes = plt.subplots()

    conjuntos_tita = "NG NP Z PP PG".split()     #Conjuntos borrosos elegidos para
    conjuntos_vel = "NG NP Z PP PG".split()      #  tita y velocidad

    base_de_reglas = [["NG","NP","NP","NP","NP"],
                      ["NP","NP","NP","NP","Z"],      #Matriz de reglas (filas velocidad, columnas tita)
                      ["NP","NP","Z","PG","PP"],
                      ["Z","PP","PP","PP","PP"],
                      ["PP","PP","PP","PP","PG"]]

    lista_grafico = [0.175,0.262,0.35,0.436,0.524,-0.175,-0.262,-0.35,-0.436,-0.524] #10,15,20,25,30 grados positivos y negativos

    for i in lista_grafico:
        pendulo = PenduloInvertido(i,0,1,0.1,0.2) #Creacion del pendulo con sus condiciones iniciales
        pendulo.aceleracion_angular(0.01,pendulo.vel_angular,5,pendulo.angulo) #Calculo aceleracion inicial
        borro = Borrosificador() #Creacion del Borrosificador

        counter = 0
        tiempo = [0] #Lista donde se almacenan los tiempo absolutos de cada iteracion
        dt = 0.01

        while(tiempo[counter] < 40):

            media_centros_denom = 0
            media_centros_num = 0
            valores_reglas = [] #Lista donde almacenamos el valor resultande de cada regla

            for i, conjunto_vel in enumerate(conjuntos_vel):       #Iteramos sobre las listas de los conjuntos
                valores_reglas.append([])                       #para obtener todas las reglas posibles
                for j, conjunto_tita in enumerate(conjuntos_tita):
                    valores_reglas[i].append(min(borro.cal_pert_tita(pendulo.angulo,conjunto_tita),
                                                 borro.calc_pert_vel(pendulo.vel_angular,conjunto_vel)))

                    media_centros_denom += valores_reglas[i][j]
                    media_centros_num += valores_reglas[i][j]*borro.calc_centro_fuerza(base_de_reglas[i][j])

            media_centros = media_centros_num / media_centros_denom

            counter+=1
            tiempo.append(tiempo[counter-1] + dt)

            #Actualizacion de las variables del pendulo
            pendulo.f_angulo(dt)
            pendulo.velocidad_angular(dt)
            pendulo.aceleracion_angular(dt, pendulo.vel_angular, media_centros, pendulo.angulo)

        #Graficamos
        axes.set_xlabel('Tiempo [s]')
        axes.set_ylabel('Angulo [rad]')
        axes.set_title('Control Péndulo')
        axes.plot(tiempo, pendulo.angulos)
        #axes.plot(tiempo, pendulo.velocidades, label = "Velocidad [rad/s]")
    plt.show()
