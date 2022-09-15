import numpy as np
import matplotlib.pyplot as plt
import time
import Partie_1
import random


def test_py_plot():
    # Ici on décrit les abscisses
    # Entre 0 et 5 en 10 points
    x_axis_list = np.arange(0, 1000, 10)
    fig, ax = plt.subplots()
    # Dessin des courbes, le premier paramètre
    # correspond aux point d'abscisse le
    # deuxième correspond aux points d'ordonnées
    # le troisième paramètre, optionnel permet de
    # choisir éventuellement la couleur et le marqueur
    ax.plot(x_axis_list, x_axis_list, 'bo-', label='Identité')
    ax.plot(x_axis_list, x_axis_list ** 2, 'r*-', label='Carré')
    ax.plot(x_axis_list, x_axis_list ** 3, 'g*-', label='Cube')
    ax.plot(x_axis_list, x_axis_list, 'bo-', label='Identité')
    ax.plot(x_axis_list, x_axis_list ** 2, 'r*-', label='Carré')
    ax.plot(x_axis_list, x_axis_list ** 3, 'g*-', label='Cube')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y',
           title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    # fig.savefig("test.png")
    plt.show()


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
    tab_resultats_func1 = []

    for e in taille_listes:
        start_pc_func_1 = time.perf_counter()
        for i in range(nb_exec):
            funct1(Partie_1.gen_list_random_int(e))
        end_pc_func_1 = time.perf_counter()
        elapsed_time_exec_func_1 = end_pc_func_1 - start_pc_func_1
        moy_perf_func_1 = elapsed_time_exec_func_1 / nb_exec
        tab_resultats_func1.append(moy_perf_func_1)

    tab_resultats_func2 = []

    for e in taille_listes:
        start_pc_func_2 = time.perf_counter()
        for i in range(nb_exec):
            funct2(Partie_1.gen_list_random_int(e))
        end_pc_func_2 = time.perf_counter()
        elapsed_time_exec_func_2 = end_pc_func_2 - start_pc_func_2
        moy_perf_func_2 = elapsed_time_exec_func_2 / nb_exec
        tab_resultats_func2.append(moy_perf_func_2)

    return tab_resultats_func1, tab_resultats_func2


print(perf_mix(Partie_1.mix_list, random.shuffle, [10, 100, 1000], 10))


def perf_extract(funct1: callable, funct2: callable, taille_listes: list[int], nb_exec: int) -> (list, list):
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

    tab_resultats_func1 = []

    for e in taille_listes:
        start_pc_func_1 = time.perf_counter()
        for i in range(nb_exec):
            funct1(Partie_1.gen_list_random_int(e), random.randint(1, e - 1))
        end_pc_func_1 = time.perf_counter()
        elapsed_time_exec_func_1 = end_pc_func_1 - start_pc_func_1
        moy_perf_func_1 = elapsed_time_exec_func_1 / nb_exec
        tab_resultats_func1.append(moy_perf_func_1)

    tab_resultats_func2 = []

    for e in taille_listes:
        start_pc_func_2 = time.perf_counter()
        for i in range(nb_exec):
            funct2(Partie_1.gen_list_random_int(e), random.randint(1, e - 1))
        end_pc_func_2 = time.perf_counter()
        elapsed_time_exec_func_2 = end_pc_func_2 - start_pc_func_2
        moy_perf_func_2 = elapsed_time_exec_func_2 / nb_exec
        tab_resultats_func2.append(moy_perf_func_2)

    return tab_resultats_func1, tab_resultats_func2


# print(perf_extract(Partie_1.extract_elements_list, random.sample, [10, 100, 1000], 100))


