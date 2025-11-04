from domain.parties import Partie
from domain.personnages import Sorcier
from domain.epreuves import Epreuve

class TournoiTroisSorciers(Partie):

    def __init__(self):

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
    