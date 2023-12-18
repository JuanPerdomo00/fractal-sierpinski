#!/usr/bin/python3
#-*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import random



def main():
    max_iter = 10000 # numo de iteraciones
    seed_xy = [0.5, 0.5] # semillas en donde va empezar 

    # puntos del plano
    #         x  y
    puntoA = [0, 1]
    puntoB = [1, 1]
    puntoC = [0.5, 0]

    for _ in range(max_iter):
        aleatorie_number = random.random()  # Genera un número aleatorio entre 0 y 1

        if aleatorie_number <= 1/3:
            xf = (seed_xy[0] + puntoA[0]) / 2
            yf = (seed_xy[1] + puntoA[1]) / 2
        elif 1/3 < aleatorie_number <= 2/3:
            xf = (seed_xy[0] + puntoB[0]) / 2
            yf = (seed_xy[1] + puntoB[1]) / 2

        else:
            xf = (seed_xy[0] + puntoC[0]) / 2
            yf = (seed_xy[1] + puntoC[1]) / 2

        seed_xy = [xf, yf]
        plt.plot(seed_xy[0], seed_xy[1], 'k.', markersize=3)



if __name__ == "__main__":
    main()
    plt.show()

