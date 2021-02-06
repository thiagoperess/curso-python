# EXERCICIO 044 - GERENCIADOR DE PAGAMENTOS

# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desconto;
# Em até 2x no cartão: preço formal;
# Em 3x ou mais no cartão: 20% de juros.

# SOLUÇÃO

print('='*10, 'LOJAS THIAGUIDES', '='*10,)
preco = float(input('Preço das compras: '))

print('''FORMAS DE PAGAMENTO:
[1] À vista (dinheiro/cheque)
[2] À vista (cartão)
[3] 2x no cartão
[4] 3x ou mais no cartão''')

pagamento = (float(input('Opção de pagamento: ')))

if pagamento == 1:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} reais.'.format(preco, preco - (preco * 10 / 100)))
elif pagamento == 2:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} reais.'.format(preco, preco - (preco * 5 / 100)))
elif pagamento == 3:
    print('O valor a ser pago é de R$ {:.2f} reais.'.format(preco))
elif pagamento == 4:
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} reais.'.format(preco, preco + (preco * 20 / 100)))
else:
    print('Digite uma opção de pagamento válida!')
