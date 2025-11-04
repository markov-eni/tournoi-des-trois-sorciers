from jeu.personnage import Personnage
from jeu.sorcier import Sorcier

class SorcierGris(Personnage):

    sorcier : Sorcier 

    """
        Decorator design pattern

        Un sorcier gris à des capacités d'attaque plus puissantes qu'un simple sorcier 
        
    """
    
    def __init__(self, sorcier : Sorcier):
        self.sorcier = sorcier

    def attaquer(self):
        return self.sorcier.attaquer() + "  Puissance 1000 ! "
