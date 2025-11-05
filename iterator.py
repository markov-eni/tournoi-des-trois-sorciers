from domain.models.epreuves import Epreuve, InteractionIterator, Interaction


epreuve_oeuf_dragon = Epreuve("Epreuve de l'oeuf du dragon","<desc>") 
epreuve_oeuf_dragon.ajouter_interaction(Interaction("Le dragon gardien de l'oeuf dort profondémment, que faites vous ?"))
epreuve_oeuf_dragon.ajouter_interaction(Interaction("Toujours assoupi, souhaitez-vous continuer de vous approcher ?"))


interaction_iterator = epreuve_oeuf_dragon.create_iterator()

while(interaction_iterator.has_next()):
    print(interaction_iterator.position)
    interaction = interaction_iterator.next()
    print(interaction.description)