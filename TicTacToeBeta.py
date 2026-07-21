import random

board = [" "] * 9

def show_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

print("🎮 TIC TAC TOE")
print("Choose a square from 1 to 9")

while True:
    show_board()

    move = int(input("❌ Your move (1-9) : ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("❌ Invalid square !")
        continue

    board[move] = "X"

    if check_winner("X"):
        show_board()
        print("🏆 YOU WIN !")
        break

    if " " not in board:
        show_board()
        print("🤝 DRAW !")
        break

    ai_move = random.choice([i for i in range(9) if board[i] == " "])
    board[ai_move] = "O"

    print(f"🤖 IA plays in square {ai_move + 1}")

    if check_winner("O"):
        show_board()
        print("💀 IA WINS !")
        break

    if " " not in board:
        show_board()
        print("🤝 DRAW !")
        break