from classe import Classe

class Especie (Classe):
    def __init__(self, nome, nutricao, organizacaocelular, tipologia, nomeFilo, nomeClasse, nomeEspecie):
        super().__init__(nome, nutricao, organizacaocelular, tipologia, nomeFilo, nomeClasse)
        self.nomeEspecie = nomeEspecie

    def __str__(self):
        return f"{self.nome}, {self.nutricao}, {self.organizacaocelular}, {self.tipologia}, {self.nomeFilo}, {self.nomeClasse}, {self.nomeEspecie}"