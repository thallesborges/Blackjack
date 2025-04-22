import random, os, platform, time, sys

def depositar():
    limpar_tela()

    while True:
        try:
            print(f'=== ♠ Saldo atual: R${saldo()} ===')
            valor_deposito = float(input('♠ Valor a ser depositado: R$'))

            while valor_deposito <= 0:
                 print('= Por favor, insira um valor maior que zero.')
                 valor_deposito = float(input('♠ Valor a ser depositado: R$'))

            saldo_antigo = float(saldo())
            novo_saldo = saldo_antigo + valor_deposito
     
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

            time.sleep(1)
            limpar_tela()
            print('= Depósito concluído com sucesso!')
            print(f'= Novo saldo: R${novo_saldo}')
            time.sleep(2.5)
            limpar_tela()
            break

        except ValueError:
             print('= Por favor, insira um valor numérico.')
    
    menu()

def jogar(valor_aposta):
    limpar_tela()
    
    cartas_dealer = []
    cartas_jogador = []
    valor_cartas_dealer = []
    valor_cartas_jogador = []

    print('= ♠ Iniciando o Blackjack ♠ =')
    
    for i in range(4):
        carta = baralho.pop(0)

        if i % 2 == 0:
            cartas_dealer.append(carta)
            if carta in ['J', 'Q', 'K']:
                valor_cartas_dealer.append(10)
            elif carta == 'A':
                valor_cartas_dealer.append(11)
            else:
                valor_cartas_dealer.append(carta)

        else:
            cartas_jogador.append(carta)
            if carta in ['J', 'Q', 'K']:
                    valor_cartas_jogador.append(10)
            elif carta == 'A':
                    valor_cartas_jogador.append(11)
            else:
                    valor_cartas_jogador.append(carta)

    if cartas_dealer == ['A', 'A']:
        valor_cartas_dealer = [11, 1]

    print(f'♠ Aposta: R${valor_aposta}')
    print(f'<LOG> DEALER -> {cartas_dealer} -> {sum(valor_cartas_dealer)} <LOG>')
    print(f'DEALER -> {cartas_dealer[0]}')
    menu_aposta(cartas_jogador, valor_cartas_jogador)

    if cartas_dealer[0] == 'A' and (valor_aposta + (valor_aposta/2)) <= saldo():
        print('= O Dealer está com um às!')
        seguro = input('♠ Deseja fazer seguro? (Y/N): ')

        while seguro not in ['Y', 'N']:
              try:
                seguro = input('Por favor, escolha uma opção disponível (Y/N): ')
              except ValueError:
                seguro = input('Por favor, escolha uma opção válida (Y/N): ')

        if seguro == 'Y' and sum(valor_cartas_dealer) == 21:
            print('= 🏦 Dealer possui Blackjack, o seguro cobriu a aposta.')
            apostar_novamente()
                
        elif seguro == 'Y' and sum(valor_cartas_dealer) != 21:
            print('= Você perdeu o seguro, Dealer não possui Blackjack.')
            novo_saldo = saldo() - (valor_aposta/2)
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

    elif cartas_dealer[0] == 'A' and (valor_aposta + (valor_aposta/2)) > saldo():
        print('= O Dealer está com um ÀS!')
        print('= Você não possui saldo suficiente para fazer seguro.')
     
def apostar_novamente():
    print('=== ♠ Rodada encerrada ♠ ===')
    apostar_novamente = input('♠ Apostar novamente? (Y/N): ')
    while apostar_novamente not in ['Y', 'N']:
        try:
            apostar_novamente = input('= Por favor, escolha uma opção válida (Y/N): ')
        except ValueError:
            apostar_novamente = input('= Por favor, escolha uma opção válida (Y/N): ')
    if apostar_novamente == 'Y':
        apostar()
    elif apostar_novamente == 'N':
        menu()

