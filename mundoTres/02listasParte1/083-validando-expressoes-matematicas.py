# EXERCÍCIO 083 - VALIDANDO EXPRESSÕES MATEMÁTICAS

# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.

# SOLUÇÃO

parentheses = []
expression = str(input('Digite a expressão: '))
for symbol in expression:
    if symbol == '(':
        parentheses.append('(')
    elif symbol == ')':
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(')')
            break
if len(parentheses) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está inválida!')