def affiche_resultat_test_mix(resultat: tuple):
    """
    Affiches les résultats du test mix
    :param resultat:
    :type resultat:
    :return:
    :rtype:
    """
    x_axis_list = (10, 100, 1000)
    fig, ax = plt.subplots()
    ax.plot(x_axis_list, resultat[0], 'bo-', label='mix_list')
    ax.plot(x_axis_list, resultat[1], 'r*-', label='shuffle')
    ax.set(xlabel='nombre de liste', ylabel='Performances moyenne',
           title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


def affiche_resultat_test_extract(resultat: tuple):
    """
    Affiches les résultats du test mix
    :param resultat:
    :type resultat:
    :return:
    :rtype:
    """
    x_axis_list = (10, 100, 1000)
    fig, ax = plt.subplots()
    ax.plot(x_axis_list, resultat[0], 'bo-', label='extract elements liste')
    ax.plot(x_axis_list, resultat[1], 'r*-', label='random.sample')
    ax.set(xlabel='nombre de liste', ylabel='Performances moyenne',
           title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


# affiche_resultat_test_mix((perf_mix(Partie_1.mix_list, random.shuffle, [10, 100, 1000], 10)))

# affiche_resultat_test_extract(perf_extract(Partie_1.extract_elements_list, random.sample, [10, 100, 1000], 100))


def fusion(liste_a: list, liste_b: list) -> list:
    """
    :param liste_a:
    :type liste_a:
    :param liste_b:
    :type liste_b:
    :return:
    :rtype:
    """
    if len(liste_a) == 0:
        return liste_b
    elif len(liste_b) == 0:
        return liste_a
    elif liste_a[0] <= liste_b[0]:
        return [liste_a[0]] + fusion(liste_a[1:], liste_b)
    else:
        return [liste_b[0]] + fusion(liste_a, liste_b[1:])


def tri_fusion(liste_t: list) -> list:
    """
    :param liste_t:
    :type liste_t:
    :return:
    :rtype:
    """
    if len(liste_t) <= 1:
        return liste_t
    else:
        milieu = len(liste_t) // 2
        return fusion(tri_fusion(liste_t[:milieu]), tri_fusion(liste_t[milieu:]))


print(tri_fusion([3, 2, 1, 0]))


def perf_tri(funct1: callable, funct2: callable, taille_listes: list[int], nb_exec: int, config: int = 1) -> (
        list, list):
    """
    Permet de calculer le temps d’exécution moyen des deux fonctions
    de mélange (mix_list et random.shuffle) passées en paramètre dans une même configuration, c’est-à-
    dire pour une même liste
    :param config:
    :type config:
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

    tab_resultats_func1 = []

    for e in taille_listes:
        start_pc_func_1 = time.perf_counter()
        for i in range(nb_exec):
            if config == 1:
                funct1(Partie_1.gen_list_random_int(e))
            elif config == 2:
                funct1(sorted(Partie_1.gen_list_random_int(e)))
            else:
                funct1(sorted(Partie_1.gen_list_random_int(e), reverse=True))
        end_pc_func_1 = time.perf_counter()
        elapsed_time_exec_func_1 = end_pc_func_1 - start_pc_func_1
        moy_perf_func_1 = elapsed_time_exec_func_1 / nb_exec
        tab_resultats_func1.append(moy_perf_func_1)

    tab_resultats_func2 = []

    for e in taille_listes:
        start_pc_func_2 = time.perf_counter()
        for i in range(nb_exec):
            if config == 1:
                funct2(Partie_1.gen_list_random_int(e))
            elif config == 2:
                funct2(sorted(Partie_1.gen_list_random_int(e)))
            else:
                funct2(sorted(Partie_1.gen_list_random_int(e), reverse=True))
        end_pc_func_2 = time.perf_counter()
        elapsed_time_exec_func_2 = end_pc_func_2 - start_pc_func_2
        moy_perf_func_2 = elapsed_time_exec_func_2 / nb_exec
        tab_resultats_func2.append(moy_perf_func_2)

    return tab_resultats_func1, tab_resultats_func2


print("")
print(perf_tri(tri_fusion, sorted, [10, 100, 1000], 10))
print(perf_tri(tri_fusion, sorted, [10, 100, 1000], 10, config=2))
print(perf_tri(tri_fusion, sorted, [10, 100, 1000], 10, config=3))


# afficher les resultat pyplot


def affiche_resultat_test_tri(resultat1: tuple, resultat2: tuple, resultat3: tuple):
    """

    :param resultat1:
    :type resultat1:
    :param resultat2:
    :type resultat2:
    :param resultat3:
    :type resultat3:
    :return:
    :rtype:
    """
    x_axis_list = (10, 100, 1000)
    fig, ax = plt.subplots()
    ax.plot(x_axis_list, resultat1[0], 'bo-', label='extract elements liste')
    ax.plot(x_axis_list, resultat1[1], 'r*-', label='random.sample')
    ax.plot(x_axis_list, resultat2[2], 'bo-', label='extract elements liste')
    ax.plot(x_axis_list, resultat2[3], 'r*-', label='random.sample')
    ax.plot(x_axis_list, resultat3[4], 'bo-', label='extract elements liste')
    ax.plot(x_axis_list, resultat3[5], 'r*-', label='random.sample')
    ax.set(xlabel='nombre de liste', ylabel='Performances moyenne',
           title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()
