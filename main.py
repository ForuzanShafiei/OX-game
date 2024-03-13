import random
choice = 0


def print_board(board):
    for row in board:
        print(" | ".join([cell if cell is not None else " " for cell in row]))
        print("-" * 5)


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_board_full(board):
    return all([cell is not None for row in board for cell in row])


def get_empty_cells(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] is None]


def person_turn(player, board):
    global choice
    if player == "O":
        choice = int(input(f"It's your friend's turn, select an empty cell (1-9): "))
        row, col = divmod(choice - 1, 3)
    else:
        choice = int(input(f"It's your turn, select an empty cell (1-9): "))
        row, col = divmod(choice - 1, 3)

    if board[row][col] is None:
        board[row][col] = player
    else:
        print("This cell is already in use.")
        if not is_board_full(board):
            person_turn(board, player)


def computer_turn(board, player):
    print("Computer turn.")
    empty_cells = get_empty_cells(board)
    row, col = divmod(empty_cells[0][0] * 3 + empty_cells[0][1], 3)
    for cell in empty_cells:
        if col < 2 and cell == board[row][col + 1]:
            board[row][col + 1] = player
        elif col < 1 and cell == board[row][col + 2]:
            board[row][col + 2] = player
        elif row < 2 and cell == board[row + 1][col]:
            board[row + 1][col] = player
        elif row < 1 and cell == board[row + 2][col]:
            board[row + 2][col] = player
        elif row < 2 and col < 2 and cell == board[row + 1][col + 1]:
            board[row + 1][col + 1] = player
        elif row < 1 and col < 1 and cell == board[row + 2][col + 2]:
            board[row + 2][col + 2] = player
        else:
            print("This cell is already in use.")
            if not is_board_full(board):
                computer_turn(board, player)


def player_move(board, player, start):
    print_board(board)
    if start == "c":
        if player == "X":
            person_turn(player, board)
        else:
            computer_turn(board, player)
    else:
        person_turn(player, board)
    return check_winner(board, player)


def play_game():
    board = [[None for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)
    winner = None
    print('Welcome to Tic Tac Toe game. You are X.')
    start = input("Choose who you want to play with? Type 'c' for computer or 'p' for a person: ")

    while not winner and not is_board_full(board):
        for player in players:
            if player_move(board, player, start):
                winner = player
                break

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")


play_game()
