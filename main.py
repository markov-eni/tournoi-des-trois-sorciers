from equipements import BaguetteMagiqueSingleton
from objets import BagueFactory , ClefFactory

baguette_singleton =  BaguetteMagiqueSingleton()

baguette_magique = baguette_singleton.get_baguette()

print(baguette_magique)

# Remplir le sac à dos 
sac = []

bague  = BagueFactory.create_object()
clef = ClefFactory.create_object()

sac.append(bague)
sac.append(clef)

print(sac)