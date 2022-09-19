from random import *


def gen_list_random_int(int_nb: int = 10, int_binf: int = 0, int_bsup: int = 10) -> list:
    """
    Génere une liste de n nombre compris entre une borne superieur et inferieur
    :param int_nb:
    :type int_nb: int
    :param int_binf:
    :type int_binf: int
    :param int_bsup:
    :type int_bsup: int
    :return:
    :rtype: list[int]
    """
    l_nb = []
    for i in range(int_nb):
        l_nb.append(randint(int_binf, int_bsup))
    return l_nb


liste_aleatoire = gen_list_random_int(10)
print(liste_aleatoire)


def mix_list(liste: list) -> list:
    """
    Prends une liste en paramètre et retourne la liste mélanger aléhatoirement
    :param liste:
    :type liste: list
    :return:
    :rtype: list
    """
    liste_copie = liste.copy()
    liste_melanger = []
    longueur_liste = len(liste)
    for i in range(longueur_liste):
        index_rand = randint(0, longueur_liste - i - 1)
        liste_melanger.append(liste_copie[index_rand])
        liste_copie.pop(index_rand)
    return liste_melanger


def testeur_de_fonction(funct, jeu_de_tests, arg_nb=1):
    """
    Fonction permettant de tester d'autres fonctions
    :return: void
    """
    if arg_nb == 1:
        for e in jeu_de_tests:
            print(f"{funct.__name__}({e}) = {funct(e)}")
    elif arg_nb == 2:
        for e in jeu_de_tests:
            print(f"{funct.__name__}({e[0]}, {e[1]}) = {funct(e[0], e[1])}")
    print("\n")


JDT1 = ([0, 1, 2],
        [0, 1, 2, 3])
testeur_de_fonction(mix_list, JDT1)


def choose_element_list(list_which_to_choose: list):
    """
    Prends en paramètre une liste et retourne un de ses élements au hazard
    :param list_which_to_choose:
    :type list_which_to_choose:
    :return:
    :rtype:
    """
    return list_which_to_choose[randint(0, len(list_which_to_choose) - 1)]


JDT1 = ([0, 1, 2],
        [0, 1, 2, 3])

testeur_de_fonction(choose_element_list, JDT1)


def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_elements_to_extract: int) -> list:
    """
    Renvoie un certain nombre d'élements choisis aux hasards dans une liste
    :param list_in_which_to_choose:
    :type list_in_which_to_choose:
    :param int_nbr_of_elements_to_extract:
    :type int_nbr_of_elements_to_extract:
    :return:
    :rtype:
    """
    elt_choisis = []
    liste_copie = list_in_which_to_choose
    for i in range(int_nbr_of_elements_to_extract):
        elt_random = randint(0, len(liste_copie) - 1)
        elt_choisis.append(liste_copie[elt_random])
        liste_copie.pop(elt_random)
    return elt_choisis


JDT2 = (([0, 1, 2], 2),
        ([0, 1, 2, 3], 1))

testeur_de_fonction(extract_elements_list, JDT2, arg_nb=2)
