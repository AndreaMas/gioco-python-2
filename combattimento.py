from random import getrandbits


def combattimento(pers1, pers2):
    print(f"Prima dell'attacco\n"
          f"Vita di {pers1.nome} = {pers1.vita}\n"
          f"Vita di {pers2.nome} = {pers2.vita}\n")
    pers1.vita = pers1.vita - pers2.arma.danno
    pers2.vita = pers2.vita - pers1.arma.danno
    print(f"Dopo l'attacco\n"
          f"Vita di {pers1.nome} = {pers1.vita}\n"
          f"Vita di {pers2.nome} = {pers2.vita}")

    return pers1, pers2
