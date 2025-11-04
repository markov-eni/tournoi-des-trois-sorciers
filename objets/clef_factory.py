from objets.objet_factory import ObjetFactory
from objets.clef import Clef 


class ClefFactory(ObjetFactory):

    @staticmethod
    def create_object()->Clef:
        return Clef()