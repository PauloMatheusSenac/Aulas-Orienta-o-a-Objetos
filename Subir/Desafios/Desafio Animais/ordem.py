from classe import Classe
class Ordem (Classe):
    def __init__(self, nome, reino, filo, classe, ordem):
        super().__init__(nome, reino, filo, classe)
        self.ordem = ordem