# board
# display board
# play game
# handle turn
# check Win
# check rows
# check col
# check Dia
# check tie
# flip player

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_going = True
# who won?
winner = None
# whos turn?
current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    # display the initial board
    display_board()
    while game_going:
        handle_turn(current_player)
        check_if_game_over()
        # flipplayer
        flip_player()
    # game_ended
    if winner == "X" or winner == "O":
        print(winner + "won")
    elif winner == None:
        print("tie")


def handle_turn(player):
    print(player + " 's Turn")
    position = input("chose a position from 1 to 9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input, Chose a correct Position:")

        # type casting string to int and subracting one to match array elements with position.
        position = int(position) - 1
        if board[position] == "-":
            valid = True

        else:
            print("Wrong Move,Try Again!")
    board[position] = player

    display_board()


def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    global winner

    row_winner = check_rows()
    cols_winner = check_cols()
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif cols_winner:
        winner = cols_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None


def check_rows():
    # Use gloabal variable
    global game_going
    # check if the there are three same elements
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_going = False
    # Return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_cols():
    # use gloabal variable
    global game_going
    # check if the there are three same elements
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_going = False
    # Return the winner X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return

    # check cols


def check_diag():
    # set global variable
    global game_going
    # check diag
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"

    if dia_1 or dia_2:
        game_going = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
    return


def check_if_tie():
    global game_going
    if "-" not in board:
        game_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()