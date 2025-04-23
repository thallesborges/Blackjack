import random, os, platform, time, sys

def embaralhar(baralho):
    random.shuffle(baralho)

def verificar_arquivo():
    try:
          with open('saldo.txt', 'x') as arq:
               arq.write('0')
    except FileExistsError:
        if os.path.getsize('saldo.txt') == 0:
            with open('saldo.txt', 'w') as arq:
                arq.write('0')

def menu():
    limpar_tela()

    print('=== ♠ Blackjack ♠ ===')
    print(f'= Saldo: R${saldo()}')
    print('1. Apostar')
    print('2. Depositar')
    print('3. Configurações')
    print('4. Sair')

    while True:
        try: 
            opcao = int(input('♠ Opção: '))
            break
        except ValueError:
            print('= Por favor, insira uma opção válida (1/2/3/4).')

    while opcao not in [1, 2, 3, 4]:
        try:
            print('= Opção inválida. Por favor, escolha 1, 2, 3 ou 4.')
            opcao = int(input('♠ Opção: '))
            
        except ValueError:
            print('= Opção inválida. Por favor, escolha 1, 2, 3 ou 4.')

    if opcao == 4:
        sair()
    elif opcao == 3:
        # # time.sleep(x)
        configuracoes()
    elif opcao == 2:
        # # time.sleep(x)
        depositar()
    else:
        # # time.sleep(x)
        # limpar_tela()
        time.sleep(1.5)
        apostar()
        time.sleep(1.5)
        jogar(valor_aposta)

def sair():
    limpar_tela()
    print('♠ Você optou em sair do Blackjack ♠')
    sys.exit(0)

def saldo():
     with open('saldo.txt', 'r') as arq:
        valor_saldo = arq.read()
        return float(valor_saldo)

def limpar_tela():
     if platform.system() == 'Windows':
          os.system('cls')
     else:
          os.system('clear')  

def depositar():
    # limpar_tela()

    while True:
        try:
            print(f'=== ♠ Saldo atual: R${saldo()} ♠ ===')
            valor_deposito = float(input('♠ Valor a ser depositado: R$'))

            while valor_deposito <= 0:
                 print('= Por favor, insira um valor maior que zero.')
                 valor_deposito = float(input('♠ Valor a ser depositado: R$'))

            saldo_antigo = float(saldo())
            novo_saldo = saldo_antigo + valor_deposito
     
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

            # # time.sleep(x)
            print('= Depósito concluído com sucesso!')
            print(f'= Novo saldo: R${novo_saldo}')
            # time.sleep(2.5)
            # limpar_tela()
            break

        except ValueError:
             print('= Por favor, insira um valor numérico.')
    
    menu()

def apostar():
    global valor_aposta
    
    limpar_tela()

    print('=== ♠ Apostar ♠ ===')

    if saldo() == 0:
        # limpar_tela()
        print('= Seu saldo está zerado ⚠\n= Para apostar é preciso possuir saldo: ')
        print('1. Depositar')
        print('2. Sair')
        
        while True:
            try:
                opcao = int(input('♠ Opção: '))
                break
            except ValueError:
                print('= Por favor, insira uma opção válida (1/2).')

        while opcao not in [1, 2]:
            try:
                print('= Por favor, insira uma opção válida (1/2).')
                opcao = int(input('♠ Opção: '))
            except ValueError:
                print('= Por favor, insira uma opção válida (1/2).')
        if opcao == 1:
            # # time.sleep(x)
            depositar()
        else:
            sair()

    while True:
        try:
            valor_aposta = float(input('♠ Aposta: R$'))
            break
        except ValueError:
            print('= Por favor, insira um número válido.')

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
    # time.sleep(2)

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
    
    if cartas_jogador == ['A', 'A']:
        valor_cartas_jogador = [11, 1]

    print(f'♠ Aposta: R${valor_aposta}')

    if cartas_dealer[0] == 'A' and (valor_aposta + (valor_aposta/2)) <= saldo():
        print('= O Dealer está com um às!')
        seguro = input('♠ Deseja fazer seguro? (Y/N): ').upper()

        while seguro not in ['Y', 'N']:
              try:
                seguro = input('Por favor, escolha uma opção disponível (Y/N): ').upper()
              except ValueError:
                seguro = input('Por favor, escolha uma opção válida (Y/N): ').upper()

        if seguro == 'Y' and sum(valor_cartas_dealer) == 21:
            print('= 💰 Dealer possui Blackjack, o seguro cobriu a aposta.')
            apostar_novamente()
                
        elif seguro == 'Y' and sum(valor_cartas_dealer) < 21:
            print('= Dealer não possui Blackjack.')
            print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)}')

            novo_saldo = saldo() - (valor_aposta/2)
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

    elif cartas_dealer[0] == 'A' and (valor_aposta + (valor_aposta/2)) > saldo():
        print('= O Dealer está com um ÀS!')
        print('= Você não possui saldo suficiente para fazer seguro.')

    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)
     
