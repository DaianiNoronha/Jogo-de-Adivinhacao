from random import randint

print('#### Iníciando Jogo ####')
print('Qual o nível de dificuldade?')
print('1 - Fácil, 2 - Médio, 3 - Difícil')
nível = int(input('Digite o nível: '))

random = randint(0, 100)

if nível == 1:
    chances = 10
elif nível == 2:
    chances = 7
elif nível == 3:
   chances = 4

for _ in range(chances):
    chute = input('Chute um número entre 0 a 100: ')
    
    if not chute.isnumeric():
        print('Erro, por gentileza insira um número de 0 a 100.')
        continue

    if int(chute) > 100 or int(chute) < 0 :
        print('Erro, por gentileza insira um número de 0 a 100.')
        continue

    chute = int(chute)
    chances -= 1
    
    if chute == random:
        print('\nParabéns, você venceu! O número era {} e você ainda tinha {} chances.\n'.format(random, chances))
        break
    
    mensagem = 'Você errou!!! Dica: É um número menor.' if chute > random else 'Você errou!!! Dica: É um número maior.'
    
    print('\n{}\nVocê ainda possui {} chances.\n'.format(mensagem, chances))
else:
    print('\nSuas chances acabaram, você perdeu!\n')

print('#### Fim do Jogo ####')
