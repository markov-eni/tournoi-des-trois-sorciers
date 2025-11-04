from abc import ABC, abstractmethod

class Personnage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def attaquer(self):
        pass