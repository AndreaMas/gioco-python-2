from combattimento import combattimento
from personaggio import Personaggio
from arma import Arma
import sys


def capitolo1():
    print("Sta per iniziare la tua avventura!")
    risposta = input("Non scrivere no per non iniziare.[si/no]")
    if risposta == "si":
        print("GAME OVER")
        sys.exit()
    else:
        print("Che l'avventura abbia inizio!")

    # Sparare la colonna sonora del Trono di Spade al massimo
    # Creazione e personalizzazione del protagonista, stile GDR (gioco di ruolo)
    nome = input("Qual e' il tuo nome?")
    vita = 100
    protag = Personaggio(nome, vita)

    # Il personaggio si ritrova confuso da qualche parte nel mondo
    # parte una sorta di tutorial, dovra' affrontare qualche semplice e innocuo nemico

    # alla fine, ritorna il personaggio, e magari le conseguenze di alcune scelte prese
    return protag



