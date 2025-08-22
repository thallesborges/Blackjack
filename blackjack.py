import random, os, platform, time, sys
from escolha_opcoes import escolher_opcao

def limpar_tela():
    if platform.system == 'Windows':
        os.system('clear')
    else:
        os.system('cls')

def saldo():
    with open('saldo.txt', 'r') as arq:
        saldo = arq.read()
    
    return float(saldo)

def dar_carta_jogador():
    carta = baralho.pop(0)
    cj.append(carta)

    if carta in ['J', 'Q', 'K']:
        v_cj.append(10)
    elif carta in ['A']:
        v_cj.append(11)
    else:
        v_cj.append(carta)

    if 'A' in cj and sum(v_cj) > 21:
        for i in range(len(cj)):
            if v_cj[i] == 11:
                v_cj[i] = 1
        
def dar_carta_dealer():
    carta = baralho.pop(0)
    cd.append(carta)

    if carta in ['J', 'Q', 'K']:
        v_cd.append(10)
    elif carta in ['A']:
        v_cd.append(11)
    else:
        v_cd.append(carta)
  
    if 'A' in cd and sum(v_cd) > 21:
        for i in range(len(cd)):
            if v_cd[i] == 11:
                v_cd[i] = 1

def entregar_cartas_iniciais():
    for _ in range(2):
        dar_carta_jogador()
        dar_carta_dealer()

def dealer_possui_as_inicial():
    print('♠ Dealer possui ás inicial ♠')
    time.sleep(1)

    if valor_aposta/2 <= saldo():
        print('♣ Deseja fazer seguro?')
        print('1. Sim')
        print('2. Não')
        opcao = escolher_opcao([1, 2])
    else:
        time.sleep(1)
        print('♠ Você não possui saldo suficiente para fazer seguro ♠')
        
        if sum(v_cd) == 21:
            time.sleep(1)
            print('♠ Dealer possui Blackjack ♠')
            time.sleep(1)
            print('== ♦ Dealer ganhou a partida ♦ ==')
            print(f'= ♦ Você perdeu: R${valor_aposta:.2f} ♦ =')
            remover_saldo(valor_aposta)
            time.sleep(1)
            jogar_novamente()

    if opcao == 1:
        print(f'♦ Seguro: R${valor_aposta/2:.2f}')
        if sum(v_cd) == 21:
            time.sleep(1)
            print('♠ Dealer possui Blackjack ♠')
            time.sleep(1)
            print('= ♦ Valor da aposta devolvido ao Saldo ♦ =')
            time.sleep(1)
            jogar_novamente()
        else:
            print('♠ Dealer não possui Blackjack ♠')
            remover_saldo(valor_aposta/2)

    elif opcao == 2 and sum(v_cd) == 21:
        time.sleep(1)
        print('♠ Dealer possui Blackjack ♠')
        time.sleep(1)
        print('== ♦ Dealer ganhou a partida ♦ ==')
        print(f'= ♦ Você perdeu: R${valor_aposta:.2f} ♦ =')
        remover_saldo(valor_aposta)
        time.sleep(1)
        jogar_novamente()

    else:
        time.sleep(1)
        print('♠ Dealer não possui Blackjack ♠')

def iniciar_rodada():
    global baralho, baralhoCompleto

    time.sleep(2)
    limpar_tela()

    print('== ♠ Blackjack ♠ ==')
    
    if len(baralho) <= len(baralhoCompleto) // 2:
        print('= ♣ Estamos reembaralhando as cartas, aguarde um instante ♣ =')
        baralho = baralhoCompleto.copy()
        random.shuffle(baralho)
        time.sleep(3)
    entregar_cartas_iniciais()
    
    if cd[0] == 'A':
        dealer_possui_as_inicial()
        time.sleep(2)

    print(f'♦ Dealer -> Carta aberta: {cd[0]}')
    print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cj)} -> {sum(v_cj)}')

    if sum(v_cj) == 21:
        print("= ♠ Você possui Blackjack Inicial ♠ ")
        time.sleep(1.25)
        print(f'♦ Cartas do Dealer {', '.join(str(carta) for carta in cd)} -> {sum(v_cd)}')
        if sum(v_cd) != 21:
            print('== ♠ Você ganhou com Blackjack Inicial ♠ ==')
            print(f'♦ Aposta ganha: R${valor_aposta*2.5}')
            adicionar_saldo(valor_aposta*1.5)
            jogar_novamente()
        else:
            print('♦ Dealer possui Blackjack ♦')
            print('== Empate! Valor da aposta devolvido.')
            jogar_novamente()
    else:
        menu_jogavel()

def adicionar_saldo(quantidade_dinheiro):
    novo_saldo = saldo() + quantidade_dinheiro
    with open('saldo.txt', 'w') as arq:
        arq.write(str(novo_saldo))