def apostar():
    global valor_aposta

    saldo()

    if saldo() == 0:
        limpar_tela()
        print('⚠ Seu saldo está zerado ⚠\n= Para apostar é necessário possuir saldo: ')
        print('1. Depositar')
        print('2. Sair')
        opcao = int(input('♠ Opção: '))

        while opcao not in [1, 2]:
            try:
                opcao = input('= Por favor, escolha uma opção válida (1/2): ')
            except ValueError:
                opcao = input('= Por favor, escolha uma opção válida (1/2): ')
        if opcao == 1:
            time.sleep(1)
            depositar()
        else:
            time.sleep(1)
            limpar_tela()
            print('= Você optou por sair do ♠ Blackjack ♠\n= Volte sempre!')
            sys.exit(0)

    while True:
        try:
            valor_aposta = float(input('♠ Aposta: R$'))
            break
        except ValueError:
            print('Por favor, insira um número válido.')

    while valor_aposta <= 0:
        try:
            print('= Por favor, aposte um valor maior que zero.')
            valor_aposta = float(input('♠ Aposta: R$'))
            break
        except ValueError:
            print('= Por favor, insira um número válido maior que zero.')
            
    while valor_aposta > saldo():
        print('= Você não possui saldo suficiente para esta aposta.')
        print(f'= Saldo atual: R${saldo()}')
        print('1. Mudar valor da aposta')
        print('2. Depositar saldo')

        opcao = int(input('♠ Opção: '))
        while opcao not in [1, 2]:
            try:
                print('= Por favor, escolha uma opção válida (1/2): ')
                opcao = int(input('♠ Opção: '))
            except ValueError:
                print('= Por favor, escolha uma opção válida (1/2): ')
                    
        if opcao == 1:
            valor_aposta = float(input('♠ Novo valor da aposta: R$'))
            while valor_aposta > saldo():
                print('= Você não possui saldo suficiente para esta aposta.')
                print(f'= Saldo atual: R${saldo()}')
                valor_aposta = float(input(' ♠ Novo valor da aposta: R$'))
        else:
            print('= Estamos te transferindo para a página de depósito, aguarde.')
            depositar()
        
    print(f'= Aposta de R${valor_aposta} feita com sucesso!')
    time.sleep(2)

def menu_aposta(cartas_jogador, valor_cartas_jogador):

    print(f'🃏 Suas cartas: {cartas_jogador[0]} & {cartas_jogador[1]}')

    if cartas_jogador == ['A', 'A']:
        valor_cartas_jogador = [11, 1]

    if sum(valor_cartas_jogador) < 21:
        if valor_cartas_jogador[0] == valor_cartas_jogador[1]:
            print('1. Dividir')
            print('2. Parar')
            print('3. Pedir')
            print('4. Dobrar')

            opcao = int(input('♠ Opção: '))
            if opcao == 1:
                print('Dividindo...')
            elif opcao == 2:
                print('Parando...')
            elif opcao == 3:
                print('Pedindo...')
            else:
                print('Dobrando...')

        else: # while
            print('1. Pedir')
            print('2. Parar')
            print('3. Dobrar')
            opcao = int(input('♠ Opção: '))
            if opcao == 1:
                print('Pedindo...')
            elif opcao == 2:
                print('Parando...')
            else:
                print('Dobrando...')

    elif sum(cartas) == 21:
        print('🤑 Blackjack!')
        print(f'= Valor recebido: R${valor_aposta*2}')
        apostar_novamente()
    else: 
        print('Estourou! 💣')
        # Remover valor da aposta do saldo
        apostar_novamente()

def saldo():
     with open('saldo.txt', 'r') as arq:
        saldo = arq.read()
        return float(saldo)

def menu():
    limpar_tela()

    saldo()

    print('=== Blackjack ♠ ===')
    print(f'= Saldo: R${saldo()}')
    print('1. Apostar')
    print('2. Depositar')
    print('3. Sair')

    while True:
        try:
            opcao = int(input('♠ Opção: '))
            while opcao not in [1, 2, 3]:
                    print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
                    opcao = int(input('♠ Opção: '))
            break
        except ValueError:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')

    if opcao == 3:
        limpar_tela()
        print('= Você optou por sair do ♠ Blackjack ♠\n= Volte sempre!')
        sys.exit(0)
    elif opcao == 2:
        time.sleep(1)
        depositar()
    else:
        apostar()
        jogar(valor_aposta)

def limpar_tela():
     if platform.system() == 'Windows':
          os.system('cls')
     else:
          os.system('clear')  

def embaralhar(baralho):
    random.shuffle(baralho)

def verificar_arquivo():
    try:
          with open('saldo.txt', 'x') as arq:
               arq.write('0')
               print('<LOG> Arquivo criado com sucesso <LOG>')
    except FileExistsError:
        print('<LOG> O arquivo já existe <LOG>')
        if os.path.getsize('saldo.txt') == 0:
            print('<LOG> O arquivo está vazio -> Escrevendo valor inicial <LOG>')
            with open('saldo.txt', 'w') as arq:
                arq.write('0')
    
    print('<LOG> Iniciando o Blackjack <LOG>')
    time.sleep(1)
    limpar_tela()

cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
baralho_ordenado = [carta for carta in cartas for _ in range(4)]

baralho = baralho_ordenado.copy()
embaralhar(baralho)

verificar_arquivo()
menu()