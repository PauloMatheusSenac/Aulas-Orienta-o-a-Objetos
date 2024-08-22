from veiculo import*
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso, necessita_habilitacao , tipo_habilitacao, especie , categoria):
        super().__init__(marca, modelo, ano, combustivel, passageiros, quantidade_eixos, tracao, profissao, estilo_vida, frequencia_uso)
        self.necessita_habilitacao = necessita_habilitacao
        self.tipo_habilitacao = tipo_habilitacao
        self.especie = especie
        self.categoria = categoria

    def necessita_habilitacao(self):
        return self.necessita_habilitacao
    
    def imprimedados_moto(self):
        print (f"A marca é: {self.marca} \nO modelo é: {self.modelo} \nO Ano é {self.ano} \nO tipo de combustivel é: {self.combustivel} \nO numero de passageiros é: {self.passageiros} \nA quantidade de eixos é: {self.quantidade_eixos} \nA tração é: {self.tracao} \nA espécoe é: {self.especie} \nA categoria é: {self.categoria} \nÉ necessaria habilitação: {self.necessita_habilitacao} \nA habilitação necessária é: {self.tipo_habilitacao} ")
