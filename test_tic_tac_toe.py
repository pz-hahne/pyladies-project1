from tic_tac_toe import winning_condition

#create at least 5 different tests for the behavior of the function.

def test_winning_condition():
    # Test case 1: X wins
    board = "xxx--ooo"
    assert winning_condition(board) == "x"

    # Test case 2: O wins
    board = "xx-oooxx"
    assert winning_condition(board) == "o"

    # Test case 3: Draw
    board = "xoxoxoxox"
    assert winning_condition(board) == "-"

    # Test case 4: No winner yet
    board = "xx---ooo"
    assert winning_condition(board) == "!"

    # Test case 5: Empty board
    board = "---------"
    assert winning_condition(board) == "!"

#create at least 2 different tests for move function
from tic_tac_toe import move

def test_move_with_x():
    # Test case 1: Make a move with "x"
    initial_board = "---------"
    new_board = move(initial_board, "x", 2)
    expected_board = "--x------"
    assert new_board == expected_board

def test_move_with_o():
    # Test case 2: Make a move with "o"
    initial_board = "--x------"
    new_board = move(initial_board, "o", 5)
    expected_board = "--xo-----"
    assert new_board == expected_board

# Answers to questions: 
    # Python module = one file; python package as multiple files/ python packages are made up of modules
    # 
    # Exceptions as a way to program specific kinds of errors into code to anticipate a problem that might come up for the user. 
    # create new exception: create new class that functions as exception, throw: , catch: 
    # Benefits of testing: ensure smoother running of programmes, realise problems that progammer might not have anticipated, 