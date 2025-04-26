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
    time.sleep(1.5)
    limpar_tela()

    print('=== ♠ Blackjack ♠ ===')
    print(f'= Saldo: R${saldo():.2f}')
    print('1. Apostar')
    print('2. Depositar')
    print('3. Sair')

    while True:
        try: 
            opcao = int(input('♠ Opção: '))
            while opcao not in [1, 2, 3]:
                print('## Opção inválida! Por favor, insira 1, 2 ou 3.')
                opcao = int(input('♠ Opção: '))
            break
        except ValueError:
            print('## Opção inválida! Por favor, insira 1, 2 ou 3.')

    if opcao == 3:
        sair()
    elif opcao == 2:
        depositar()
    else:
        apostar()
        jogar(valor_aposta)

def sair():
    time.sleep(2)
    limpar_tela()
    print('=== ♠ Saída ♠ ===')
    print('= Você optou por sair do Blackjack, volte sempre!')
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
    time.sleep(2)
    limpar_tela()

    print(f'=== ♠ Saldo atual: R${saldo():.2f} ♠ ===')

    while True:
        try:
            valor_deposito = float(input('♠ Valor a ser depositado: R$'))
            while valor_deposito <= 0:
                 print('# Opção inválida! Por favor, insira um valor maior que zero.')
                 valor_deposito = float(input('♠ Valor a ser depositado: R$'))
            break
        except ValueError:
             print('## Opção inválida! Por favor, insira um valor numérico.')

    novo_saldo = saldo() + valor_deposito
    with open('saldo.txt', 'w') as arq:
        arq.write(str(novo_saldo))

    time.sleep(0.5)
    print('= Depósito concluído com sucesso!')
    print(f'= Novo saldo: R${saldo():.2f}')

    time.sleep(1)
    menu()

def apostar():
    global valor_aposta

    time.sleep(2)
    limpar_tela()

    print('=== ♠ Apostar ♠ ===')
    print(f'= Saldo atual: R${saldo():.2f}')

    if saldo() == 0:
        print('= Seu saldo está zerado.\n= Estamos te encaminhando para a sessão de depósito.')
        time.sleep(3)
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

        while True:
            try:
                opcao = int(input('♠ Opção: '))
                while opcao not in [1, 2]:
                    print('# Opção inválida! Por favor, insira 1 ou 2. ')
                    opcao = int(input('♠ Opção: '))
                break
            except ValueError:
                print('# Opção inválida! Por favor, insira 1 ou 2.')

        if opcao == 1:
            apostar()
        else:
            depositar()
    else:
        novo_saldo = saldo() - valor_aposta
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))
    
def jogar(valor_aposta):
    time.sleep(2)
    limpar_tela()

    if len(baralho) == len(baralho)/2:
        embaralhar(baralho_ordenado)
        print('=== ♠ Reembaralhando ♠ ===')
    
    cartas_dealer = []
    cartas_jogador = []
    valor_cartas_dealer = []
    valor_cartas_jogador = []

    print('=== ♠ Entregando Cartas ♠ ===')
    
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

    print(f'= Aposta: R${valor_aposta:.2f}')
    print(f'♠ DEALER -> Carta aberta: {cartas_dealer[0]}')

    if cartas_dealer[0] == 'A' and (valor_aposta/2) <= saldo():
        print('= O Dealer está com um ás!')
        print('♦ Deseja fazer seguro?')
        print('1. Sim')
        print('2. Não')
        
        while True:
            try:
                opcao = int(input('♠ Opção: '))
                while opcao not in [1, 2]:
                    print('# Opção inválida! Por favor, insira 1 ou 2.')
                break
            except ValueError:
                print('# Opção inválida! Por favor, insira 1 ou 2.')

        if opcao == 1 and sum(valor_cartas_dealer) == 21:
            print('= ♦ Dealer possui Blackjack, o seguro cobriu a aposta.')
            apostar_novamente()
        
        elif opcao == 1 and sum(valor_cartas_dealer) < 21:
            print('♦ Dealer não possui Blackjack.')
            print(f'= Dinheiro gasto no seguro: {valor_aposta/2}')

            novo_saldo = saldo() - (valor_aposta/2)
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))
        
        elif opcao == 2 and sum(valor_cartas_dealer) == 21:
            parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)
        
        else:
            print('Erro desconhecido, linha 207.')
            
    elif cartas_dealer[0] == 'A' and (valor_aposta/2) > saldo():
        print('= O Dealer está com um ás!')
        print('= Você não possui saldo suficiente para fazer seguro.')

    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)
     
