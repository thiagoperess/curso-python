# EXERCICIO 006

# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada:

# SOLUÇÃO:

R = int(input("Digite um número: "))
d = R * 2
t = R * 3
qd = R ** (1/2)
print("O dobro de {} é {},\no triplo de {} é {},\ne a raiz quadrada de {} é {}".format(R, d, R, t, R, qd))
