from domain.epreuves import Epreuve
from domain.personnages import Sorcier

class EpreuveOeufDragon(Epreuve):

    def __init__(self):
        super.__init__(
            "Epreuve de l'oeuf du dragon",
            """
                Le but est de récupérer un oeuf qu'un dragon garde précieusement
            """,
            [])

    def tenter(self,sorcier : Sorcier ):
        