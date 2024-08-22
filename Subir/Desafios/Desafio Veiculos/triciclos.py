from categoria import*

class Triciclo (Categoria):
    def __init__(self, marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso, especie, categoria,tipo_habilitacao):
        super().__init__(marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso, especie, categoria)
        self.tipo_habilitacao = tipo_habilitacao
        self.especie = especie
        self.categoria = categoria