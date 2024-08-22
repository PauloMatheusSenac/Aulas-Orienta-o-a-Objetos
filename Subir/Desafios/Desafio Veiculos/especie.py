from veiculo import*
class Especie (Veiculo):
    def __init__(self, marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso,especie):
        super().__init__(marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso)
        self.especie = especie