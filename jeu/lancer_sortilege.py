from abc import ABC , abstractmethod


class LancerSortilege(ABC):
    """
    Bridge Design pattern pour toutes les manières de lancer un sort.

    Ici il est mal implémenté dans le sens ou le bridge devrait etre utiliser sur la manière de lancer un sort 
    Alors que la maniere de lancer un sort est la meme , c'est juste le sort qui diffère 
    """
    
    @staticmethod
    @abstractmethod
    def lancer_sort()->str:
        pass