def apostar_novamente():
    # # time.sleep(5)
    # # limpar_tela()

    print('=== ♠ Rodada encerrada ♠ ===')
    print(f'= Saldo atual: R${saldo()}')
    if saldo() == 0:
        print('= Seu saldo zerou. Por favor, deposite mais crédito na página de depósito.')
        # time.sleep(3)
        menu()

    apostar_novamente = input('♠ Apostar novamente? (Y/N): ').upper()
    while apostar_novamente not in ['Y', 'N']:
        try:
            apostar_novamente = input('= Por favor, escolha uma opção válida (Y/N): ').upper()
        except ValueError:
            apostar_novamente = input('= Por favor, escolha uma opção válida (Y/N): ').upper()
    if apostar_novamente == 'Y':
        apostar()
        # # time.sleep(x)
        jogar(valor_aposta)
    elif apostar_novamente == 'N':
        menu()

def menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer):
    print(f'♠ DEALER -> Carta aberta: {cartas_dealer[0]}')
    print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')

    if len(cartas_jogador) == 2 and sum(valor_cartas_jogador) == 21:
        print('🤑 Blackjack 🤑')
        print(f'= Valor ganho: R${valor_aposta*1.5}')

        novo_saldo = saldo() + valor_aposta*1.5
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))

        apostar_novamente()

    elif len(cartas_jogador) > 2 and sum(valor_cartas_jogador) == 21:
        print('💲 Blackjack 💲')
        print(f'= Valor ganho: R${valor_aposta}')

        novo_saldo = saldo() + valor_aposta
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))

        apostar_novamente()        
        
    elif sum(valor_cartas_jogador) > 21: 
        print('💣 Você estourou 💣')
        print(f'= Valor perdido: R${valor_aposta}')

        novo_saldo = saldo() - valor_aposta
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))

        apostar_novamente()

    else:
        while sum(valor_cartas_jogador) < 21:
            if valor_cartas_jogador[0] == valor_cartas_jogador[1]:
                print('1. Dividir')
                print('2. Pedir')
                print('3. Parar')
                print('4. Dobrar')

                opcao = int(input('♠ Opção: '))      

                while opcao not in [1, 2, 3, 4]:
                    try:
                        print('= Por favor, escolha uma opção válida (1/2/3/4): ')
                        opcao = int(input('♠ Opção: '))
                    except ValueError:
                        print('= Por favor, escolha uma opção válida (1/2/3/4): ')
                        opcao = int(input('♠ Opção: '))
                        
                if opcao == 1:
                    # Dividir
                    print('Dividindo...') # !! Criar a função dividir_cartas()
                elif opcao == 2:
                    # Pedir
                    pedir_carta(cartas_jogador, valor_cartas_jogador)
                elif opcao == 3:
                    # Parar
                    parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)
                else:
                    # Dobrar
                    print('Dobrando...') # !! Criar a função dobrar_cartas()

            elif len(cartas_jogador) == 2:
                print('1. Pedir')
                print('2. Parar')
                print('3. Dobrar')
                opcao = int(input('♠ Opção: '))
                while opcao not in [1, 2, 3]:
                    try:
                        print('= Por favor, escolha uma opção válida (1/2/3): ')
                        opcao = int(input('♠ Opção: '))
                    except ValueError:
                        print('= Por favor, escolha uma opção válida (1/2/3): ')
                        opcao = int(input('♠ Opção: '))

                if opcao == 1:
                    time.sleep(2)
                    limpar_tela()
                    pedir_carta(cartas_jogador, valor_cartas_jogador)
                    print(f'== Uma carta foi adicionada à sua mão: {cartas_jogador[-1]}')
                    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)

                elif opcao == 2:
                    # # time.sleep(x)
                    # limpar_tela()
                    parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)

                else:
                    print('Dobrando...')

            else:
                print('1. Pedir')
                print('2. Parar')
                opcao = int(input('♠ Opção: '))

                while opcao not in [1, 2]:
                    try:
                        print('= Por favor, escolha uma opção válida (1/2): ')
                        opcao = int(input('♠ Opção: '))
                    except ValueError:
                        print('= Por favor, escolha uma opção válida (1/2): ')
                        opcao = int(input('♠ Opção: '))

                if opcao == 1:
                    time.sleep(2)
                    limpar_tela()
                    pedir_carta(cartas_jogador, valor_cartas_jogador)
                    print(f'== Uma carta foi adicionada à sua mão: {cartas_jogador[-1]}')
                    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)

                else:
                    # # # time.sleep(x)
                    # # limpar_tela()
                    parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)

