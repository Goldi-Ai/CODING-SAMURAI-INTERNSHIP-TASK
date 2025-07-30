from board import print_board, make_move, is_full
from utils import check_winner
from minimax import best_move

def main():
    board = [0] * 9
    player, ai = 1, 2
    turn = player

    print("Tic Tac Toe — You are X, AI is O")

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Player {'X' if winner == 1 else 'O'} wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        if turn == player:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move not in range(9) or not make_move(board, move, player):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Enter a number between 1 and 9.")
                continue
        else:
            move = best_move(board, ai, player)
            make_move(board, move, ai)
            print(f"AI chose position {move + 1}")

        turn = ai if turn == player else player

if __name__ == "__main__":
    main()
