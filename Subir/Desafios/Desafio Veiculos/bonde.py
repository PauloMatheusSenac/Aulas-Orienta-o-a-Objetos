from categoria import* 


class Bonde (Categoria):
    def __init__(self, marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso, especie, categoria,necessita_habilitacao,tipo_habilitacao):
        super().__init__(marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso, especie, categoria)
        self.necessita_habilitacao=necessita_habilitacao
        self.tipo_habilitacao = tipo_habilitacao
