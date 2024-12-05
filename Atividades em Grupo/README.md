## 🖥 Atividades Em Grupo

Reinforcement Learning: https://github.com/klaytoncastro/idp-machinelearning/tree/main/reinforcement  
RNA (Redes Neurais Artificiais): https://github.com/klaytoncastro/idp-machinelearning/tree/main/rna  
Rules (Regras de Associação): https://github.com/klaytoncastro/idp-machinelearning/tree/main/rules  

## 🕹️ Jogo da Velha com Minimax

<details>
Este projeto implementa o clássico jogo da velha utilizando o algoritmo **Minimax** para criar uma inteligência artificial (IA) capaz de jogar contra um humano. A aplicação foi desenvolvida como parte do trabalho do **Grupo 2** no estudo de algoritmos de busca em jogos.

---

## 📚 Descrição do Projeto

A aplicação apresenta:
1. **Tabuleiro do Jogo da Velha** em um layout baseado em texto.
2. Um sistema para o jogador humano escolher entre os símbolos `X` e `O`.
3. O uso do algoritmo **Minimax** para calcular o melhor movimento para a IA.
4. Uma mecânica de sorteio para definir quem começa o jogo.

O objetivo principal é demonstrar o funcionamento do **Minimax**, um algoritmo amplamente utilizado em jogos de tabuleiro para determinar a jogada ótima.

---

## 🔧 Estrutura do Código

### Funções Principais
- **`check_winner(board)`**: Verifica se há um vencedor no jogo.
- **`is_board_full(board)`**: Determina se o tabuleiro está completamente preenchido (empate).
- **`minimax(board, is_maximizing, player)`**: Implementação do algoritmo Minimax para explorar todas as possibilidades de jogadas e escolher a melhor.
- **`best_move(board, player)`**: Calcula o melhor movimento da IA com base no Minimax.
- **`print_board(board)`**: Exibe o estado atual do tabuleiro.
- **`play_game()`**: Controla o fluxo principal do jogo, alternando entre o humano e a IA.
- **`human_turn(board, player)`**: Permite que o humano faça uma jogada.
- **`ai_turn(board, ai, player)`**: Executa a jogada da IA.
- **`check_game_over(board)`**: Verifica se o jogo terminou (vitória ou empate).

---

## 🧠 Como o Algoritmo Minimax Funciona

O **Minimax** avalia todas as jogadas possíveis no tabuleiro e atribui um valor a cada cenário:
- **Vitória do oponente**: Retorna `-1`.
- **Vitória da IA**: Retorna `1`.
- **Empate**: Retorna `0`.

A IA maximiza suas chances de vencer enquanto minimiza as chances do oponente. Este processo envolve chamadas recursivas para avaliar todos os cenários possíveis até o final do jogo.

### Exemplo de Execução do Minimax
1. O tabuleiro atual é avaliado.
2. A IA simula todas as jogadas possíveis.
3. Cada resultado é ponderado para encontrar a jogada ótima.

---

## 🚀 Grupo do Trabalho

- Mariana
- Fábio
- Sara
- Arthur
- Felipe Barroso **(Eu)**
- Igor
- Eduardo
- Pedro Calil

</details>

## 🧠 RNA (Redes Neurais Artificiais)

<details>



</details>

## 🚩 Rules (Regras de Associação)

<details>



</details>
