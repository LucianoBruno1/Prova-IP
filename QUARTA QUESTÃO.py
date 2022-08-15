from time import sleep
import statistics
cont = 0
soma = 0
contacimadamedia = 0
lista = []
dp = 0
print()
print('\033[1m='*38)
print('CADERNETA DE INTRODUÇÃO À PROGRAMAÇÃO')
print('='*38)
print('\n OBS: Se digitar uma nota maior que dez, o programa será encerrado.')
print()
sleep(2)
while True:
    cont+=1
    notas = float(input('\033[1mDigite as notas finais dos alunos na disciplina de Introdução a programação(digite numero negativo para parar): '))
    soma+= notas
    lista.append(notas)
    media = statistics.mean(lista)

    if notas > 10:
        cont-=1
        print('\n\033[31mDigite uma nota válida. Reinicie o programa e tente novamente.')
        exit()
        break


    if notas < 0:
        lista.pop()
        cont-=1
        soma-=notas
        print('\nCalculando requisitos solicitados...\n')
        sleep(3)
        break


for acimadamedia in lista:
    if acimadamedia > media:
        contacimadamedia+=1

dp = statistics.stdev(lista) #desvio padrão
media = statistics.mean(lista)

print(f'\033[33mA quantidade de notas lidas foi: {cont}')
print(f'Notas na ordem em que foram informadas:  {lista}')
print(f'A soma é: {soma:.2f}')
print(f'A média é: {media:.2f}')
print(f'A quantidade de notas acima da média calculada é: {contacimadamedia}')
print(f'O desvio padrão é: {dp:.2f}')