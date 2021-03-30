# EXERCÍCIO 093 - CADASTRO DE JOGADOR DE FUTEBOL

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa
# vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

# SOLUÇÃO

soccerMatches = list()
player = dict()
player['nome'] = str(input('Qual o nome do jogador? '))
total = int(input(f'Quantas partidas {player["nome"]} jogou? '))
for c in range(0, total):
    soccerMatches.append(int(input(f'Quantos gols na {c+1}º partida? ')))
player['goals'] = soccerMatches[:]
player['total'] = sum(player['goals'])
print('-='*25)
print(player)
print('-='*25)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*25)
print(f'O jogador {player["nome"]} jogou {len(soccerMatches)} partidas')
for i, v in enumerate(player['goals']):
    print(f'=> Na {i+1}ª partida fez {v} gols.')
print(f'Foi um total de {player["total"]} gols.')
