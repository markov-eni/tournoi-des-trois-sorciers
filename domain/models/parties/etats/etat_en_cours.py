from domain.models.parties.etats import EtatPartie, ContextPartie
from domain.models.parties.etats.etat_arrete import EtatArrete

class EtatEnCours(EtatPartie):

    def __init__(self):
        pass
    
    def commencer( context : ContextPartie):
        raise Exception("Impossible de débuter une partie qui a déjà commencé")
    
    def terminer(context : ContextPartie):
        etat_termine = EtatArrete()
        context.set_etat(etat_termine)
