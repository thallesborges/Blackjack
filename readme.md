# ♠ Blackjack

Um jogo de Blackjack em Python que simula a experiência de um cassino, permitindo gerenciar saldo, fazer apostas e jogar contra o dealer. Desenvolvido com uma interface textual intuitiva e funcionalidades clássicas do jogo.

---

## 📖 Visão Geral

O **Blackjack** é um jogo de cartas onde o jogador compete contra o dealer, tentando alcançar uma soma de cartas próxima de 21 sem ultrapassá-la. Este projeto implementa as regras padrão do jogo, com recursos como depósitos, apostas, divisão de cartas, seguro e Blackjack natural.

---

## ✨ Funcionalidades

- **Gerenciamento de Saldo**: Saldo armazenado em `saldo.txt`, com opção de depósito.
- **Sistema de Apostas**: Validação para apostas positivas e saldo suficiente.
- **Mecânicas do Jogo**: Suporta ações como pedir carta, parar, dobrar e dividir (parcialmente implementado).
- **Manuseio de Cartas**: Baralho embaralhado com valuation correta para ases e cartas de face.
- **Interface de Usuário**: Interface textual clara com prompts e atualizações do estado do jogo.
- **Compatibilidade**: Funciona em Windows e sistemas Unix (limpeza de tela adaptada).

---

## 📋 Requisitos

- **Python 3.x**
- Bibliotecas padrão: `random`, `os`, `platform`, `time`, `sys`

Nenhuma dependência externa é necessária.

---

## 📂 Estrutura de Arquivos

- `main.py`: Script principal com toda a lógica do jogo.
- `saldo.txt`: Arquivo gerado automaticamente para armazenar o saldo do jogador (inicializado em 0, se vazio ou inexistente).

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.

2. Salve o código fornecido como `main.py`.

3. Execute o script com o comando:

   ```bash
   python main.py
   ```

4. Siga os prompts na tela para navegar pelo menu, depositar fundos, apostar e jogar.

---

## 🎮 Como Jogar

1. **Menu Principal**:
   - Escolha entre apostar, depositar ou sair.
2. **Depósito**:
   - Adicione fundos ao saldo, salvos em `saldo.txt`.
3. **Aposta**:
   - Insira um valor de aposta (deve ser positivo e não exceder o saldo).
4. **Jogo**:
   - Receba duas cartas e veja a carta aberta do dealer.
   - Escolha entre pedir carta, parar, dobrar ou dividir (se aplicável).
   - O dealer compra cartas até atingir pelo menos 17.
   - O resultado (vitória, derrota, Blackjack) é determinado pelas regras padrão.
5. **Casos Especiais**:
   - **Blackjack Natural**: 21 com duas cartas (ás + carta de valor 10) paga 1.5x a aposta.
   - **Seguro**: Oferecido se a carta aberta do dealer for um ás, cobrindo perdas em caso de Blackjack do dealer.
   - **Divisão/Dobrar**: Disponível em condições específicas (divisão para pares, dobrar para mãos iniciais).

---

## 🔧 Funções Principais

- `embaralhar(baralho)`: Embaralha o baralho.
- `verificar_arquivo()`: Verifica/cria `saldo.txt` e inicializa o saldo.
- `menu()`: Exibe o menu principal e gerencia as opções do usuário.
- `saldo()`: Lê o saldo atual de `saldo.txt`.
- `limpar_tela()`: Limpa o console (compatível com Windows/Unix).
- `depositar()`: Gerencia depósitos no saldo.
- `apostar()`: Valida e processa apostas.
- `jogar(valor_aposta)`: Lógica principal para distribuição de cartas e estado inicial.
- `menu_aposta(...)`: Gerencia ações do jogador durante a rodada.
- `pedir_carta(...)`: Adiciona uma carta à mão do jogador.
- `parar_rodada(...)`: Gerencia o turno do dealer e determina o resultado.

---

## ℹ️ Notas

- As funções `dividir()` e `dobrar_cartas()` estão referenciadas, mas não implementadas no código fornecido.
- O jogo usa um único baralho, embaralhado no início de cada sessão.
- Ases valem 11 por padrão, mas mudam para 1 se a mão ultrapassar 21.
- Inclui tratamento básico de erros para entradas inválidas (ex.: valores não numéricos).

---

## ⚠️ Limitações

- As funcionalidades de divisão e dobrar estão incompletas.
- Interface exclusivamente textual, sem elementos gráficos.
- O baralho não é reembaralhado durante a sessão, o que pode afetar rodadas longas.
- Suporte apenas para um jogador contra o dealer.
- Sem validação avançada para casos extremos (ex.: arquivo `saldo.txt` corrompido).

---

## 🌟 Melhorias Futuras

- Implementar as funções `dividir()` e `dobrar_cartas()`.
- Adicionar reembaralhamento do baralho após um número de rodadas.
- Criar uma interface gráfica com bibliotecas como **Pygame** ou **Tkinter**.
- Melhorar o tratamento de erros para casos específicos.
- Suportar múltiplos baralhos, como em cassinos reais.

---

## 📜 Licença

Este projeto é fornecido sem licença, para fins educacionais.

---

Desenvolvido com 💻 e ♠