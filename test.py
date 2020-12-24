from combattimento import combattimento
from personaggio import Personaggio
from arma import Arma


def test():
    protagonista = Personaggio("Artur", 20)
    nemico = Personaggio("Bla", 13)

    spada = Arma("spada", 10, 10)
    spadone = Arma("spadone", 100, 100)
    spadina = Arma("spadina", 1, 1)

    protagonista.zaino.append(spada)

    protagonista.arma = spada
    nemico.arma = spadina

    # protagonista.info()
    # nemico.info()

    protagonista, nemico = combattimento(protagonista, nemico)
