class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.turno = 'branco'

    def imprimir_tabuleiro(self):
        print("  a b c d e f g h")
        print(" +-----------------+")
        for i in range(8):
            print(f"{8 - i}|" + " ".join(self.tabuleiro[i]) + "|")
        print(" +-----------------+")
    
    def mover_peca(self, origem, destino):
        # Converter a coordenada da forma "e2" para (7, 4)
        col_origem = ord(origem[0]) - ord('a')
        linha_origem = 8 - int(origem[1])
        
        col_destino = ord(destino[0]) - ord('a')
        linha_destino = 8 - int(destino[1])
        
        # Movimenta a peça na matriz do tabuleiro
        self.tabuleiro[linha_destino][col_destino] = self.tabuleiro[linha_origem][col_origem]
        self.tabuleiro[linha_origem][col_origem] = ' '

    def jogar(self):
        while True:
            self.imprimir_tabuleiro()
            
            if self.turno == 'branco':
                print("\nTurno das brancas")
            else:
                print("\nTurno das pretas")
            
            origem = input("Escolha a casa de origem (por exemplo, 'e2'): ")
            destino = input("Escolha a casa de destino (por exemplo, 'e4'): ")
            
            self.mover_peca(origem, destino)
            
            # Alternar o turno
            if self.turno == 'branco':
                self.turno = 'preto'
            else:
                self.turno = 'branco'

if __name__ == "__main__":
    jogo = Tabuleiro()
    jogo.jogar()