def remover_saldo(quantidade_dinheiro):
    novo_saldo = saldo() - quantidade_dinheiro
    with open('saldo.txt', 'w') as arq:
        arq.write(str(novo_saldo))

def menu_jogavel():

    while sum(v_cj) < 21:
        opcoes_menu = ['1. Pedir', '2. Parar']
        
        if len(cj) == 2 and valor_aposta*2 <= saldo():
            opcoes_menu.append('3. Dobrar')
            if cj[0] == cj[1]:
                opcoes_menu.append('4. Separar')
        
        for opcoes in opcoes_menu:
            print(opcoes)

        opcoes_validas = list(range(1, len(opcoes_menu) + 1))
        opcao = escolher_opcao(opcoes_validas)

        if opcao == 1:
            time.sleep(1.25)
            limpar_tela()
            dar_carta_jogador()
            print(f'♣ Adicionamos a carta {cj[-1]} à sua mão ♣')
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cj)} -> {sum(v_cj)}')
            
            if sum(v_cj) == 21:
                print('== ♠ Você possui Blackjack == ♠')
                parar_rodada()

            if sum(v_cj) > 21:
                print(f'== ♠ Você ESTOUROU com {sum(v_cj)} pontos ♠ ==')
                print(f'= ♦ Aposta perdida: R${valor_aposta:.2f}')
                remover_saldo(valor_aposta)
                jogar_novamente()

            print(f'♦ Dealer -> Carta aberta: {cd[0]}')

        elif opcao == 2:
            parar_rodada()
    
        elif opcao == 3:
            dobrar()

        else:
            print()
            # Separar o jogo em duas mãos e fazer as ações para cada uma delas 
    
    if sum(v_cj) == 21:
        print('== ♠ Você possui Blackjack == ♠')
        parar_rodada()
    else:
        print(f'== ♠ Você ESTOUROU com {sum(v_cj)} pontos ♠ ==')
        print(f'= ♦ Aposta perdida: R${valor_aposta:.2f}')
        remover_saldo(valor_aposta)
        jogar_novamente()

def dobrar():
    global jogadorDobrou
    jogadorDobrou = True

    dar_carta_jogador()
    print(f'♣ Adicionamos a carta {cj[-1]} à sua mão ♣')
    if sum(v_cj) > 21:
                print(f'== ♠ Você ESTOUROU com {sum(v_cj)} pontos ♠ ==')
                print(f'= ♦ Aposta perdida: R${valor_aposta*2:.2f}')
                remover_saldo(valor_aposta*2)
                jogar_novamente()
    print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cj)} -> {sum(v_cj)}')
    parar_rodada()

def parar_rodada():
    time.sleep(1)
    print(f'♦ Cartas do Dealer: {', '.join(str(carta) for carta in cd)} -> {sum(v_cd)}')
    
    while sum(v_cd) < 17:
        time.sleep(1.25)
        dar_carta_dealer()
        print(f'♣ Adicionamos a carta {cd[-1]} à mão do Dealer ♣')
        print(f'♦ Cartas do Dealer: {', '.join(str(carta) for carta in cd)} -> {sum(v_cd)}')
    
    if sum(v_cd) > 16 and sum(v_cd) <= 21:
        if sum(v_cj) > sum(v_cd):
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cj)} -> {sum(v_cj)}')
            time.sleep(3)
            print(f'== ♠ Você GANHOU por {sum(v_cj)-sum(v_cd)} ponto(s) ♠ ==')
            if jogadorDobrou == False:
                print(f'= ♦ Aposta ganha: R${valor_aposta*2:.2f}')
                adicionar_saldo(valor_aposta)
            else:
                print(f'= ♦ Aposta ganha: R${valor_aposta*4:.2f}')
                adicionar_saldo(valor_aposta*2)
            jogar_novamente()

        elif sum(v_cj) < sum(v_cd):
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cj)} -> {sum(v_cj)}')
            time.sleep(3)
            print(f'== ♠ Você PERDEU por {sum(v_cd)-sum(v_cj)} ponto(s) ♠ ==')
            if jogadorDobrou == False:
                print(f'= ♦ Aposta perdida: R${valor_aposta:.2f}')
                remover_saldo(valor_aposta)
            else:
                print(f'= ♦ Aposta perdida: R${valor_aposta*2:.2f}')
                remover_saldo(valor_aposta*2)
            jogar_novamente()
    
        else:
            time.sleep(3)
            print('= ♦ Dealer EMPATOU com sua pontuação ♦ =')
            print('= ♦ Valor da aposta devolvido')
            jogar_novamente()
    else:
        time.sleep(1.25)
        print(f'== ♠ Dealer ESTOUROU com {sum(v_cd)} pontos ♠ ==')
        if jogadorDobrou == False:
            print(f'= ♦ Aposta ganha: R${valor_aposta*2:.2f}')
            adicionar_saldo(valor_aposta)
        else:
            print(f'= ♦ Aposta ganha: R${valor_aposta*4:.2f}')
            adicionar_saldo(valor_aposta*2)
        jogar_novamente()

