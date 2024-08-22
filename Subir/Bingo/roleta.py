from random import*
class Roleta:
    def __init__(self):
        self.numero_roleta = set() 

    def confere(self):
        while True:
            number = randint(1, 75)
            if number not in self.numero_roleta:
                self.numero_roleta.add(number)
                return number

    def reset(self):
        self.numero_roleta = set()