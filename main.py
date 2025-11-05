"""
------ Harry Potter et la coupe de Feu --------

    Le Tournoi des 3 sorciers

"""
from domain.models.parties import  PartieTournoiTroisSorciers , ProxyPartieTournoiTroisSorciers
from domain.models.parties.etats import EtatArrete
from domain.models.lancer_sort import LancerAvadaKedavra
from domain.models.personnages import SorcierBuilder, SorcierGris


def main():

    # 1. Creation du Personnage

    nom ="Tom Jedusor" # input("Entrer votre nom :")
    maison ="Serpentard" # input("Entrer votre nom de maison (Gryffondor, Serpentard) :")
    lancer_sortilege = LancerAvadaKedavra.lancer_sort # bridge indiquant que un sorcier ne lancer qu'un seul type de sort 
    # => un strategy pattern serait adapté pour changer de sort dynamiquement 
    
    sorcier = SorcierBuilder().create().nom(nom).maison(maison).lancer_sortilege(lancer_sortilege).build()

    print(sorcier.attaquer())

    # 2. Sorcier Gris  ( decorator )
    sorcier_gris = SorcierGris(sorcier)

    print(sorcier_gris.attaquer())


    # 2. Jouer la partie via un proxy
    nbr_joueurs =  1
    etat_initial = EtatArrete()
    partie = ProxyPartieTournoiTroisSorciers(etat_initial, nbr_joueurs).jouer(sorcier)

    # 3. 

if __name__ == "__main__":
    main()