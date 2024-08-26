import os


class Boletim:
    def __init__(self):
        self.nota = []

    def adicionar_nota(self, peso):
        try:
            nota = int(input(f'Digite a nota: ')) * peso
            self.nota.append(nota)
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Digite um valor valido!')
            self.adicionar_nota(peso)

    def nota_complementar(self):
        try:
            complementar = int(input('Digite a nota complementar: '))
            if self.nota[0] < complementar * 0.4:
                self.nota[0] = complementar * 0.4  
            elif self.nota[1] < complementar * 0.3:
                self.nota[1] = complementar * 0.3  
            elif self.nota[2] < complementar * 0.3:
                self.nota[2] = complementar * 0.3
        except ValueError:
             os.system('cls' if os.name == 'nt' else 'clear')
             print('Digite um valor valido!')
             self.nota_complementar()


    def ajustar_lista(self):
        self.nota.sort()

    def exibir_lista(self):
        if sum(self.nota) > 60:
            print(f'Com as notas de {self.nota[0]: .0f},{self.nota[1]: .0f} e{self.nota[2]: .0f} O aluno está aprovado com resultado final de {sum(self.nota): .0f}')
        else:
            print('Reprovado')
