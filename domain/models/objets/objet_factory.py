from abc import ABC, abstractmethod
from domain.models.objets.objet import Objet

class ObjetFactory(ABC):

    @abstractmethod
    def create_object()->Objet:
        pass