# def dividir(): 

def pedir_carta(cartas_jogador, valor_cartas_jogador):
    carta = baralho.pop(0)
    cartas_jogador.append(carta)
    if carta in ['J', 'Q', 'K']:
        valor_cartas_jogador.append(10)
    elif carta == 'A' and (sum(valor_cartas_jogador) + 11) > 21:
        valor_cartas_jogador.append(1)
    elif carta == 'A' and (sum(valor_cartas_jogador) + 11) <= 21:
        valor_cartas_jogador.append(11)
    else:
        valor_cartas_jogador.append(carta)

    return valor_cartas_jogador, cartas_jogador

def parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador):

    print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)} -> {sum(valor_cartas_dealer)}')

    while sum(valor_cartas_dealer) < 17:
        # # time.sleep(x)
        carta = baralho.pop(0)
        cartas_dealer.append(carta)

        if carta in ['J', 'Q', 'K']:
            valor_cartas_dealer.append(10)
        elif carta == 'A' and (sum(valor_cartas_dealer) + 11) > 21:
            valor_cartas_dealer.append(1)
        elif carta == 'A' and (sum(valor_cartas_dealer) + 11) <= 21:
            valor_cartas_dealer.append(11)
        else:
            valor_cartas_dealer.append(carta)

        if sum(valor_cartas_dealer) > 21 and 'A' in valor_cartas_dealer == True:
            sum(valor_cartas_dealer) == sum(valor_cartas_dealer) - 10

        print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)} -> {sum(valor_cartas_dealer)}')
        
    if sum(valor_cartas_dealer) >= 17 and sum(valor_cartas_dealer) <= 21:
        if sum(valor_cartas_dealer) > sum(valor_cartas_jogador) or sum(valor_cartas_dealer) == 21:
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')
            print('=== Resultado ===')
            print(f'🔴 Você perdeu por {sum(valor_cartas_dealer) - sum(valor_cartas_jogador)} ponto(s) de diferença 🔴')
            print(f'= Saldo perdido: R${valor_aposta}')

            novo_saldo = saldo() - valor_aposta
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))
            
            # time.sleep(6)
            # limpar_tela()
            apostar_novamente()

        elif sum(valor_cartas_jogador) > sum(valor_cartas_dealer):
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')
            print(f'💲 Você ganhou por {sum(valor_cartas_jogador) - sum(valor_cartas_dealer)} ponto(s) de diferença 💲')
            print(f'= Saldo ganho: R${valor_aposta}')

            novo_saldo = saldo() + valor_aposta
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

            # time.sleep(6)
            # limpar_tela()
            apostar_novamente()
        
    else:
        print('💣 Dealer estorou 💣')
        print(f'= Valor ganho: R${valor_aposta}')

        novo_saldo = saldo() + valor_aposta
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))
            
        apostar_novamente()
        
# def dobrar_cartas():

def configuracoes(): # Adicionar opções para mudar a quantidade de baralhos.
    # limpar_tela()
    print('== ♠ Configurações ♠ ==')
    print('1. Quantidade de Baralhos')

cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
baralho_ordenado = [carta for carta in cartas for _ in range(4)]

baralho = baralho_ordenado.copy()
embaralhar(baralho)


verificar_arquivo()
menu()