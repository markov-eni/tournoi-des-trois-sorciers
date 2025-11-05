from domain.models.parties import EtatPartie, EtatArrete, Context

class EtatEnCours(EtatPartie):

    def __init__(self):
        pass
    
    def commencer( context : ContextPartie):
        raise Exception("Impossible de débuter une partie qui a déjà commencé")
    
    def terminer(context : ContextPartie):
        etat_termine = EtatTermine()
        context.set_etat(etat_termine)
