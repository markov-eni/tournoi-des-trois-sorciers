from abc import ABC , abstractmethod
from typing import List
from domain.models.epreuves import Epreuve
from domain.models.personnages import Personnage
from domain.models.parties.etats import EtatPartie, ContextPartie

class Partie(ContextPartie, ABC):
    """
    Une partie est composée d'un personnage surmontant différentes épreuves =
    """

    etat_partie : EtatPartie
    
    personnage : Personnage

    epreuves : List[Epreuve]

    # NOTE! 
    # Probleme héritage de classe abstraite / interface
    # Toute partie doit avoir un etat initial
    # Mais toute partie doit implémenter sa façon de jouer
    def __init__(self):
        pass
        

    @abstractmethod
    def set_etat(self, etat ):
        pass

    @abstractmethod
    def jouer(self, personnage : Personnage):
        pass

    @abstractmethod
    def game_over(self):
        pass
