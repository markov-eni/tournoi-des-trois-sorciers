from abc import ABC , abstractmethod
from typing import List
from domain.models.epreuves import Epreuve
from domain.models.personnages import Personnage

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
    def game_over(self):
        pass
