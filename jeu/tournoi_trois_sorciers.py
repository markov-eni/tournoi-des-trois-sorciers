from jeu import Partie
from jeu import Sorcier


class TournoiTroisSorciers(Partie):

    def __init__(self):

        epreuve_oeuf_dragon = Epreuve("Epreuve de l'oeuf du dragon",[]) # not solid 
        epreuve_lac = Epreuve("Epreuve du lac",[])
        epreuve_labyrinthe = Epreuve("Epreuve labyrinthe",[])

        self.epreuves = [epreuve_oeuf_dragon, epreuve_lac, epreuve_labyrinthe]

    def jouer(self, sorcier : Sorcier):
        for epreuve in self.epreuves : 
            resultat = epreuve.tenter
            if not resultat :
                self.fin()
                break
    def fin():
        pass
    