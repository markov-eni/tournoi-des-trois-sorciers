from domain.epreuves import Epreuve
from domain.personnages import Sorcier

# classe à détruire puisqu'il s'agit d'un objet d'une épreuve et pas un type d'pereuve en lui meme

class EpreuveOeufDragon(Epreuve):

    def __init__(self):
        super.__init__(
            "Epreuve de l'oeuf du dragon",
            """
                Le but est de récupérer un oeuf qu'un dragon garde précieusement
            """,
            )

        

    def tenter(self,sorcier : Sorcier ):

        