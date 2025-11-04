from abc import ABC, abstractmethod
from objets.objet import Objet

class ObjetFactory(ABC):

    @abstractmethod
    def create_object()->Objet:
        pass