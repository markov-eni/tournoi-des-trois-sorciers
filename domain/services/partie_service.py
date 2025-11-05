from domain.models.parties import Partie
from domain.models.personnage import Personnage
from domain.models.etats import EtatEnCours

class PartieService():
    """
    L'objectif de cette classe est de dire comment jouer une partie
    """

    def __init__(self, partie : Partie )->None:
        self.partie = partie

    def jouer(self, personnage : Personnage)->None:
        """
        Déroulement d'une partie de manière générale
        """

        # 1. Démarrage de la partie
        self.partie.set_etat(EtatEnCours())

        # 2. 
        for epreuve in self.partie.epreuves : 
            interaction_iterator = epreuve.create_iterator()
            while(interaction_iterator.has_next()):
                # récupérer l'interaction
                interaction = interaction_iterator.next()
                # choix joueur selon l'interaction proposée
                choix_joueur = joueur_service.get_choix_joueur(interaction)
                # Récupérer le résultat de l'interaction du joueur
                resultat = interaction ( joueur )
            