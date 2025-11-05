from abc import ABC , abstractmethod
from domain.models.parties import ContextPartie

class EtatPartie(ABC):

    @abstractmethod
    def commencer( context : ContextPartie):
        pass
    
    @abstractmethod
    def terminer(context : ContextPartie):
        pass

    