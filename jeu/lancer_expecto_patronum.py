from jeu.lancer_sortilege import LancerSortilege

class LancerExpectoPatronum(LancerSortilege):

    @staticmethod
    def lancer_sort()->str:
        return "Expecto Patronum ! "

