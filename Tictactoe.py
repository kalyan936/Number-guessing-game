
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_win(board, player):
    
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    return all([cell != " " for row in board for cell in row])


def get_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter row and column numbers between 0 and 2.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row, col = get_move(board)
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
