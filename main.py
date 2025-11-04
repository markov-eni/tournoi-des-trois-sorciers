"""
Harry Potter et la coupe de Feu : 

    REMAKE du tournoi des 3 sorciers 

"""
from domain.parties import  TournoiTroisSorciers
from domain.lancer_sort import LancerAvadaKedavra
from domain.personnages import Sorcier, SorcierGris


def main():

    # 1. Creation du Personnage

    nom = "Tom Jedusor"
    maison = "Serpentard"
    lancer_sortilege = LancerAvadaKedavra.lancer_sort
    
    sorcier = Sorcier(nom, maison,lancer_sortilege ) # => not solid

    print(sorcier.attaquer())

    # 2. Sorcier Gris
    sorcier_gris = SorcierGris(sorcier)

    print(sorcier_gris.attaquer())


    # 2. Jouer la partie
    partie = TournoiTroisSorciers().jouer(sorcier)

if __name__ == "__main__":
    main()