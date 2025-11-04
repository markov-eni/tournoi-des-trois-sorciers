from jeu.partie import Partie
from jeu.sorcier import Sorcier
from jeu.epreuve import Epreuve

class TournoiTroisSorciers(Partie):

    def __init__(self):

        epreuve_oeuf_dragon = Epreuve("Epreuve de l'oeuf du dragon","<desc>",[]) # not solid 
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
    