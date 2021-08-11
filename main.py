from random import randint # randint é uma função que retorna um número inteiro aleatório dentro de um intervalo

class Jogo: # cria a classe "Jogo"
    def __init__(self, palpite):
        self.__palpite = palpite # palpite do usuário
        self.__numero_sorteado = randint(1, 100) # número sorteado
        self.__resultado = self.__compara() # resultado do jogo (se ganhou ou perdeu)
    
    # função que retorna uma string colorida de acordo com o resultado do jogo
    def __compara(self):
        if self.__palpite == self.__numero_sorteado: # verifica se ganhou
            return '\033[34mParabéns, você acertou !\033[m'
        else: # verifica se perdeu
            return f'\033[31mVocê errou! O número sorteado era o {self.__numero_sorteado}\033[m'
    

    @property
    def resultado(self): # getter que retorna o resultado do jogo
        return self.__resultado


if __name__ == '__main__': # verifica se o contexto de execução do módulo está no escopo principal
    
    while True: # looping infinito
        try:
            palpite = int(input('Dê o seu palpite: ')) # atribuição da variável "palpite" à entrada de dados

            if palpite > 100 or palpite < 1: # verfica se o palpite está dentro do intervalo de 1 a 100
                raise ValueError('Digite um número maior ou igual 1 ou menor ou igual a 100 !') # se não estiver o programa irá lançar uma exceção notificando o usuário do erro

        except Exception as E: # intercepta as exceções 
            print(f'\033[31m{E}\033[m') # imprime a mensagem da exceçãõ na cor vermelha
            continue # volta para a atribuição da variável

        else: # tratados os erros, o programa irá criar um objeto do tipo Jogo através da atribução à variável "jogo"
            jogo = Jogo(palpite)
            break # encerra o looping

    print(jogo.resultado) # mostra o resultado
    
