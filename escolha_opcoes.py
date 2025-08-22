def formatar_opcoes(opcoes):
    opcoes = list(map(str, opcoes))
    if len(opcoes) == 1:
        return opcoes[0]
    return ", ".join(opcoes[:-1]) + " ou " + opcoes[-1]

def escolher_opcao(opcoes_validas):
    while True:
        try:
            opcao = int(input('♣ Opção: '))
            if opcao in opcoes_validas:
                return opcao
            else:
                print(f'# Opção inválida! Por favor, insira {formatar_opcoes(opcoes_validas)}.')
        except ValueError:
            print(f'# Opção inválida! Por favor, insira {formatar_opcoes(opcoes_validas)}.')
