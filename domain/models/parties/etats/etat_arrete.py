from domain.models.parties.etats import EtatPartie, ContextPartie
import domain.models.parties.etats.etat_en_cours

class EtatArrete(EtatPartie):

    def __init__(self):
        pass

    def commencer( context : ContextPartie):
        etat_en_cours = etat_en_cours.EtatEnCours()

        context.set_etat(etat_en_cours)

    
    def terminer(context : ContextPartie):
        raise Exception("Impossible de terminer une partie qui n'a pas commencé")
