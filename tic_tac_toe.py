board = "--------------------"
mark_player1 = "x"
mark_player2 = "o"

def winning_condition(board):
    if "xxx" in board: 
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" in board: 
        return "-"
    else:  
        return "!"

import random
computer_choice = random.randrange(1,19)

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    return board[:position - 1] + mark + board[position:]

# Step 5: 1D_tictactoe function with alternate calls 
def tic_tac_toe_1d():
    """Starts the game
    It creates an empty board and runs player_move and computer_move alternately
    until the game is finished.
    """
    
    board = "--------------------"
    mark_player1 = "x"
    mark_player2 = "o"

    while "-" in board:
        user_move = int(input("To which position do you want to move your mark? "))
        computer_choice = random.randrange(1,19)

        if user_move < 21: 
            board = move(board, mark_player1, user_move)
            print(board)
        elif (user_move == computer_choice or board[user_move] != "-"): 
            print(f"Both players selected {user_move}.You can't move to a spot that's already occupied!")
            user_move = int(input("Please select a new position: "))
            board = move(board, mark_player1, user_move)
            print(board)
        else:
            print("This move is outside the board! Please choose a position between 1 and 20. ")
    
        while (computer_choice == user_move or board[computer_choice] != "-"):
            print(f"The computer selected {computer_choice}.")
            print(f"Both players selected {computer_choice}.You can't move to a spot that's already occupied!")
            computer_choice = random.randrange(1,19)

        if (computer_choice != user_move) and (board[computer_choice] == "-"): 
            print(f"The computer selected {computer_choice}.")
            board = move(board, mark_player2, computer_choice)
            print(board)

        if "xxx" in board: 
            print("x won!")
            break
        elif "ooo" in board:
            print("o won!")
            break
        elif "-" in board:
            print("The game continues.")
        else: 
            print("No one won!")
            break

