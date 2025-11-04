"""
Harry Potter et la coupe de Feu : 

    REMAKE du tournoi des 3 sorciers 

"""

from jeu import Sorcier, TournoiTroisSorciers


def main():

    # 1. Creation du Personnage

    nom = "Tom Jedusor"
    maison = "Serpentard"
    sorcier = Sorcier(nom, maison)

    # 2. Jouer la partie
    partie = TournoiTroisSorciers().jouer(sorcier)

if __name__ == "__main__":
    main()