from domain.equipements import BaguetteMagique


class BaguetteMagiqueBuilder():

    baguette_magique: BaguetteMagique

    def __init__(self):
        self.baguette_magique = BaguetteMagique()

    def bois(self,bois:str):
        self.baguette_magique.bois = bois
        return self

    def puissance(self, puissance:int):
        self.baguette_magique.puissance = puissance
        return self

    def create(self)->BaguetteMagique:
        return self.baguette_magique

    