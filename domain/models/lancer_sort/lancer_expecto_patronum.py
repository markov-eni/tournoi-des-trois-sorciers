from domain.models.lancer_sort import LancerSortilege

class LancerExpectoPatronum(LancerSortilege):

    @staticmethod
    def lancer_sort()->str:
        return "Expecto Patronum ! "

