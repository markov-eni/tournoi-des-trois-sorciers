from domain.objets.objet_factory import ObjetFactory
from domain.objets.clef import Clef 


class ClefFactory(ObjetFactory):

    @staticmethod
    def create_object()->Clef:
        return Clef()