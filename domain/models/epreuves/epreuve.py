from domain.models.objets import Objet
from domain.models.personnages import Personnage
from typing import List
from abc import ABC, abstractmethod

class Epreuve():
    def __init__(self, nom :str , description :str, actions : List)->None:
        self.nom = nom
        self.description = description
        self.actions = actions
        

    def tenter(self, personnage : Personnage)->bool:
        return True
