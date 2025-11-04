"""
Harry Potter et la coupe de Feu : 

    REMAKE du tournoi des 3 sorciers 

"""

from jeu import Sorcier, TournoiTroisSorciers, LancerAvadaKeavra


def main():

    # 1. Creation du Personnage

    nom = "Tom Jedusor"
    maison = "Serpentard"
    lancer_sortilege = LancerAvadaKeavra.lancer_sort
    
    sorcier = Sorcier(nom, maison,lancer_sortilege ) # => not solid

    sorcier.attaquer()

    # 2. Jouer la partie
    partie = TournoiTroisSorciers().jouer(sorcier)

if __name__ == "__main__":
    main()