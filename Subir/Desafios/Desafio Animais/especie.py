from genero import Genero
class Especie (Genero):
    def __init__(self, nome, reino, filo, classe, ordem, familia, genero, especie):
        super().__init__(nome, reino, filo, classe, ordem, familia, genero)
        self.especie = especie

    def imprimir_dados (self):
        print(f"O nome do animal é: {self.nome}")
        print(f"O reino do animal é: {self.reino}")
        print(f"O filo do animal é: {self.filo}")
        print(f"A classe do animal é: {self.classe}")
        print(f"A ordem do animal é: {self.ordem}")
        print(f"A familia do animal é: {self.familia}")
        print(f"O genero do animal é: {self.genero}")
        print(f"A especie do animal é: {self.especie}")





    