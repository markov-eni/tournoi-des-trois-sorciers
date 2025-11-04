from domain.objets.objet_factory import ObjetFactory
from domain.objets.bague import Bague 


class BagueFactory(ObjetFactory):

    @staticmethod
    def create_object()->Bague:
        return Bague()