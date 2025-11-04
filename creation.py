from equipements import BalaisSorcierSingleton, BaguetteMagiqueBuilder
from objets import BagueFactory , ClefFactory


# 1. Singleton 

balais_sorcier = BalaisSorcierSingleton().get_balais()

print(balais_sorcier)

#2. Factory
sac = []

bague  = BagueFactory.create_object()
clef = ClefFactory.create_object()

sac.append(bague)
sac.append(clef)

print(sac)


# 3. Builder

baguette_magique_surpuissante = BaguetteMagiqueBuilder().bois("sureau").puissance("99").create()

print(baguette_magique_surpuissante)

# 4. Prototype 

balais_sorcier_copy = balais_sorcier.__clone__()

print(balais_sorcier, balais_sorcier_copy)

# 5. Abstract Factory

