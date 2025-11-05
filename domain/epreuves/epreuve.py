from domain.objets import Objet
from domain.personnages import Personnage
from typing import List
from abc import ABC, abstractmethod

class Epreuve(ABC):
    def __init__(self, nom :str , description ,objets: List[Objet]):
        self.nom = nom
        self.description = description
        self.objets = objets
        
    @abstractmethod
    def tenter(self, personnage : Personnage)->bool:
        return True
