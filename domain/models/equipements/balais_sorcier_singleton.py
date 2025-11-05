from domain.models.equipements import BalaisSorcier


class BalaisSorcierSingleton():

    def get_balais(self) -> BalaisSorcier:
        if not hasattr(self,'balais_sorcier'):
            self.balais_sorcier = BalaisSorcier()
        return self.balais_sorcier
