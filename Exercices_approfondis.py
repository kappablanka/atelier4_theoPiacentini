import numpy as np
import matplotlib.pyplot as plt
import time
import Partie_1


def test_py_plot():
    # Ici on décrit les abscisses
    # Entre 0 et 5 en 10 points
    x_axis_list = np.arange(0,5.5,0.5)
    fig, ax = plt.subplots()
    # Dessin des courbes, le premier paramètre
    # correspond aux point d'abscisse le
    # deuxième correspond aux points d'ordonnées
    # le troisième paramètre, optionnel permet de
    # choisir éventuellement la couleur et le marqueur
    ax.plot(x_axis_list,x_axis_list,'bo-',label='Identité')
    ax.plot(x_axis_list,x_axis_list**2, 'r*-', label='Carré')
    ax.plot(x_axis_list,x_axis_list**3,'g*-', label='Cube')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
    title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    # fig.savefig("test.png")
    plt.show()

def test_perf_counter():
    # Exemple d'utilisation
    # Pour mesurer le temps d'exécution nous avons à notre disposition
    # la fonction perf_counter()
    n = 10000000
    # Récupération du temps système et démarrage du chronomètre
    start_pc = time.perf_counter()
    for i in range(n):
        None
    end_pc = time.perf_counter()
    elapsed_time_pc = end_pc - start_pc
    print("Temps écoulé entre les deux mesures : ", elapsed_time_pc)
    print("Temps estimé pour une instruction", elapsed_time_pc / n)
    # Exécutez ce code et vérifiez par vous-même la variabilité des mesures.

# test_perf_counter()


def perf_mix(funct1: callable, funct2: callable, taille_listes: list[int], nb_exec: int) -> (list, list):
    """
    Permet de calculer le temps d’exécution moyen des deux fonctions
    de mélange (mix_list et random.shuffle) passées en paramètre dans une même configuration, c’est-à-
    dire pour une même liste
    :param funct1:
    :type funct1: callable
    :param funct2:
    :type funct2: callable
    :param taille_listes:
    :type taille_listes: list
    :param nb_exec:
    :type nb_exec: int
    :return:
    :rtype:
    """
    start_pc_func_1 = time.perf_counter()
    for i in range(nb_exec):
        for e in taille_listes:
            funct1(Partie_1.gen_list_random_int(e))
    end_pc_func_1 = time.perf_counter()
    elapsed_time_exec_func_1 = start_pc_func_1 - end_pc_func_1

    start_pc_func_2 = time.perf_counter()
    for i in range(nb_exec):
        for e in taille_listes:
            funct1(Partie_1.gen_list_random_int(e))
    end_pc_func_2 = time.perf_counter()
    elapsed_time_exec_func_2 = start_pc_func_2 - end_pc_func_2