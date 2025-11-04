from domain.objets import ClefFactory
from domain.equipements import BaguetteMagiqueBuilder
from domain.personnages import Sorcier

baguette_magique = BaguetteMagiqueBuilder().bois("sureau").puissance(62).create()

clef = ClefFactory.create_object()
