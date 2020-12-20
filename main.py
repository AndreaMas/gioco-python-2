import sys
from personaggio import Personaggio
from arma import Arma


def main():
    protagonista = Personaggio("Arturocassoduro",20)
    protagonista.info()

    spada = Arma("spada", 10, 10)
    spadone = Arma("spadone", 100, 100)
    spadina = Arma("spadina", 1, 1)
    spada.info()

    protagonista.zaino.append(spada)
    protagonista.zaino.append(spadone)
    protagonista.zaino.append(spadina)
    protagonista.info()

    protagonista.arma = spada

    nemico = Personaggio("Blanz", 13)
    nemico.arma = spadina
    nemico.info()



if __name__ == "__main__":
    main()
