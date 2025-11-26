"""
Module principal pour les calculs et l'affichage de la suite de Syracuse.
"""
# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER (Sauf corrections de style pour Pylint) ###
def syr_plot(lsyr):
    """
    Affiche le graphique de la suite de Syracuse avec Plotly.

    :param lsyr: La liste des valeurs de la suite.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({ 'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                 }
    )

    # Correction R1721: Optimisation de la création de liste
    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    # Correction R1711: Le return None explicite est inutile
#######################

def syracuse_l(n):
    """
    Fonction secondaire syracuse.

    :param n: Le nombre souhaité
    :return: La suite de Syracuse sous forme de liste
    """
    l_syr = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        l_syr.append(n)
    return l_syr

def temps_de_vol(l):
    """
    Fonction temps de vol.

    :param l: La liste de la suite
    :return: Le temps de vol
    """
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """
    Fonction temps_de_vol_en_altitude.

    :param l: La liste de la suite
    :return: Le temps de vol en altitude
    """
    depart = l[0]
    duree = 0
    for i in range(1, len(l)):
        if l[i] > depart:
            duree = duree + 1
        else:
            break
    return duree

def altitude_maximale(l):
    """
    Fonction altitude_maximale.

    :param l: La liste de la suite
    :return: L'altitude maximale
    """
    return max(l)

#### Fonction principale

def main():
    """
    Fonction principale pour l'exécution du programme.
    """
    # vos appels à la fonction secondaire ici
    n_test = 15
    lsyr = syracuse_l(n_test)
    print(f"Suite de Syracuse pour n={n_test}: {lsyr}")

    # Pour n=3, les valeurs de la suite sont [3, 10, 5, 16, 8, 4, 2, 1].
    # tv=7, tva=5 (10, 5, 16, 8, 4, 2, 1), am=16
    n_test_3 = 3
    lsyr_3 = syracuse_l(n_test_3)
    print(f"\nSuite de Syracuse pour n={n_test_3}: {lsyr_3}")
    print(f"Temps de vol (attendu 7): {temps_de_vol(lsyr_3)}")
    print(f"Temps de vol en altitude (attendu 5): {temps_de_vol_en_altitude(lsyr_3)}")
    print(f"Altitude maximale (attendu 16): {altitude_maximale(lsyr_3)}")

    # Décommenter la ligne suivante pour visualiser le graphique de la suite pour n=15
    # syr_plot(lsyr)

    # Affichage des résultats pour n=15
    print(f"\nRésultats pour n={n_test}:")
    print(f"Temps de vol: {temps_de_vol(lsyr)}")
    print(f"Temps de vol en altitude: {temps_de_vol_en_altitude(lsyr)}")
    print(f"Altitude maximale: {altitude_maximale(lsyr)}")


if __name__ == "__main__":
    main()
