from filo import Filo
class Classe (Filo):
    def __init__(self, nome, reino, filo, classe):
        super().__init__(nome, reino, filo)
        self.classe = classe