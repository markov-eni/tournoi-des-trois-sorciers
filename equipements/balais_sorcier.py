from equipements.equipement import Equipement


class BalaisSorcier(Equipement):

    durabilite: int = 100 

    # en km/h , vitesse maximale atteignable en accélérant sur une ligne droite horizontale
    vitesse_maximale:int = 126
    
    def __init__(self):
        pass

    def voler():
        print("Indispensable pour une partie de quidditch !")

    # prototype
    def __clone__(self):
        balais_sorcier = BalaisSorcier()
        balais_sorcier.durabilite = self.durabilite
        balais_sorcier.vitesse_maximale = self.vitesse_maximale
        return balais_sorcier