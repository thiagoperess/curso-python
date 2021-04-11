# EXERCÍCIO 105 - ANALISANDO E GERANDO DICIONÁRIOS

# Faça um programa que tenha uma função notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

# SOLUÇÃO

def notes(*note, situation=False):
    """
    -> Função para analisar notas e situação do aluno.
    :param note: uma ou mais notas dos alunos. Aceita notas ilimitadas.
    :param situation: valor opcional. Indica se de ou não adicionar a situação.
    :return: dicionário com informações sobre a situação da turma.
    """
    ans = dict()
    ans['total'] = len(note)
    ans['major'] = max(note)
    ans['minor'] = min(note)
    ans['mean'] = sum(note) / len(note)
    if ans['mean'] >= 7:
        ans['situation'] = 'BOA'
    elif ans['mean'] >= 5:
        ans['situation'] = 'RAZOÁVEL'
    else:
        ans['situation'] = 'RUIM'
    return ans


answer = notes(9.5, 8.5, 9, 8.5, situation=True)
print(answer)
help(notes)

