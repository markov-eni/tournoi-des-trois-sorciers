from objets import Objet
from typing import List
from abc import ABC

class Epreuve(ABC):
    def __init__(nom :str , description ,objets: List[Objet]):
        self.nom = nom
        self.description = description
        self.objets = objets
        
    def tenter(self)->bool:
        pass

    def reussir(self):
        pass