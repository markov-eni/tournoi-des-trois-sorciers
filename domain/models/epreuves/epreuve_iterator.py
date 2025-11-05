from domain.models.epreuves import InteractionIterator
from domain.models.epreuves import Interaction

from typing import List

class EpreuveIterator(InteractionIterator):

    interactions : List[Interaction]

    position : int = 0 

    def __init__(self,interactions : List[Interaction] ):
        self.interactions = interactions


    def has_next(self)->bool:
        """
        Est-ce qu'il y a un élément suivant dans la liste ? 
        """
        return self.position < len(self.interactions) 


    def next(self)->Interaction:
        """
        """
        
        current_interaction = self.interactions[self.position]
        
        # avancer position pour la prochain item
        self.position += 1 

        return current_interaction
