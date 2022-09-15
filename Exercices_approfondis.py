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
    ax.plot(x_axis_list, resultat1[0], 'tab:blue', label='mon_tri sur liste hasards')
    ax.plot(x_axis_list, resultat1[1], 'tab:purple', label='sorted sur liste hasards ')
    ax.plot(x_axis_list, resultat2[0], 'tab:cyan', label='mon_tri sur liste trié')
    ax.plot(x_axis_list, resultat2[1], 'lightcoral', label='sorted sur liste trié')
    ax.plot(x_axis_list, resultat3[0], 'indianred', label='mon_tri sur liste trié reverse')
    ax.plot(x_axis_list, resultat3[1], 'firebrick', label='sorted sur liste  trié reverse')
    ax.set(xlabel='nombre de liste', ylabel='Performances moyenne',
           title='Fonctions identité, cube et carré')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


affiche_resultat_test_tri(perf_tri(tri_fusion, sorted, [10, 100, 1000], 10, config=1),
                          perf_tri(tri_fusion, sorted, [10, 100, 1000], 10, config=2),
                          perf_tri(tri_fusion, sorted, [10, 100, 1000], 10, config=3))


def is_sorted(liste: list):
    """

    :param liste:
    :type liste:
    :return:
    :rtype:
    """
    est_triee = True
    for i in range(1, len(liste)):
        if liste[i - 1] > liste[i]:
            est_triee = False
    return est_triee


def tri_stupide(liste: list):
    """
    Tri une liste en la mixant jusqu'à ce qu'elle soit triée
    :param liste:
    :type liste:
    :return:
    :rtype:
    """
    while not is_sorted(liste):
        liste = Partie_1.mix_list(liste)
    return liste


def tri_par_insertion(liste: list):
    """
    Aussi appelé tri du joueur de carte
    :param liste:
    :type liste:
    :return:
    :rtype:
    """
    for i in range(len(liste)):
        x = liste[i]
        j = i
        while j > 0 and liste[j - 1] > x:
            liste[j] = liste[j - 1]
            j = j - 1
        liste[j] = x
    return liste


def tri_selection(liste_t: list, n: int):
    for i in range(n - 1):
        mon_min = i
        for j in range(i + 1, n):
            if liste_t[j] < liste_t[mon_min]:
                mon_min = j
        if mon_min != i:
            temp = liste_t[i]
            liste_t[i] = liste_t[mon_min]
            liste_t[mon_min] = temp
    return liste_t


def tri_par_bulle(liste_t: list):
    """

    :return:
    :rtype:
    """
    for i in range(len(liste_t) - 1, 0, -1):
        tableau_trie = True
        for j in range(i):
            if liste_t[j + 1] < liste_t[j]:
                temp = liste_t[j + 1]
                liste_t[j + 1] = liste_t[j]
                liste_t[j] = temp
                tableau_trie = False
            if tableau_trie:
                return liste_t


# Tri fusion déjà implémenter plus haut !


def radix_sort(list_to_sort: list):
    """
    param list_to_sort:
    :type list_to_sort:
    :return:
    :rtype:
    """
    len_liste_to_sorte = []
    list_copier = list_to_sort.copy()
    for e in list_to_sort:
        len_liste_to_sorte.append(len(str(e)))
    for i in range(0, max(len_liste_to_sorte)):
        radix_order_sort(list_copier, i)
        print(list_copier)
    return list_copier


def radix_order_sort(list_to_sort: list, ordre: int):
    """
    param list_to_sort:
    :type list_to_sort:
    :return:
    :rtype:
    """
    copie_liste = list_to_sort
    for i in range(len(copie_liste)):
        copie_liste[i] = copie_liste[i] % 10**ordre - copie_liste[i] % 10**(ordre-1)

    return sorted(copie_liste)


print(radix_order_sort([30, 2, 1], 0))
print(radix_order_sort([30, 2, 1], 1))


