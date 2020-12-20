from arma import Arma


class Personaggio:
    def __init__(self, nome, vita):
        self.nome = nome
        self.vita = vita
        self.arma = Arma("Vuoto", 0, 0)
        self.zaino = []

    def stampa_zaino(self):
        for i in range(len(self.zaino)):
            print(f"  {self.zaino[i].nome}")

    def info(self):
        print(f"Personaggio:\n"
              f" nome: {self.nome}\n"
              f" vita: {self.vita}\n"
              f" arma: {self.arma.nome}\n"
              f" zaino: ")
        self.stampa_zaino()
