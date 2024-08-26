from avaliacoes import Boletim
import os

notas = Boletim()

def adicionar_notas():
    notas.adicionar_nota(0.4)
    notas.adicionar_nota(0.3)
    notas.adicionar_nota(0.3)
    notas.nota_complementar()

def exibir_resultado():
    notas.ajustar_lista()
    notas.exibir_lista()

def recomeçar():
    try:
        usuario = int(input('Deseja calcular novamente?\n 1 - SIM\n 2 - NÃO\n'))
        if usuario == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        elif usuario == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            return False
        else:
            print('Digite um valor valido!')
            return recomeçar()
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Digite um valor valido!')
        return recomeçar()


def main():
    executar = True
    while executar:
        adicionar_notas()
        exibir_resultado()
        executar = recomeçar()

main()