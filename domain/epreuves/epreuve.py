from domain.objets import Objet
from domain.personnages import Personnage
from typing import List
from abc import ABC, abstractmethod

class Epreuve(ABC):
    def __init__(self, nom :str , description :str, actions : List)->None:
        self.nom = nom
        self.description = description
        self.actions = actions
        
        
    @abstractmethod
    def tenter(self, personnage : Personnage)->bool:
        return True
