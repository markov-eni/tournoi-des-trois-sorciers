"""
Hedwige, la chouette d'Harry Potter s'est échappée ! 
Ron a réussi à la localiser dans le bureau de Dumbledore
Malheureusement le bureau est sécurisé : il est nécessaire de traverser plusieurs salles pour y parvenir.

"""
from equipements import BalaisSorcierSingleton, BaguetteMagiqueBuilder
from sorcier import Sorcier

# 1. Creation du sorcier
sorcier = Sorcier()

# 2. Selection des equipements

balais_sorcier = BalaisSorcierSingleton().get_balais()
modeste_baguette_magique = BaguetteMagiqueBuilder().bois("sureau").puissance("99").create()

#