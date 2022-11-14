import random
nc=random.randint(0,10)
print('Ola, pensei em um número, você consegue adivinhar?')
np=int(input('digite aqui um número de 1 a 10: '))
tent=0
while nc!=np:
    tent+=1
    np=(int(input('digite aqui novamente: ')))
print('parabéns, voce acertou depois de {} tentativas'.format(tent))