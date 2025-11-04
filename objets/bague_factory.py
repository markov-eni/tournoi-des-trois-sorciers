from objets.objet_factory import ObjetFactory
from objets.bague import Bague 


class BagueFactory(ObjetFactory):

    @staticmethod
    def create_object()->Bague:
        return Bague()