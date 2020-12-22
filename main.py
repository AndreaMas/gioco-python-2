import sys
from personaggio import Personaggio
from arma import Arma
from combattimento import combattimento


def main():
    protagonista = Personaggio("Arturocassoduro", 20)
    nemico = Personaggio("Blanz", 13)

    spada = Arma("spada", 10, 10)
    spadone = Arma("spadone", 100, 100)
    spadina = Arma("spadina", 1, 1)

    protagonista.zaino.append(spada)

    protagonista.arma = spada
    nemico.arma = spadina

    # protagonista.info()
    # nemico.info()

    protagonista, nemico = combattimento(protagonista, nemico)


if __name__ == "__main__":
    main()
