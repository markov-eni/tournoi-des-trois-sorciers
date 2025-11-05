from abc import ABC , abstractmethod
from domain.models.epreuves import Interaction

class InteractionIterator(ABC):

    @abstractmethod
    def has_next(self)->bool:
        pass
        

    @abstractmethod
    def next(self)->Interaction:
        pass