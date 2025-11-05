from domain.models.parties.etats import EtatPartie, ContextPartie
import domain.models.parties.etats.etat_arrete

class EtatEnCours(EtatPartie):

    def __init__(self):
        pass
    
    def commencer( context : ContextPartie):
        raise Exception("Impossible de débuter une partie qui a déjà commencé")
    
    def terminer(context : ContextPartie):
        etat_termine = etat_arrete.EtatArrete()
        context.set_etat(etat_termine)
