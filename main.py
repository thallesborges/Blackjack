import random, os, platform, time

def limpar_tela():
     if platform.system() == 'Windows':
          os.system('cls')
     else:
          os.system('clear')

def embaralhar(baralho):
    random.shuffle(baralho)

def depositar():
    # limpar_tela()
    
    with open('saldo.txt', 'r') as arq:
        saldo = arq.read()

    while True:
        try:
            print(f'=== ♠ Saldo atual: R${saldo} ===')
            valor_deposito = float(input('Valor a ser depositado: R$'))

            while valor_deposito <= 0:
                 print('Por favor, insira um valor maior que zero.')
                 valor_deposito = float(input('Valor a ser depositado: R$'))

            saldo_antigo = float(saldo)
            novo_saldo = saldo_antigo + valor_deposito
     
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

            print('♠ Depósito concluído com sucesso!')
            print(f'=== ♠ Novo saldo: R${novo_saldo}')
            print('')
            print('Estamos te redirecionando para o Menu principal...')

            break

        except ValueError:
             print('Por favor, insira um valor válido.')
    
    menu()
     
def verificar_arquivo():
    try:
          with open('saldo.txt', 'x') as arq:
               arq.write('0.00')
               print('!! LOG -> Arquivo criado com sucesso.')

    except FileExistsError:
        print('!! LOG -> O arquivo já existe.')
    
    print('!! LOG -> Iniciando o Blackjack...')
    # time.sleep(2)

def jogar(aposta):
    cartas_dealer = []
    cartas_jogador = []
    valor_cartas_dealer = []
    valor_cartas_jogador = []

    print(baralho)
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

    print('')
    print(f'♠ Aposta: R${aposta}')
    print(f'!! LOG !! DEALER -> {cartas_dealer} -> {sum(valor_cartas_dealer)}')
    print(f'DEALER -> {cartas_dealer[0]}')
    print(f'JOGADOR -> {cartas_jogador[0]} & {cartas_jogador[1]}')

    if cartas_dealer[0] == 'A' and (valor_aposta + (valor_aposta/2)) < saldo():
        print('O Dealer está com um ÀS!')
        seguro = input('Deseja fazer seguro? (Y/N): ')

        while seguro not in ['Y', 'N']:
              try:
                seguro = input('Por favor, escolha uma opção disponível (Y/N): ')
              except ValueError:
                seguro = input('Por favor, escolha uma opção válida (Y/N): ')

        if seguro == 'Y' and sum(valor_cartas_dealer) == 21:
            print('Dealer possui 21 -> Seguro cobriu a aposta.')
            print('=== ♠ Rodada encerrada ♠ ===')
            apostar_novamente = input('♠ Apostar novamente? (Y/N): ')
            while apostar_novamente not in ['Y', 'N']:
                try:
                    apostar_novamente = input('Por favor, escolha uma opção válida (Y/N): ')
                except ValueError:
                    apostar_novamente = input('Por favor, escolha uma opção válida (Y/N): ')
            if apostar_novamente == 'Y':
                apostar()
            elif apostar_novamente == 'N':
                menu()
                
        elif seguro == 'Y' and sum(valor_cartas_dealer) != 21:
             with open('saldo.txt', 'w') as arq:
                  arq.write(float(saldo() - (valor_aposta/2)))

    elif cartas_dealer[0] == 'A' and (valor_aposta + (valor_aposta/2)) > saldo():
        print('O Dealer está com um ÀS!')
        print('Você não possui saldo suficiente para fazer seguro.')

    # print(f'Cartas do Dealer: {cartas_dealer[0]} & {cartas_dealer[1]}')
        
def apostar():
    global valor_aposta

    saldo()

    if saldo() == 0:
        # limpar_tela()
        print('Seu saldo está zerado. Para apostar é necessário possuir saldo.')
        print('Estamos te levando à tela de depósito.')
        # time.sleep(3)
        # limpar_tela()
        depositar()

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
        
            
    print('')
    print(f'= Aposta de R${valor_aposta} feita com sucesso!\n== ♠ Iniciando o Blackjack ♠ ==')
    # time.sleep(2)
    
def saldo():
     with open('saldo.txt', 'r') as arq:
        saldo = float(arq.read())
        return saldo

def menu():
    # limpar_tela()

    saldo()

    print('=== Blackjack ♠ ===')
    print(f'♠ Saldo: R${saldo()} ♠')
    print('1. Apostar')
    print('2. Depositar')
    print('3. Sair')

    while True:
        try:
            opcao = int(input('== Opção: '))
            while opcao not in [1, 2, 3]:
                    print('Opção inválida. Por favor, escolha 1, 2 ou 3.')
                    opcao = int(input('== Opção: '))
            break
        except ValueError:
            print('Opção inválida. Por favor, escolha 1, 2 ou 3.')

    if opcao == 3:
        # limpar_tela()
        print('Você optou por sair do Blackjack ♠, volte sempre!')
    elif opcao == 2:
        depositar()
    else:
        apostar()
        jogar(valor_aposta)
        
cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
baralho_ordenado = [carta for carta in cartas for _ in range(4)]

baralho = baralho_ordenado.copy()
embaralhar(baralho)

verificar_arquivo()

menu()