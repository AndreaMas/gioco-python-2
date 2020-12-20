class Arma:
    def __init__(self, nome, usura, danno):
        self.nome = nome
        self.usura = usura
        self.danno = danno

    def info(self):
        print(f"Arma:\n"
              f" nome: {self.nome}\n"
              f" usura: {self.usura}\n"
              f" danno: {self.danno}\n")


