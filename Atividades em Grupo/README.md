## 🖥 Atividades Em Grupo

Reinforcement Learning: https://github.com/klaytoncastro/idp-machinelearning/tree/main/reinforcement  
RNA (Redes Neurais Artificiais): https://github.com/klaytoncastro/idp-machinelearning/tree/main/rna  

## 🕹️ Reinforcement Learning (Minimax)

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

# Projeto de Redes Neurais Artificiais (RNA)

Este projeto aborda a implementação e o uso de Redes Neurais Artificiais (RNA) para resolver problemas específicos utilizando frameworks como **TensorFlow** ou **PyTorch**. O trabalho foi desenvolvido como parte das atividades práticas do curso de Machine Learning.

## Estrutura do Repositório

- **`Grupo1_RNA.ipynb`**: Notebook principal contendo o código para implementação das Redes Neurais Artificiais.
- **`dataset.csv`** (exemplo): Conjunto de dados utilizado para treinar e avaliar as RNAs. 

## Objetivo

O objetivo principal deste projeto foi:
- Implementar Redes Neurais Artificiais para um problema específico.
- Treinar e avaliar a performance do modelo utilizando métricas apropriadas.
- Explorar diferentes arquiteturas de redes neurais para observar o impacto em sua performance.

## Etapas do Projeto

### 1. Carregamento e Preparação dos Dados
- **Leitura dos Dados**:
  - Os dados foram carregados de um arquivo CSV e analisados.
- **Pré-processamento**:
  - Normalização dos dados para garantir que todas as variáveis estivessem na mesma escala.
  - Divisão do dataset em conjuntos de treino e teste.

### 2. Implementação do Modelo RNA
- **Biblioteca Utilizada**: TensorFlow ou PyTorch.
- **Arquitetura da Rede**:
  - Camadas densamente conectadas (Dense Layers).
  - Funções de ativação utilizadas: `ReLU`, `Sigmoid`, ou outras dependendo do problema.
  - Otimizador: Adam ou SGD (Stochastic Gradient Descent).
  - Função de perda: CrossEntropy (para classificação) ou MSE (para regressão).

### 3. Treinamento e Avaliação
- **Treinamento**:
  - Configurado para rodar por um número definido de épocas.
  - Monitoramento de métricas como acurácia, perda (loss) e validação.
- **Avaliação**:
  - Métricas calculadas no conjunto de teste, como Acurácia, Precision, Recall, F1-Score.
  - Gráficos de perda e acurácia foram gerados para avaliar o desempenho.

### 4. Resultados e Análise
- **Desempenho da Rede**:
  - A rede neural conseguiu aprender padrões significativos nos dados.
  - Resultados foram comparados com abordagens tradicionais (como regressão logística ou árvores de decisão).
- **Visualizações**:
  - Gráficos de convergência (loss/accuracy).
  - Comparação entre valores reais e previstos.

### 5. Conclusões
- **Conclusões Gerais**:
  - O modelo apresentou bom desempenho para a tarefa proposta.
  - Redes neurais foram capazes de capturar padrões complexos que algoritmos tradicionais não conseguiram.
- **Limitações**:
  - O tempo de treinamento foi elevado devido ao tamanho do dataset e à complexidade da rede.
  - Testes adicionais poderiam ser realizados com arquiteturas mais avançadas, como Redes Convolucionais (CNNs) ou Redes Recorrentes (RNNs).

## Ferramentas Utilizadas

- **Linguagens/Bibliotecas**:
  - Python
  - TensorFlow ou PyTorch
  - pandas, numpy
  - matplotlib, seaborn
- **Ambiente de Desenvolvimento**:
  - Jupyter Notebook
 
## Grupo
- Fábio
- Sara
- Arthur
- Felipe Barroso
- Lucas Narita

</details>

---
