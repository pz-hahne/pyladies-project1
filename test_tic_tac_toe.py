import tic_tac_toe

def winning_condition(board):
    if "xxx" in board: 
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" in board: 
        return "-"
    else:  
        return "!"
    
#create at least 5 different tests for the behavior of the function.

def test_winning_condition_x():
    board = tic_tac_toe.computer_choice('--------------------')
    assert len(board) == 20
    assert board.count('x') == 3
    assert "xxx" in board

#create at least 2 different tests for move function

def move(board, mark, position):
  new_board = board[:position] + mark + board[position+1:]
  return new_board

def test_move_to_empty_space():
    board = tic_tac_toe.computer_choice('--------------------')
    assert len(board) == 20
    assert board.count('x') == 1
    assert board.count('-') == 19
    


# Answers to questions: 
    # Python module = one file; python package as multiple files/ python packages are made up of modules
    # 
    # Exceptions as a way to program specific kinds of errors into code to anticipate a problem that might come up for the user. 
    #
    # Benefits of testing: 