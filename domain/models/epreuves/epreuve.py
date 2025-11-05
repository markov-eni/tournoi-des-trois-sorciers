from domain.models.objets import Objet
from domain.models.personnages import Personnage
from domain.models.epreuves import Interaction, EpreuveIterator

from typing import List
from abc import ABC, abstractmethod



class Epreuve():

    interactions : List[Interaction]

    def __init__(self, nom :str , description :str)->None:
        self.nom = nom
        self.description = description
        self.interactions = []

    def tenter(self, personnage : Personnage)->bool:
        return True
    
    
    # Iterator pattern implementation

    # il faut un conteneur pour itérer 
    def ajouter_interaction(self, interaction : Interaction )->None:
        self.interactions.append(interaction)

    # instanciation de l'iterator
    # On sépare la logique d'itération dans une classe distincte 
    def create_iterator(self)->EpreuveIterator:
        return EpreuveIterator(self.interactions)

