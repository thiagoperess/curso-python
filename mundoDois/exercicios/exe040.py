# EXERCICIO 040

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você possui uma média {} e está \033[31mREPROVADO!'.format(media))
elif 5 <= media <= 6.9:
    print('Você possui uma média {} e está de \033[33mRECUPERAÇÃO!'.format(media))
else:
    print('Você possui uma média {} e está \033[32mAPROVADO!\033[m PARABÉNS!!'.format(media))
