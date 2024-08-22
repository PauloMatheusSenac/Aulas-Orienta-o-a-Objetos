from familia import Familia
class Genero (Familia):
    def __init__(self, nome, reino, filo, classe, ordem, familia, genero):
        super().__init__(nome, reino, filo, classe, ordem, familia)
        self.genero = genero