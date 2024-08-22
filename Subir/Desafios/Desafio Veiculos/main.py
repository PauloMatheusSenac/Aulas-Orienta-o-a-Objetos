from veiculo import*
from caminhao import*
from moto import*
from carro import* 
from bicicleta import*
from bonde import*
from caminhonete import*
from onibus import*
from ciclomotor import*
from triciclos import*

profissao_opcoes = {
   "1" : "Estudante",
   "2" : "Profissional liberal",
   "3" : "Empresário(a)",
   "4" : "Trabalhador(a) CLT",
   "5" : "Aposentado(a)"
}
estilo_vida_opcoes = {
    "1": "Muito ativo, sempre em movimento",
    "2": "Moderadamente ativo, com algumas atividades ao ar livre",
    "3": "Principalmente tranquilo e urbano",
    "4": "Focado em família e lazer"
}
frequencia_uso_opcoes = {      
    "1": "Regularmente (pelo menos uma vez por semana)",
    "2": "Com frequência (duas a três vezes por mês)",
    "3": "Ocasionalmente (uma vez por mês)",
    "4": "Raramente (menos de uma vez por mês)"
}
tracao_opcoes = {
    "1": "Dianteira",
    "2": "4x4",
    "3": "Traseira",
    "4": "Semi Reboque",
    "5": "Via aérea"
}
especie_opcoes = {
    "1": "Veículo de passageiros",
    "2": "Veículo de carga",
    "3": "Veículo misto",
    "4": "Veículo de competição",
    "5": "Veículo de tração",
    "6": "Veículo especial",
    "7": "Veículo de coleção"
}
categoria_opcoes = {
    "1": "Veículo particular",
    "2": "Veículo oficial",
    "3": "Veículo de representação diplomática",
    "4": "Veículo de coleção"
}
escolha_passageiros_opcoes = {
    "1": "2 passageiros ou menos",
    "2": "entre 3 e 5 passageiros",
    "3": "mais de 5 passageiros"
}
carros_cadastrados = [
    Carro("Ford", "EcoSport", 2023, "Flex", 2, 2, "Dianteira", "Estudante", "Muito ativo, sempre em movimento", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "Sim", "A", "SUV"),
    Carro("Chevrolet", "Onix", 2023, "Flex", 4, 2, "Dianteira", "Estudante", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "Sim", "B", "Hatchback"),
    Carro("Volkswagen", "Golf", 2023, "Flex", 4, 2, "Dianteira", "Profissional liberal", "Principalmente tranquilo e urbano", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo oficial", "Sim", "B", "Hatchback"),
    Carro("Honda", "Civic", 2023, "Flex", 4, 2, "Dianteira", "Empresário(a)", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "C", "Sedan"),
    Carro("Toyota", "Corolla", 2023, "Flex", 4, 2, "Dianteira", "Aposentado(a)", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo oficial", "Sim", "C", "Sedan"),
    Carro("Hyundai", "Creta", 2023, "Flex", 4, 2, "Dianteira", "Profissional liberal", "Moderadamente ativo, com algumas atividades ao ar livre", "Raramente (menos de uma vez por mês)", "Veículo de passageiros", "Veículo de representação diplomática", "Sim", "B", "SUV"),
    Carro("Jeep", "Renegade", 2023, "Flex", 4, 2, "4x4", "Trabalhador(a) CLT", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de passageiros", "Veículo de coleção", "Sim", "B", "SUV"),
    Carro("Fiat", "Argo", 2023, "Flex", 4, 2, "Dianteira", "Estudante", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "Sim", "B", "Hatchback"),
    Carro("Renault", "Duster", 2023, "Flex", 4,2, "4x2", "Profissional liberal", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo oficial", "Sim", "B", "SUV"),
    Carro("Kia", "Sportage", 2023, "Flex", 4, 2, "4x4", "Empresário(a)", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "C", "SUV"),
    Carro("Nissan", "Versa", 2023, "Flex", 4, 2, "Dianteira", "Aposentado(a)", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "Sim", "B", "Sedan"),
    Carro("Mercedes-Benz", "Classe A", 2023, "Gasolina", 4, 2, "Dianteira", "Empresário(a)", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de passageiros", "Veículo oficial", "Sim", "C", "Hatchback"),

]
motos_cadastradas = [
    Moto("Honda", "CG 160", 2023, "Gasolina", 2, 2, "Traseira", "Estudante", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Sim", "A", "Veículo de passageiros", "Veículo particular"),
    Moto("Yamaha", "MT-07", 2023, "Gasolina", 2, 2, "Traseira", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Sim", "A", "Veículo de passageiros", "Veículo particular"),
    Moto("Suzuki", "GSX-R1000", 2023, "Gasolina", 2, 2, "Traseira", "Empresário(a)", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Sim", "A", "Veículo de competição", "Veículo particular"),
    Moto("Kawasaki", "Ninja 650", 2023, "Gasolina", 2, 2, "Traseira", "Aposentado(a)", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Sim", "A", "Veículo de passageiros", "Veículo particular"),
    Moto("BMW", "S 1000 RR", 2023, "Gasolina", 2, 2, "Traseira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Sim", "A", "Veículo de passageiros", "Veículo particular"),
    Moto("Ducati", "Monster", 2023, "Gasolina", 2, 2, "Traseira", "Estudante", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Sim", "A", "Veículo de passageiros", "Veículo particular"),
    Moto("Harley-Davidson", "Sportster Iron 883", 2023, "Gasolina", 2, 2, "Traseira", "Profissional liberal", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Sim", "A", "Veículo de competição", "Veículo oficial"),
    Moto("Triumph", "Street Triple", 2023, "Gasolina", 2, 2, "Traseira", "Empresário(a)", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Sim", "A", "Veículo de coleção", "Veículo de coleção"),
    Moto("Aprilia", "RSV4", 2023, "Gasolina", 2, 2, "Traseira", "Aposentado(a)", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Sim", "A", "Veículo de passageiros", "Veículo de coleção"),
    Moto("Indian", "Scout", 2023, "Gasolina", 2, 2, "Traseira", "Trabalhador(a) CLT", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Sim", "A", "Veículo de competição", "Veículo de coleção"),
]

caminhoes_cadastrados = [
    Caminhao("Volvo", "FH 540", 2023, "Diesel", 2, 3, "Dianteira", "Profissional liberal", "Muito ativo, sempre em movimento", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo particular", "Sim", "E"),
    Caminhao("Scania", "R 500", 2023, "Diesel", 2, 3, "Dianteira", "Trabalhador(a) CLT", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de carga", "Veículo oficial", "Sim", "E"),
    Caminhao("Mercedes-Benz", "Actros 2651", 2023, "Diesel", 2, 3, "Dianteira", "Profissional liberal", "Moderadamente ativo, com algumas atividades ao ar livre", "Ocasionalmente (uma vez por mês)", "Veículo de carga", "Veículo de representação diplomática", "Sim", "E"),
    Caminhao("MAN", "TGX 29.500", 2023, "Diesel", 3, 3, "Dianteira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre","Raramente (menos de uma vez por mês)", "Veículo de carga", "Veículo particular", "Sim", "E"),
    Caminhao("Iveco", "Stralis", 2023, "Diesel", 3, 3, "Dianteira", "Profissional liberal", "Muito ativo, sempre em movimento", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo oficial", "Sim", "E"),
    Caminhao("DAF", "XF 530", 2023, "Diesel", 2, 3, "Dianteira", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de carga", "Veículo de coleção", "Sim", "E"),
    Caminhao("Ford", "Cargo 2842", 2023, "Diesel", 2, 3, "Dianteira", "Trabalhador(a) CLT", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de carga", "Veículo oficial", "Sim", "E"),
    Caminhao("Renault", "T 520", 2023, "Diesel", 5, 3, "Dianteira", "Profissional liberal", "Moderadamente ativo, com algumas atividades ao ar livre", "Raramente (menos de uma vez por mês)", "Veículo de carga", "Veículo particular", "Sim", "E"),
    Caminhao("Fiat", "M520", 2023, "Diesel", 2, 3, "Dianteira", "Profissional liberal", "Muito ativo, sempre em movimento", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo oficial", "Sim", "E"),
    Caminhao("Hyundai", "Xcient", 2023, "Diesel", 2, 3, "Dianteira", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de carga", "Veículo de representação diplomática", "Sim", "E"),
]
bicicletas_cadastradas = [
    Bicicleta("Caloi", "Elite Carbon", 2023, "N/A", 1, 2, "Dianteira", "Estudante", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Sim", "Veículo especial", "Veículo particular", "Não", "N/A"),
    Bicicleta("Specialized", "Stumpjumper", 2023, "N/A", 1, 2, "Traseira", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Não", "Veículo de tração", "Veículo particular", "Não", "N/A"),
    Bicicleta("Trek", "Domane", 2023, "N/A", 1, 2, "Dianteira", "Empresário(a)", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Sim", "Veículo especial", "Veículo particular", "Não", "N/A"),
    Bicicleta("Giant", "Anthem", 2023, "N/A", 1, 2, "Traseira", "Aposentado(a)", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Não", "Veículo de tração", "Veículo de competição", "Não", "N/A"),
    Bicicleta("Cannondale", "Synapse", 2023, "N/A", 1, 2, "Dianteira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Sim", "Veículo especial", "Veículo particular", "Não", "N/A"),
    Bicicleta("Scott", "Spark", 2023, "N/A", 1, 2, "Traseira", "Estudante", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Não", "Veículo de tração", "Veículo de competição", "Não", "N/A"),
    Bicicleta("Cervélo", "S-Series", 2023, "N/A", 1, 2, "Dianteira", "Profissional liberal", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Sim", "Veículo especial", "Veículo particular", "Não", "N/A"),
    Bicicleta("Santa Cruz", "Nomad", 2023, "N/A", 1, 2, "Traseira", "Empresário(a)", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Não", "Veículo de tração", "Veículo de competição", "Não", "N/A"),
    Bicicleta("Yeti", "SB130", 2023, "N/A", 1, 2, "Dianteira", "Aposentado(a)", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Sim", "Veículo especial", "Veículo particular", "Não", "N/A"),
    Bicicleta("Pinarello", "Dogma F12", 2023, "N/A", 1, 2, "Traseira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Não", "Veículo de tração", "Veículo particular", "Não", "N/A"),
]
bondes_cadastrados = [
    Bonde("Siemens", "Combino", 2023, "Eletricidade", 150, 4, "Via aérea", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)","Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Bonde("Bombardier", "Flexity Outlook", 2023, "Eletricidade", 180, 4, "Trilhos", "Trabalhador(a) CLT", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Bonde("CAF", "Urbos", 2023, "Eletricidade", 160, 4, "Via aérea", "Trabalhador(a) CLT", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Bonde("Alstom", "Citadis", 2023, "Eletricidade", 140, 4, "Via aérea", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular",  "Sim", "D"),
    Bonde("Skoda", "ForCity", 2023, "Eletricidade", 170, 4, "Via aérea", "Trabalhador(a) CLT", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular",  "Sim", "D"),
    Bonde("Stadler", "Tango", 2023, "Eletricidade", 160, 4, "Via aérea", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo oficial",  "Sim", "D"),
    Bonde("AnsaldoBreda", "Sirio", 2023, "Eletricidade", 150, 4, "Via aérea", "Trabalhador(a) CLT", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo oficial",  "Sim", "D"),
    Bonde("PESA", "Twist", 2023, "Eletricidade", 180, 4, "Via aérea", "Trabalhador(a) CLT", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo oficial",  "Sim", "D"),
    Bonde("CRRC", "FLEXITY 2", 2023, "Eletricidade", 170, 4, "Via aérea", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo oficial",  "Sim", "D"),
    Bonde("CNR", "Variobahn", 2023, "Eletricidade", 160, 4, "Via aérea", "Trabalhador(a) CLT", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo oficial",  "Sim", "D"),
]
caminhonetes_cadastradas = [
    Caminhonete("Toyota", "Hilux", 2023, "Diesel", 5, 2, "4x4", "Empresário(a)", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Ford", "Ranger", 2023, "Diesel", 5, 2, "4x4", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Chevrolet", "S10", 2023, "Diesel", 5, 2, "4x4", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Volkswagen", "Amarok", 2023, "Diesel", 5, 2, "4x4", "Estudante", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Nissan", "Frontier", 2023, "Diesel", 5, 2, "4x4", "Aposentado(a)", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Mitsubishi", "L200 Triton", 2023, "Diesel", 5, 2, "4x4", "Empresário(a)", "Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("RAM", "2500", 2023, "Diesel", 5, 2, "4x4", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Hyundai", "Santa Cruz", 2023, "Diesel", 5, 2, "4x4", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Mercedes-Benz", "X-Class", 2023, "Diesel", 5, 2, "4x4", "Estudante", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de carga", "Veículo particular", "Sim", "D"),
    Caminhonete("Fiat", "Toro", 2023, "Diesel", 5, 2, "4x4", "Aposentado(a)", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de carga", "Veículo particular", "Sim", "D"),
]
onibus_cadastrados = [
    Onibus("Mercedes-Benz", "O500U", 2023, "Diesel", 50, 2, "Traseira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Onibus("Volvo", "B340M", 2023, "Diesel", 40, 2, "Traseira", "Trabalhador(a) CLT", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Onibus("Scania", "K310IA", 2023, "Diesel", 45, 2, "Traseira", "Trabalhador(a) CLT", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Onibus("Marcopolo", "Paradiso 1800 DD", 2023, "Diesel", 60, 3, "Traseira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo oficial", "Sim", "D"),
    Onibus("Neoplan", "Cityliner", 2023, "Diesel", 55, 2, "Traseira", "Trabalhador(a) CLT", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Onibus("Irizar", "i8", 2023, "Diesel", 50, 2, "Traseira", "Trabalhador(a) CLT", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "Sim", "D"),
    Onibus("MAN", "Lions Coach", 2023, "Diesel", 45, 2, "Traseira", "Trabalhador(a) CLT", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo de coleção", "Sim", "D"),
    Onibus("Van Hool", "TX", 2023, "Diesel", 40, 2, "Traseira", "Profissional liberal", "Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo oficial", "Sim", "D"),
    Onibus("Setra", "S 531 DT", 2023, "Diesel", 55, 2, "Traseira", "Profissional liberal", "Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo oficial", "Sim", "D"),
    Onibus("Iveco Bus", "Crossway", 2023, "Diesel", 50, 2, "Traseira", "Profissional liberal", "Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo de coleção", "Sim", "D"),
]
ciclomotores_cadastrados = [
    Ciclomotor("Honda", "Biz 125", 2022, "Gasolina", 1, 2, "Dianteira", "Estudante","Muito ativo, sempre em movimento", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "A"),
    Ciclomotor("Yamaha", "Crypton 115", 2023, "Gasolina", 1, 2, "Dianteira", "Profissional liberal","Moderadamente ativo, com algumas atividades ao ar livre", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "A"),
    Ciclomotor("Suzuki", "Yes 125", 2021, "Gasolina", 1, 2, "Dianteira", "Aposentado(a)","Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo particular", "A"),
    Ciclomotor("Kawasaki", "Z300 ABS", 2022, "Gasolina", 1, 2, "Dianteira", "Trabalhador(a) CLT","Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "A"),
    Ciclomotor("BMW", "G 310 R", 2023, "Gasolina", 1, 2, "Dianteira", "Empresário(a)","Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de passageiros", "Veículo particular", "A"),
    Ciclomotor("Ducati", "Monster 797", 2023, "Gasolina", 1, 2, "Dianteira", "Estudante","Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "A"),
    Ciclomotor("Harley-Davidson", "Iron 883", 2023, "Gasolina", 1, 2, "Dianteira", "Profissional liberal","Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de competição", "Veículo oficial", "A"),
    Ciclomotor("Triumph", "Street Twin", 2023, "Gasolina", 1, 2, "Dianteira", "Empresário(a)","Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de coleção", "Veículo de coleção", "A"),
    Ciclomotor("Aprilia", "RS 660", 2023, "Gasolina", 1, 2, "Dianteira", "Aposentado(a)","Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo de coleção", "A"),
    Ciclomotor("Indian", "Scout Bobber Sixty", 2023, "Gasolina", 1, 2, "Dianteira", "Trabalhador(a) CLT","Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de competição", "Veículo de coleção", "A"),
]
triciclos_cadastrados = [
    Triciclo("Can-Am", "Spyder RT", 2022, "Gasolina", 2, 3, "Traseira", "Estudante","Muito ativo, sempre em movimento", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "B"),
    Triciclo("Harley-Davidson", "Freewheeler", 2023, "Gasolina", 2, 3, "Traseira", "Profissional liberal","Moderadamente ativo, com algumas atividades ao ar livre", "Com frequência (duas a três vezes por mês)", "Veículo de passageiros", "Veículo particular", "B"),
    Triciclo("Polaris", "Slingshot SL", 2021, "Gasolina", 2, 3, "Traseira", "Aposentado(a)","Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo particular", "B"),
    Triciclo("Can-Am", "Ryker Rally Edition", 2022, "Gasolina", 2, 3, "Traseira", "Trabalhador(a) CLT","Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de passageiros", "Veículo particular", "B"),
    Triciclo("Rewaco", "RF1 LT-2", 2023, "Gasolina", 2, 3, "Traseira", "Empresário(a)","Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de passageiros", "Veículo particular", "B"),
    Triciclo("Campagna", "T-Rex 16S", 2023, "Gasolina", 2, 3, "Traseira", "Estudante","Muito ativo, sempre em movimento", "Com frequência (duas a três vezes por mês)", "Veículo de competição", "Veículo particular", "B"),
    Triciclo("Can-Am", "Spyder F3", 2023, "Gasolina", 2, 3, "Traseira", "Profissional liberal","Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de competição", "Veículo oficial", "B"),
    Triciclo("Harley-Davidson", "Tri Glide Ultra", 2023, "Gasolina", 2, 3, "Traseira", "Empresário(a)","Moderadamente ativo, com algumas atividades ao ar livre", "Regularmente (pelo menos uma vez por semana)", "Veículo de coleção", "Veículo de coleção", "B"),
    Triciclo("Morgan", "3 Wheeler", 2023, "Gasolina", 2, 3, "Traseira", "Aposentado(a)","Principalmente tranquilo e urbano", "Ocasionalmente (uma vez por mês)", "Veículo de passageiros", "Veículo de coleção", "B"),
    Triciclo("Campagna", "V13R", 2023, "Gasolina", 2, 3, "Traseira", "Trabalhador(a) CLT","Focado em família e lazer", "Raramente (menos de uma vez por mês)", "Veículo de competição", "Veículo de coleção", "B"),
]



print("*"*15, "Seja bem vindo🧞", "*"*15)
print("*"*5, "Vamos escolher um veículo para você agora!!!!!", "*"*5)
print("*" * 70)
escolha = int(input("Vamos escolher veiculos pra você conforme a sua necessidade! \n\nA seguir você vai escolher a tração, especie, categoria e numero de passageiros para determinar o veiculo ideal! \nDigite 1 - se esta pronto pra continuar ou 2 - se quiser sair! \nESCOLHA AQUI>>>"))
if escolha == 1:
    escolha_profissao = input("\nQual sua profissão?\n1 - Estudante\n2 - Profissional liberal\n3 - Empresário(a)\n4 - Trabalhador(a) CLT\n5 - Aposentado(a)\nESCOLHA AQUI>>> ")
    if escolha_profissao not in profissao_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()

    escolha_estilo_vida = input("\nComo é seu estilo de vida?\n1 - Muito ativo, sempre em movimento\n2 - Moderadamente ativo, com algumas atividades ao ar livre\n3 - Principalmente tranquilo e urbano\n4 - Focado em família e lazer\nESCOLHA AQUI>>> ")
    if escolha_estilo_vida not in estilo_vida_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()

    escolha_frequencia_uso = input("\nQual a frequencia de uso do veiculo?\n1 - Regularmente (pelo menos uma vez por semana)\n2 - Com frequência (duas a três vezes por mês)\n3 - Ocasionalmente (uma vez por mês)\n4 - Raramente (menos de uma vez por mês)\nESCOLHA AQUI>>> ")
    if escolha_frequencia_uso not in frequencia_uso_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()

    escolha_tracao = input("\nEscolha a tração do veículo: \n1. Dianteira \n2. 4x4 \n3. Traseira \n4. Semi Reboque \n5. Via aérea \nESCOLHA AQUI>>> ")
    if escolha_tracao not in tracao_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()

    escolha_especie = input("\nEscolha a espécie do veículo: \n1. Veículo de passageiros \n2. Veículo de carga \n3. Veículo misto \n4. Veículo de competição \n5. Veículo de tração \n6. Veículo especial \n7. Veículo de coleção\nESCOLHA AQUI>>> ")
    if escolha_especie not in especie_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()

    escolha_categoria = input("\nEscolha a categoria do veículo: \n1. Veículo particular \n2. Veículo oficial \n3. Veículo de representação diplomática \n4. Veículo de coleção \nESCOLHA AQUI>>> ")
    if escolha_categoria not in categoria_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()

    escolha_passageiros = input("\nEscolha capacidade de passageiros do veículo: \n1. 2 passageiros ou menos \n2. entre 3 e 5 passageiros \n3. mais de 5 passageiros \nESCOLHA AQUI>>> ")
    if escolha_passageiros not in escolha_passageiros_opcoes:
        print("Opção inválida. Programa encerrado.")
        exit()


    resultados = []

    for veiculo in carros_cadastrados + motos_cadastradas + caminhoes_cadastrados + bicicletas_cadastradas + bondes_cadastrados + caminhonetes_cadastradas + onibus_cadastrados + ciclomotores_cadastrados + triciclos_cadastrados:
        if (veiculo.tracao == tracao_opcoes[escolha_tracao] and
            veiculo.profissao  == profissao_opcoes[escolha_profissao] and
            veiculo.estilo_vida == estilo_vida_opcoes[escolha_estilo_vida] and
            veiculo.frequencia_uso == frequencia_uso_opcoes[escolha_frequencia_uso] and
            veiculo.especie == especie_opcoes[escolha_especie] and
            veiculo.categoria == categoria_opcoes[escolha_categoria]):
            
            if escolha_passageiros == "1":
                if veiculo.passageiros <= 2:
                    resultados.append(veiculo)
            elif escolha_passageiros == "2":
                if veiculo.passageiros > 2 and veiculo.passageiros <= 5:
                    resultados.append(veiculo)
            elif escolha_passageiros == "3":
                if veiculo.passageiros > 5:
                    resultados.append(veiculo)


    if resultados:
        print("\nVeículos disponíveis que atendem sua busca:")
        for veiculo in resultados:
            if isinstance(veiculo, Carro):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao} \nCarroceria: {veiculo.carroceria}")
            elif isinstance(veiculo, Moto):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Bicicleta):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Caminhao):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Bonde):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Caminhonete):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Onibus):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Ciclomotor):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            elif isinstance(veiculo, Triciclo):
                print(f"\nMarca: {veiculo.marca} \nModelo: {veiculo.modelo} \nAno: {veiculo.ano} \nCombustível: {veiculo.combustivel} \nPassageiros: {veiculo.passageiros} \nTração: {veiculo.tracao} \nCategoria: {veiculo.categoria} \nHabilitação Necessária: {veiculo.tipo_habilitacao}")
            
    else:   
        print("\nNão há veículos disponíveis que correspondem aos critérios selecionados.")
elif escolha == 2 :
    print("TUDO BEM, SAINDO DO PROGRAMAA.....")
else:
    print("COMO NÃO DIGITOU NEM 1 E NEM 2, PROGRAMA SERA FECHADO TAMBEM!")
