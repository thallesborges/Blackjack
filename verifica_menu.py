def menu_aposta():
    if sum(cartas) < 21:
        if cartas[0] == cartas[1]:
            print('1. Dividir')
            print('2. Parar')
            print('3. Pedir')
            print('4. Dobrar')

            opcao = int(input('♠ Opção: '))
            if opcao == 1:
                dividir()
            elif opcao == 2:
                print('Parando...')
            elif opcao == 3:
                print('Pedindo...')
            else:
                print('Dobrando...')

        else:
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
        print('= Valor recebido: R$') # Soma do valor da aposta
    
    else: 
        print('Estourou! 💣')
        # Jogar novamente?
    
def parar():
    print('= Você optou por parar a rodada, vamos verificar as cartas do Dealer.')

def dividir():
    print('= Você optou por dividir, entregando novas cartas: ')

    deckUm = [cartas[0]]
    deckDois = [cartas[1]]
    nova_carta = int(input('1° Carta = ')) # Será tirado do baralho
    deckUm.append(nova_carta)
    nova_carta = int(input('2° Carta = ')) # Será tirado do baralho
    deckDois.append(nova_carta)

    print(f'= Primeira mão: {deckUm[0]} e {deckUm[1]}')
    print(f'= Segunda mão: {deckDois[0]} e {deckDois[1]}')

    print(f'= Primeira mão ({deckUm[0]}, {deckUm[1]}): ')
    if sum(deckUm) == 21:
        print('= ♠ Blackjack ♠')
        print('= Valor recebido: R$') # Soma do valor da aposta
    else:
        print('1. Pedir')
        print('2. Parar')
    
    opcao = int(input('♠ Opção = '))
    if opcao == 1:
        carta = int(input('Carta: '))
        deckUm.append(carta)
        if sum(deckUm) > 21:
            print('= Estourou! 💣')
        elif sum(deckUm) == 21:
            print('= ♠ Blackjack ♠')
        else:
            print('1. Pedir')
            print('2. Parar')
    else:
        print('= Primeira mão encerrada!')
    
    print(f'= Segunda mão ({deckDois[0]}, {deckDois[1]}): ')
    if sum(deckDois) == 21:
        print('= ♠ Blackjack ♠')
        print('= Valor recebido: R$') # Soma do valor da aposta
    else:
        print('1. Pedir')
        print('2. Parar')
    
    opcao = int(input('♠ Opção = '))
    if opcao == 1:
        carta = int(input('Carta: '))
        deckDois.append(carta)
        while sum(deckDois) < 21:
            print('1. Pedir')
            print('2. Parar')
            opcao = int(input('♠ Opção: '))
            if opcao == 1:
                carta = int(input('♠ Carta: '))
                deckDois.append(carta)
        if sum(deckDois) > 21:
            print('💣 Estourou! ')
        else:
            print('🤑 Blackjack!')
        
    else:
        print('= Segunda mão encerrada!')
    
def verificar_dealer():
    print('Aqui será o processo pra avaliar as cartas do Dealer')

cartas = []
for i in range(2):
    valor = int(input(f'Carta {i+1} = '))
    cartas.append(valor)

print(cartas)
menu_aposta()