<div style="text-align: center;">

# 🧹  Harry Potter et la coupe de Feu 🏆
# Le Tournoi des 3 sorciers 🧙‍♂️

</div>

## ⚡️ Présentation du jeu
Définissez votre sorcier et remportez le tournoi des 3 sorciers ! <br>
Ce tournoi est composé de 3 épreuves :
- La quête de l'oeuf de dragon
- La nage du lac aux sirènes
- La conquête du labyrinthe de Poudlard

Toute erreur vous sera fatale.


## ✨ Design pattern implémentés  

**creation**
- factory : [bague_factory](domain/models/objets/bague_factory.py)
- singleton : [baguette_magique](domain/models/equipements/baguette_magique_singleton.py)
- builder : [baguette_magique](domain/models/equipements/baguette_magique_builder.py)
- clone : [balais_sorcier](domain/models/equipements/balais_sorcier.py)

**structurel**
- proxy :  [tournoi_trois_sorciers](domain/models/parties/tournoi_trois_sorciers.py)
- bridge : [lancer_sortilege](domain/models/lancer_sort/lancer_sortilege.py)
- decorator : [sorcier_gris](domain/models/personnages/sorcier_gris.py)


**comportementaux**
- etat : [etat de la partie](domain/models/parties/etats/)
- iterator : [ iterer sur les interactions d'une épreuve](domain/models/epreuves/)

etape : reussie, echec, en cours 

## TODO
- faire un singleton de factory ?
- séprarer les interfaces des implémentations
