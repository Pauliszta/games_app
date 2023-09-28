X = "x"
O = "o"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
    """Shows instructions of game"""
    print(
        """Witaj w grze "kółko i krzyżyk"! Będzie to rozgrywka między Twoim ludzkim mózgiem a komputerem. 
         Chcesz podjąć wyzwanie?
         Swoje posunięcia wskażesz poprzez wprowadzenie liczby z zakresu 0-8. 
         Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem. 
         
         0 | 1 | 2
         ---------
         3 | 4 | 5
         ---------
         6 | 7 | 8
         
         Przygotuj się. Zaczynamy?
         """
    )


def ask_yes_no(question):
    """
    Question for which answer is yes or no
    :param question:
    :return:
    """
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """
    Asks for number in right range
    :param question:
    :param low:
    :param high:
    :return:
    """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """
    Asks which player will start the game
    :return:
    """
    go_first = ask_yes_no("Czy chcesz zacząć pierwszy? (t/n): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie. ")
        human = X
        computer = O
    else:
        print("\nJa wykonuje pierwszy ruch, powodzenia!")
        computer = X
        human = O
    return computer, human


def new_board():
    """
    new game's board
    :return:
    """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """
    Shows the game's board
    :return:
    """
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "----------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "----------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """
    Creates list of correct moves
    :param board:
    :return:
    """
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """
    Shows possible winner's moves
    :param board:
    :return:
    """
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (1, 4, 7),
        (2, 4, 6),
        (0, 3, 6),
        (2, 5, 8),
    )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


def human_move(board, human):
    """
    Reads human moves
    :param board:
    :param human:
    :return:
    """
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch? (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte. Wybierz inne. Tracisz ruch!\n")
        print("\nZnakomicie...")
        return move


def computer_move(board, computer, human):
    """
    Shows computer's moves
    :param board:
    :param computer:
    :param human:
    :return:
    """
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """
    next player's move
    :param turn:
    :return:
    """
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """
    Congratulations for the winner
    :param the_winner:
    :param computer:
    :param human:
    :return:
    """
    if the_winner != TIE:
        print(the_winner, "jest zwycięzcą!\n")
    else:
        print("Remis!\n")

    if the_winner == computer:
        print("Byłem pewien, że wygram! Żegnaj!")
    elif the_winner == human:
        print("No nie! To niemożliwe! Oszukiwałeś? To się więcej nie powtórzy!")
    elif the_winner == TIE:
        print("Miałeś mnóstwo szczęścia! Udało Ci się ze mną zremisować! Świętuj ten dzień,bo więcej się nie powtórzy!")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")
