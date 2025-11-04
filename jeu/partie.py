from abc import ABC , abstractmethod
from typing import List
from jeu import Epreuve, Personnage

class Partie(ABC):
    """
    Une partie est composée d'un personnage surmontant différentes épreuves =
    """
    
    personnage : Personnage

    epreuves : List[Epreuve]

    @abstractmethod
    def jouer(self, personnage : Personnage):
        pass

    @abstractmethod
    def fin(self):
        pass
