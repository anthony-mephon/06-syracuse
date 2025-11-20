"""
Ce module contient des fonctions pour calculer et analyser la suite de Syracuse.
Il inclut également une fonction pour tracer la suite.
"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Trace la suite de Syracuse donnée en utilisant Plotly.

    Args:
        lsyr (list): La suite de Syracuse à tracer.

    Returns:
        None: Affiche le graphique.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                 'xaxis': {'title': {'text':"x"}},
                                 'yaxis': {'title': {'text':"y"}},
                                 }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    #return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            l.append(n)
        else:
            n = n * 3 + 1
            l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """
    # votre code ici
    #n = 0
    return l.index(1)

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """
    # votre code ici
    tva = l[0]
    for i in range(len(l) - 1):
        if l[i+1] < tva:
            return i
    return None

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """
    # votre code ici
    return max(l)


#### Fonction principale


def main():
    """Fonction principale pour exécuter les calculs et le tracé de Syracuse."""

    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    #print(syracuse_l(15))
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
