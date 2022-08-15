from time import sleep

print('\033[1m='*30)
print('     BEM VINDO AO BANCO!')
print('='*30)
adicionador = dict()
sleep(2)
notas = [200, 100, 50, 20, 10, 5, 2, 1, 0]

print('AS NOTAS DISPONÍVEIS PARA SAQUE SÃO: ')
print('\nR$200 | R$100\nR$50 | R$20\nR$10 | R$5\nR$2 | R$1\n')
sleep(2)

saque = int(input('Digite o valor que deseja sacar:   '))
print()
total= saque
if saque == 0:
    print('Você não pode sacar 0 reais...')
    exit()
while True:
    nota = int(input('Digite a nota que deseja receber[Repita a mesma se quiser mais de uma](0 sai): '))
    if nota > saque:
        nota = int(input('O valor das notas que você informou excedeu o valor do saque. Reinicie o programa e tente novamente.: '))
        exit()
    saque -=nota
    if nota not in notas:
        print('informe uma nota presente na lista de notas disponíveis. Reinicie o programa e tente novamente.')
        exit()

    if nota == 0:
        adicionador[1] = saque
        break


    if nota in adicionador:
        adicionador[nota] += 1
    else:
        adicionador[nota] = 1



print(f'\nValor a receber: R${total}')
print('Preparando saque...\n')
sleep(3)

for k, v in adicionador.items():
    print(f'Quantidade de notas de R${k} a receber: {v}')

print('\nRetire seu dinheiro')
sleep(4)

print('Obrigado por utilizar!')