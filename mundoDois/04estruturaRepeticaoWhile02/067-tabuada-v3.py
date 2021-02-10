# EXERCÍCIO 067 - TABUADA V3.0

# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# SOLUÇÃO

print('Vamos brincar de tabuada?\n'
      'Se quiser parar, digite um número negativo')
while True:
    num = int(input('Digite um número para ver a tabuada: '))
    if num < 0:
        break
    for c in range(11):
        print(f'{num} X {c:2} = {num * c:2}')
print('Brrr!! Não opero com negativos! o.O \nPrograma finalizado!!')
