from random import sample

class Cartela:
    def __init__(self, nome):
        self.nome = nome
        self.b = sample(range(1, 16), 5)
        self.i = sample(range(16, 31), 5)
        self.n = sample(range(31, 46), 5)
        self.g = sample(range(46, 61), 5)
        self.o = sample(range(61, 76), 5)

        self.n[2] = "⭐"

    def imprimedados(self):
        print(f"Cartela do {self.nome}")
        print(self.b)
        print(self.i)
        print(self.n)
        print(self.g)
        print(self.o)

    def verifica_vitoria(self, numeros_sorteados):
        linhas = [self.b, self.i, self.n, self.g, self.o]
        
        # Horizontal
        for linha in linhas:
            if all(numero in numeros_sorteados for numero in linha):
                return True
        
        # Vertical
        for coluna in range(5):
            if (self.b[coluna] in numeros_sorteados and
                self.i[coluna] in numeros_sorteados and
                self.n[coluna] in numeros_sorteados and
                self.g[coluna] in numeros_sorteados and
                self.o[coluna] in numeros_sorteados):
                return True
        
        # Diagonal
        if all(self.b[i] in numeros_sorteados for i in range(5)) or \
           all(self.i[i] in numeros_sorteados for i in range(5)) or \
           all(self.n[i] in numeros_sorteados for i in range(5)) or \
           all(self.g[i] in numeros_sorteados for i in range(5)) or \
           all(self.o[i] in numeros_sorteados for i in range(5)):
            return True
        
        if all(self.b[4-i] in numeros_sorteados for i in range(5)) or \
           all(self.i[4-i] in numeros_sorteados for i in range(5)) or \
           all(self.n[4-i] in numeros_sorteados for i in range(5)) or \
           all(self.g[4-i] in numeros_sorteados for i in range(5)) or \
           all(self.o[4-i] in numeros_sorteados for i in range(5)):
            return True
        
        return False
