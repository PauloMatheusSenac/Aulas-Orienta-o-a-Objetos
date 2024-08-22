from reino import Reino

class Filo (Reino):
    def __init__(self, nome, nutricao, organizacaocelular, tipologia, nomeFilo):
        super().__init__(nome, nutricao, organizacaocelular, tipologia)
        self.nomeFilo = nomeFilo
    