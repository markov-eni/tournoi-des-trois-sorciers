from domain.models.parties import Partie
from domain.models.personnages import Sorcier
from domain.models.epreuves import Epreuve
from domain.models.parties.etats import EtatPartie

class PartieTournoiTroisSorciers(Partie):
    """
    Le jeu tournoi des 3 soricers est constitué de parties 
    """

    def __init__(self, etat_initial : EtatPartie):


        super.__init__(etat_initial)

        
        # TODO : instancier les epreuves en dehors de la partie car une partie contient des épreuves 
        epreuve_oeuf_dragon = Epreuve("Epreuve de l'oeuf du dragon","<desc>",[]) 
        epreuve_lac = Epreuve("Epreuve du lac","<desc>",[])
        epreuve_labyrinthe = Epreuve("Epreuve labyrinthe","<desc>",[])

        self.epreuves = [epreuve_oeuf_dragon, epreuve_lac, epreuve_labyrinthe]

    def jouer(self, sorcier : Sorcier):
        for epreuve in self.epreuves : 
            resultat = epreuve.tenter(sorcier)
            if not resultat :
                self.game_over()
                break
        
    def game_over():
        print("Perdu")
    