def apostar_novamente():
    time.sleep(2)
    print('=== ♠ Rodada Encerrada ♠ ===')
    print(f'= Saldo atual: R${saldo():.2f}')
    if saldo() == 0:
        print('= Seu saldo zerou. Por favor, deposite mais crédito na página de depósito.')
        time.sleep(4)
        menu()

    print('= Apostar novamente?')
    print('1. Sim')
    print('2. Não')

    while True:
        try:
            opcao = int(input('♠ Opção: '))
            while opcao not in [1, 2]:
                print('# Opção inválida! Por favor, insira 1 ou 2.')
            break
        except ValueError:
            print('# Opção inválida! Por favor, insira 1 ou 2.')

    if opcao  == 1:
        apostar()
        jogar(valor_aposta)
    else:
        menu()

def menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer):
    print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')

    time.sleep(2)
    if len(cartas_jogador) == 2 and sum(valor_cartas_jogador) == 21:
        if sum(valor_cartas_dealer) >= 17 and sum(valor_cartas_dealer) < 21:
            print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)} -> {sum(valor_cartas_dealer)}')
            print('♥.♥ BLACKJACK ♥.♥')
            print(f'= Dinheiro ganho: R${(valor_aposta*1.5):.2f}')

            novo_saldo = saldo() + valor_aposta*2.5
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))
    
            apostar_novamente()

        else:
            print('♥ VOCÊ POSSUI BLACKJACK ♥')
            print('== ♠ Verificando cartas do Dealer ♠ ==')
            parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)
        
    elif len(cartas_jogador) > 2 and sum(valor_cartas_jogador) == 21:
        print('♥ BLACKJACK ♥')
        print(f'= Dinheiro ganho: R${valor_aposta:.2f}')

        novo_saldo = saldo() + valor_aposta*2
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))

        apostar_novamente()        
        
    elif sum(valor_cartas_jogador) > 21: 

        print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)} -> {sum(valor_cartas_dealer)}')
        print('♣ VOCÊ ESTOUROU ♣')
        print(f'= Dinheiro perdido: R${valor_aposta:.2f}')

        apostar_novamente()

    else:
        while sum(valor_cartas_jogador) < 21:
            if len(cartas_jogador) == 2 and valor_cartas_jogador[0] == valor_cartas_jogador[1]:
                print('1. Pedir')
                print('2. Parar')
                print('3. Dobrar')
                print('4. Dividir')

                while True:
                    try:
                        opcao = int(input('♠ Opção: '))
                        while opcao not in [1, 2, 3, 4]:
                            print('## Opção inválida! Por favor, insira 1, 2, 3, ou 4.')
                            opcao = int(input('♠ Opção: '))
                        break
                    except ValueError:
                        print('## Opção inválida! Por favor, insira 1, 2, 3 ou 4.')

                if opcao == 1:
                    # Pedir
                    pedir_carta(cartas_jogador, valor_cartas_jogador)
                    limpar_tela()
                    print(f'= Aposta: R${valor_aposta:.2f}')
                    if len(cartas_dealer) == 2:
                        print(f'= DEALER -> Carta aberta: {cartas_dealer[0]}')
                    if len(cartas_dealer) > 2:
                        print(f'== Uma carta foi adicionada à sua mão: {cartas_jogador[-1]}')
                    
                    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)
                elif opcao == 2:
                    # Parar
                    parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)
                elif opcao == 3:
                    # Dobrar
                    print('Dobrando...') # !! Criar a função dobrar_cartas()
                else:
                    # Dividir
                    print('Dividindo...') # !! Criar a função dividir_cartas()

            elif len(cartas_jogador) == 2:
                print('1. Pedir')
                print('2. Parar')
                print('3. Dobrar')

                while True:
                    try:
                        opcao = int(input('♠ Opção: '))
                        while opcao not in [1, 2, 3]:
                            print('## Opção inválida! Por favor, insira 1, 2 ou 3.')
                            opcao = int(input('♠ Opção: '))
                        break
                    except ValueError:
                        print('## Opção inválida! Por favor, insira 1, 2 ou 3.')

                if opcao == 1:
                    pedir_carta(cartas_jogador, valor_cartas_jogador)
                    limpar_tela()
                    print(f'= Aposta: R${valor_aposta:.2f}')
                    print(f'== Uma carta foi adicionada à sua mão: {cartas_jogador[-1]}')
                    print(f'♠ DEALER -> Carta aberta: {cartas_dealer[0]}')
                    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)

                elif opcao == 2:
                    parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)

                else:
                    print('Dobrando...')

            else:
                print('1. Pedir')
                print('2. Parar')

                while True:
                    try:
                        opcao = int(input('♠ Opção: '))
                        while opcao not in [1, 2]:
                            print('## Opção inválida! Por favor, insira 1 ou 2.')
                            opcao = int(input('♠ Opção: '))
                        break   
                    except ValueError:
                        print('## Opção inválida! Por favor, insira 1 ou 2.')

                if opcao == 1:
                    pedir_carta(cartas_jogador, valor_cartas_jogador)
                    limpar_tela()
                    print(f'= Aposta: R${valor_aposta:.2f}')
                    print(f'== Uma carta foi adicionada à sua mão: {cartas_jogador[-1]}')
                    menu_aposta(cartas_jogador, valor_cartas_jogador, cartas_dealer, valor_cartas_dealer)

                else:
                    time.sleep(2)
                    parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador)

