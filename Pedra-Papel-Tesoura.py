from random import randint, choice
from time import sleep

print('-=' * 20)
print('    Seja Bem-Vindo(a) ao jogo de:\n       Pedra, Papel, Tesoura!')
print('-=' * 20)

opcoes = ("Pedra", "Papel", "Tesoura")
count = 1
vitorias_jogador = 0
vitorias_maquina = 0
modo_desbloqueado = False

# Função
def jogar_melhor_de_3():
    dificuldade = input('Escolha a dificuldade: [F]ácil, [M]édio, [D]ifícil\nR-> ').strip().upper()
    rodadas_m3 = 1
    vitorias_j = 0
    vitorias_m = 0

    while rodadas_m3 <= 3:
        print(f'-=-=-=- MELHOR DE 3 - RODADA {rodadas_m3} -=-=-=-')
        jogada_user_m3 = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\nR-> '))

        if dificuldade == 'F':
            jogada_maquina_m3 = randint(0, 2)
        elif dificuldade == 'M':
            jogada_maquina_m3 = choice([0, 0, 1, 1, 2])
        elif dificuldade == 'D':
            jogada_maquina_m3 = (jogada_user_m3 + 1) % 3
        else:
            jogada_maquina_m3 = randint(0, 2)

        print('_-' * 15)
        print('JO  ✌️')
        sleep(1)
        print('KEN ✋')
        sleep(1)
        print('PÔ! ✊')
        sleep(1)
        print('_-' * 15)

        print(f'O computador jogou: {opcoes[jogada_maquina_m3]}')
        print(f'Você jogou: {opcoes[jogada_user_m3]}')

        if jogada_user_m3 == jogada_maquina_m3:
            print('EMPATE!')
        elif (jogada_user_m3 == 0 and jogada_maquina_m3 == 2) or \
             (jogada_user_m3 == 1 and jogada_maquina_m3 == 0) or \
             (jogada_user_m3 == 2 and jogada_maquina_m3 == 1):
            print('Você venceu esta rodada!')
            vitorias_j += 1
        else:
            print('A máquina venceu esta rodada!')
            vitorias_m += 1

        rodadas_m3 += 1

    print('-=' * 20)
    if vitorias_j > vitorias_m:
        print('VOCÊ venceu o MELHOR DE 3!')
    elif vitorias_j < vitorias_m:
        print('O COMPUTADOR venceu o MELHOR DE 3!')
    else:
        print('Foi um EMPATE no MELHOR DE 3!')
    print('-=' * 20)

# Loop principal do jogo
while True:
    print(f'------- RODADA N{count} ----------')
    jogada_user = int(input('[0] Pedra\n[1] Papel\n[2] Tesoura\n[3] Sair \nR-> '))

    if jogada_user == 3:
        print('Saindo...')
        break
    elif jogada_user not in [0, 1, 2]:
        print('Jogada inválida! Tente novamente.')
        continue

    jogada_maquina = randint(0, 2)

    print('_-' * 15)
    print('JO  ✊')
    sleep(1)
    print('KEN ✋')
    sleep(1)
    print('PÔ! ✌️')
    sleep(1)
    print('_-' * 15)

    print(f'O computador jogou: {opcoes[jogada_maquina]}')
    print(f'Você jogou: {opcoes[jogada_user]}')

    if jogada_user == jogada_maquina:
        print('EMPATE!')
    elif (jogada_user == 0 and jogada_maquina == 2) or \
         (jogada_user == 1 and jogada_maquina == 0) or \
         (jogada_user == 2 and jogada_maquina == 1):
        print('Você venceu!')
        vitorias_jogador += 1
    else:
        print('A máquina venceu!')
        vitorias_maquina += 1

    if vitorias_jogador == 1 and not modo_desbloqueado:
        print('*-_-*-_-*-_- OPA! ദ്ദി •⩊• ) *-_-*-_-_-*')
        print('Parabéns! Você desbloqueou o modo: MELHOR DE 3!')
        modo_desbloqueado = True

    count += 1

    # Escolhendo o próximo passo
    if modo_desbloqueado:
        while True:
            print('-=-=-=- Escolha o Modo de Jogo! -=-=-=-')
            print('[1] Continuar jogo normal')
            print('[2] Jogar MELHOR DE 3')
            print('[3] Sair do jogo')
            escolha = input('R-> ')
            if escolha == '1':
                break
            elif escolha == '2':
                jogar_melhor_de_3()
                break
            elif escolha == '3':
                print('-=' * 20)
                print('-=-=-=-=-=-=- PLACAR -=-=-=-=-=-=-')
                print(f'Vitórias do jogador: {vitorias_jogador}')
                print(f'Vitórias da máquina: {vitorias_maquina}')
                print('-=' * 20)
                print('Obrigada por jogar! =)')
                exit()
            else:
                print('Opção inválida, tente novamente.')
    else:
        continuar = input('--- Deseja continuar jogando? [S/N] ---\nR-> ').strip().upper()
        if continuar != 'S':
            break

# Exibe placar final
print('-=' * 20)
print('-=-=-=-=-=-=- PLACAR FINAL -=-=-=-=-=-=-')
print(f'Vitórias do jogador: {vitorias_jogador}')
print(f'Vitórias da máquina: {vitorias_maquina}')
print('-=' * 20)
print('Obrigada por jogar! =)')
