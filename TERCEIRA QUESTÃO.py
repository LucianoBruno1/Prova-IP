from time import sleep
print('\033[1m='*30)
print('    ZERO OU UM AMERICANO')
print('='*30)
print('começando...')
sleep(2)
dedos = list()
ganhador = 0
total = 0
cont = 0
contganhador = 0
pessoas = int(input('Informe o número de participantes (número maior do que 1): '))
participantes = list()

if pessoas == 1:
    print('Quantidadede participantes inválida. Reinicie o programa e tente novamente.')
    exit()

if pessoas <=0:
    print('Quantidadede participantes inválida. Reinicie o programa e tente novamente.')
    exit()


while cont <= pessoas - 1:
    cont+=1
    numeros = int(input(f'informe o número de dedos do participante {cont}: '))
    jogadores = [f'participante {cont} = {numeros}',]
    dedos.append(numeros)
    total+=numeros
    participantes.append(jogadores)


print(f'\nO total é: {total}')


while total != 0:
    total-=1
    contganhador+=1
    if contganhador > len(participantes):
        contganhador=0
        contganhador+=1



dedos = dedos*total
print(f'O vencedor foi o participante {contganhador}')