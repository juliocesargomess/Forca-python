import random # Importando módulo para sortear palavras.

import desenho

listaPalavras = ['CARRO', 'CASA', 'PRAIA', 'TELEVISAO', 'COMPUTADOR']



def selectRandom(palavras): # Função que sorteia a palavra.
    return random.choice(palavras)

def imprimePalavra(letraTeste): # Método para testar se a letra está na palavra.
    print("A Palavra é:")
    for letraTeste in palavra:
        if letraTeste in letras_digitadas: # Condicional, se a lelra estiver no conjunto de letras digitadas ela é printada.
            print(f'{letraTeste}', end='')
        else:   # Se não, imprime um '-' ao invés da letra.
            print('-', end='')


palavra = selectRandom(listaPalavras) # Chamando a função (selectRandom) para sortear a palavra.
letras_palavra = set(palavra) # Definindo variáveis.
letras_digitadas = set()
letraCerta = '0'
acerto = 1
erros = 0
desenho.forcaVazia() # Chamada desenho da forca

print('A palavra é: ', end='') #Inicio do programa, imprimindo ' - - - - '.
for letra in palavra:
    print('-',end='')
print('')

while erros < 6: # Laço de repetição, enquanto não tiver 6 erros, o programa continua rodando.
    letraUser = input('Digite uma letra: ').upper()
    print('')
    if len(letraUser) > 1 or letraUser in letras_digitadas or letraUser == '': # Condicional, se tiver mais de 1 letra ou for repetida, exibe essa mensagem.
        print('\nLETRA INVÁLIDA, DIGITE OUTRA LETRA:')
    else:
        letras_digitadas.add(letraUser) # Adiciona as letras digitadas ao conjunto (letras_digitadas).
        if letraUser in letras_palavra:
            letraCerta = letraUser # DEFINI ESSA VARIÁVEL PRA PODER COMPARAR A PRIMEIRA LETRA ERRADA.
            imprimePalavra(letra)  # Chamada da Método imprimePalavra.
            acerto += 1 # Contador de acertos.
            if len(palavra) == acerto: # Condicional, se o contador for igual ao tamanho da palavra, o programa encerra.
             print("\nVOCÊ GANHOU")
             break

        else:
            erros += 1 # Contador de erros.
            desenho.testeErros(erros) # Método para mudar o desenho da forca
            print(f'Erro {erros} de 6. Tente novamente!\n')
            if erros == 6: # Condicional, se o contador chegar a 6 o programa encerra.
                print('VOCÊ PERDEU!!!!')
                break
            imprimePalavra(letraCerta)
    print('\nLetras já digitadas: ', letras_digitadas, '\n')
input('')