# def dividir(): 

def pedir_carta(cartas_jogador, valor_cartas_jogador):
    time.sleep(2)

    carta = baralho.pop(0)
    cartas_jogador.append(carta)
    
    if carta in ['J', 'Q', 'K']:
        valor_cartas_jogador.append(10)
    elif carta == 'A':
        valor_cartas_jogador.append(11)
    else:
        valor_cartas_jogador.append(carta)

    if 'A' in cartas_jogador and sum(valor_cartas_jogador) > 21:
        for i in range(len(cartas_jogador)):
            if valor_cartas_jogador[i] == 11:
                valor_cartas_jogador[i] = 1

    return valor_cartas_jogador, cartas_jogador

def parar_rodada(cartas_dealer, valor_cartas_dealer, cartas_jogador, valor_cartas_jogador):
    
    print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)} -> {sum(valor_cartas_dealer)}')

    while sum(valor_cartas_dealer) < 17:
        carta = baralho.pop(0)
        cartas_dealer.append(carta)

        if carta in ['J', 'Q', 'K']:
            valor_cartas_dealer.append(10)
        elif carta == 'A':
            valor_cartas_dealer.append(11)
        else:
            valor_cartas_dealer.append(carta)

        if 'A' in cartas_dealer and sum(valor_cartas_dealer) > 21:
            for i in range(len(cartas_dealer)):
                if valor_cartas_dealer[i] == 11:
                    valor_cartas_dealer[i] = 1

        time.sleep(1)
        print(f'= Cartas do Dealer: {', '.join(str(carta) for carta in cartas_dealer)} -> {sum(valor_cartas_dealer)}')
        
    if sum(valor_cartas_dealer) == 21:
        print('🥊 DEALER POSSUI BLACKJACK 🥊')

    if sum(valor_cartas_dealer) >= 17 and sum(valor_cartas_dealer) <= 21:
        if sum(valor_cartas_dealer) > sum(valor_cartas_jogador):

            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')
            time.sleep(1)
            print('=== ♠ Resultado ♠ ===')
            print(f'🔴 VOCÊ PERDEU por {sum(valor_cartas_dealer) - sum(valor_cartas_jogador)} ponto(s) de diferença 🔴')
            print(f'= Dinheiro perdido: R${valor_aposta:.2f} ❌')

            time.sleep(2)
            apostar_novamente()

        elif sum(valor_cartas_jogador) > sum(valor_cartas_dealer):
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')
            time.sleep(1)
            print('=== ♠ Resultado ♠ ===')
            print(f'💲 VOCÊ GANHOU por {sum(valor_cartas_jogador) - sum(valor_cartas_dealer)} ponto(s) de diferença 💲')
            print(f'= Dinheiro ganho: R${valor_aposta:.2f} ✅')

            novo_saldo = saldo() + valor_aposta*2
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

            time.sleep(2)
            apostar_novamente()
        
        else:
            print(f'♠ Suas cartas: {', '.join(str(carta) for carta in cartas_jogador)} -> {sum(valor_cartas_jogador)}')
            time.sleep(1)
            print('🚧 DEALER EMPATOU 🚧')

            novo_saldo = saldo() + valor_aposta
            with open('saldo.txt', 'w') as arq:
                arq.write(str(novo_saldo))

            print('= Valor da aposta devolvido.')
            time.sleep(2)
            apostar_novamente()

    else:
        print('♣ DEALER ESTOUROU ♣')
        print(f'= Dinheiro ganho: R${(valor_aposta):.2f} ♥')

        novo_saldo = saldo() + valor_aposta*2
        with open('saldo.txt', 'w') as arq:
            arq.write(str(novo_saldo))
            
        apostar_novamente()
        
def dobrar_cartas():
    print('Olá, mundo!')
    # Tirar o saldo da conta
    # Adicionar uma carta à mão do jogador (pedir_carta)
    # Encerrar a rodada e verificar as cartas do Dealer (parar_rodada)

cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
baralho_ordenado = [carta for carta in cartas for _ in range(4)]

baralho = baralho_ordenado.copy()
embaralhar(baralho)

verificar_arquivo()
menu()