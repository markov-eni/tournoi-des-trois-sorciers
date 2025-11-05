from abc import ABC , abstractmethod


class ContextPartie(ABC):
    """
    Interface forçant l'implémentation d'une méthode pour gérer l'état d'un objet
    """
    @abstractmethod
    def set_etat(etat):
        pass