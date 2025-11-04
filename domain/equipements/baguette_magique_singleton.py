from domain.equipements import BaguetteMagique


class BaguetteMagiqueSingleton():

    def get_baguette(self) -> BaguetteMagique:
        if not hasattr(self,'baguette_magique'):
            self.baguette_magique = BaguetteMagique()
        return self.baguette_magique
