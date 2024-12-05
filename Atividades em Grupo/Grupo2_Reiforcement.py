import math
import random

# Função para verificar se alguém venceu
def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]
    return None

# Função para verificar se o tabuleiro está cheio
def is_board_full(board):
    return ' ' not in board

# Função Minimax
def minimax(board, is_maximizing, player):
    minimaxBot = 'O' if player == 'X' else 'X'
    winner = check_winner(board)
    if winner == minimaxBot:
        return 1
    if winner == player:
        return -1
    if is_board_full(board):
        return 0    
    

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = minimaxBot
                score = minimax(board, False, player)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                score = minimax(board, True, player)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# Função para encontrar o melhor movimento para o jogador X (Minimax)
def best_move(board, player):
    minimaxBot = 'O' if player == 'X' else 'X'
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = minimaxBot
            score = minimax(board, False, player)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Função para imprimir o tabuleiro
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('|'.join(row))
        print("-" * 5)

# Função principal para jogar contra o Minimax com sorteio
def play_game():
    board = [' '] * 9
    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)

    player = input("Você quer ser X ou O? ").upper()
    if player not in ['X', 'O']:
        print("Escolha inválida! O padrão será X.")
        player = 'X'

    ai = 'O' if player == 'X' else 'X'

    # Sorteio para decidir quem começa
    first_player = random.choice(['Você'])
    print(f"{first_player} começa!")

    if first_player == 'Você':
        while True:
            # Sua jogada
            human_turn(board, player)
            if check_game_over(board):
                break

            # Minimax (IA) joga
            ai_turn(board, ai, player)
            if check_game_over(board):
                break
    else:
        while True:
            # Minimax (IA) joga
            ai_turn(board, ai, player)
            if check_game_over(board):
                break

            # Sua jogada
            human_turn(board, player)
            if check_game_over(board):
                break

# Função para a jogada do jogador humano
def human_turn(board, player):
    while True:
        try:
            move = int(input(f"Sua vez ({player}). Escolha uma posição (0-8): "))
            if board[move] == ' ':
                board[move] = player
                break
            else:
                print("Posição ocupada, escolha outra.")
        except (ValueError, IndexError):
            print("Escolha um número válido entre 0 e 8.")
    print_board(board)

# Função para a jogada do Minimax (IA)
def ai_turn(board, ai, player):
    print(f"Turno do {ai} (IA Minimax).")
    move = best_move(board, player)
    board[move] = ai
    print_board(board)

# Função para verificar se o jogo acabou
def check_game_over(board):
    winner = check_winner(board)
    if winner:
        print(f"{winner} venceu!")
        return True
    elif is_board_full(board):
        print("Empate!")
        return True
    return False

# Inicia o jogo
play_game()