def jogar_novamente():
    global cj, v_cj, cd, v_cd, jogadorDobrou
    time.sleep(2)

    if jogadorDobrou == True:
        jogadorDobrou = False
    
    cj = []
    v_cj = []

    cd = []
    v_cd = []

    print('== ♠ Rodada Encerrada ♠ ==')
    print(f'♦ Novo Saldo: R${saldo():.2f}')
    if saldo() > 0:
        print('♣ Deseja jogar novamente?')
        print('1. Sim')
        print('2. Não')
        opcao = escolher_opcao([1, 2])
        if opcao == 1:
            apostar()
        else:
            menu_inicial()
        
def separar_maos():
    primeiraMao = []
    v_primeiraMao = []
    
    segundaMao = []
    v_segundaMao = []

    dar_carta_jogador()
    primeiraMao.append(cj[0], cj[2])
    v_primeiraMao.append(v_cj[0], v_cj[2])
    
    dar_carta_jogador()
    segundaMao.append(cj[1], cj[3])
    v_segundaMao.append(v_cj[1], v_cj[3])

    # print(f'♠ Primeira Mão: {', '.join(str(carta) for carta in cj)} -> {sum(v_cj)}')
    # while v_primeiraMao < 21:
    #     print('1. Pedir')
    #     print('2. Parar')

def menu_inicial():
    time.sleep(1.5)
    limpar_tela()

    print('== ♠ Blackjack ♠ ==')
    print(f'= Saldo: R${saldo():.2f}')
    print('1. Apostar')
    print('2. Depositar')
    print('3. Sair')

    opcao = escolher_opcao([1, 2, 3])
    if opcao == 1:
        apostar()
    elif opcao == 2:
        depositar()
    else:
        sair()

def apostar():
    global valor_aposta

    time.sleep(2)
    limpar_tela()

    print('== ♠ Apostar ♠ ==')
    print(f'= Saldo atual: R${saldo():.2f}')

    if saldo() == 0:
        print('= Seu saldo está zerado.\n= Estamos te encaminhando para a Tela de Depósito.')
        time.sleep(2)
        depositar()

    while True:
        try:
            valor_aposta = float(input('♠ Aposta: R$').replace(',', '.'))
            while valor_aposta <= 0:
                 print('# Opção inválida! Por favor, insira um número maior que zero.')
                 valor_aposta = float(input('♠ Aposta: R$').replace(',', '.'))     
            break
        except ValueError:
            print('# Opção inválida! Por favor, insira um número válido.')
            
    if valor_aposta > saldo():
        time.sleep(1)
        print('= Você não possui saldo suficiente para esta aposta.')
        print('1. Mudar aposta')
        print('2. Depositar saldo')
        opcao = escolher_opcao([1, 2])

        if opcao == 1:
            apostar()
        else:
            depositar()
    else:
        iniciar_rodada()

def depositar():
    time.sleep(2)
    limpar_tela()

    print('== ♠ Tela de Depósito ♠ ==')
    print(f'♦ Saldo atual: R${saldo():.2f}')

    while True:
        try:
            valor_deposito = float(input('♠ Valor a ser depositado: R$').replace(',', '.'))
            while valor_deposito <= 0:
                 print('# Opção inválida! Por favor, insira um valor maior que zero.')
                 valor_deposito = float(input('♠ Valor a ser depositado: R$').replace(',', '.'))
            break
        except ValueError:
             print('# Opção inválida! Por favor, insira um valor numérico.')

    adicionar_saldo(valor_deposito)

    time.sleep(0.5)
    print('= Depósito concluído com sucesso!')
    print(f'= Novo saldo: R${saldo():.2f}')

    time.sleep(2)
    menu_inicial()

def sair():
    time.sleep(2)
    limpar_tela()
    print('== ♠ Saída ♠ ==')
    print('= ♠ Você optou por sair do Blackjack, volte sempre!')
    sys.exit(0)

try:
    with open('saldo.txt', 'x') as arq:
        arq.write('0')
except FileExistsError:
    if os.path.getsize('saldo.txt') == 0:
        with open('saldo.txt', 'w') as arq:
            arq.write('0')

cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
baralhoCompleto = [carta for carta in cartas for _ in range(4)]
baralho = baralhoCompleto.copy()
random.shuffle(baralho)

cj = []
v_cj = []

cd = []
v_cd = []

jogadorDobrou = False

menu_inicial()