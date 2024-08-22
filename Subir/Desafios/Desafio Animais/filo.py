from reino import Reino
class Filo (Reino):
    def __init__(self, nome, reino, filo):
        super().__init__(nome, reino)
        self.filo = filo