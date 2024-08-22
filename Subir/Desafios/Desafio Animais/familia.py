from ordem import Ordem
class Familia (Ordem):
    def __init__(self, nome, reino, filo, classe, ordem, familia):
        super().__init__(nome, reino, filo, classe, ordem)
        self.familia = familia