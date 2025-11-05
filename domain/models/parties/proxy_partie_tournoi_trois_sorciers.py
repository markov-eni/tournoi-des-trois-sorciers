from domain.models.parties import Partie , PartieTournoiTroisSorciers
from domain.models.personnages import Sorcier


class ProxyPartieTournoiTroisSorciers(Partie):
    """
        Design Pattern Proxy

        On manipule l'objet comme si c'était un vrai 
        mais on rajoute des comportements à la classe avant ou apres des actions 
        sans "augmenter" les cpt de celle-ci comme udécorateur le ferai
    """

    tournoi_trois_sorciers : Partie

    nombre_de_joueurs : int 
    
    def __init__(self, nombre_de_joueurs : int): 
        """
        """
        self.tournoi_trois_sorciers = PartieTournoiTroisSorciers() # TODO : déplacer logique instanciation ailleur
        self.nombre_de_joueurs = nombre_de_joueurs

    def check_joueur_necessaires(self)->bool:
        if self.nombre_de_joueurs > 1 :
            return False 

        return True 

    def jouer(self, sorcier : Sorcier ):
        
        if not self.check_joueur_necessaires():
            raise Exception("Nombre de joueur nécessaire ne correspond pas")
        
        self.tournoi_trois_sorciers.jouer(sorcier)
        
        

    def game_over(self):
        pass