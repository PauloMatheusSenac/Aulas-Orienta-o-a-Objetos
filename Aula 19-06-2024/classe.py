from filo import Filo

class Classe(Filo):
    def __init__(self, nome, nutricao, organizacaocelular, tipologia, nomeFilo, nomeClasse):
        super().__init__(nome, nutricao, organizacaocelular, tipologia, nomeFilo)
        self.nomeClasse = nomeClasse