class Disc:
    def __init__(self, color="Black"):
        self.color = color

    def __eq__(self, value: object):
        return (self.color == value.color)

    def __repr__(self):
        return self.color


class Player:
    def __init__(self, tp, color):
        self.tp = tp
        self.color = color

    def __repr__(self):
        return f"Player {self.tp}"

    def __eq__(self, other):
        return self.color == other.color


init_board = [[None]*8, [None]*8, [None]*8, [None, None, None, Disc("Black"), Disc("White"), None, None, None], [
    None, None, None, Disc("White"), Disc("Black"), None, None, None], [None]*8, [None]*8, [None]*8, [None]*8]
players = [Player(1, "Black"), Player(2, "White")]
gameover = False


def move(tp, board_state, x, y):
    if boardstate[x][y] == None:
        board_state[x][y] = Disc(tp.color)
    return board_state


def print_board(board_state):
    for i in range(len(board_state)):
        print(board_state[i])


def player_turn(tp, boardstate):

    print(f"{tp} Turn!")
    x = int(input("Please Enter a Row: "))
    y = int(input("Please Enter a Column: "))
    new_state = move(tp, boardstate, x, y)
    return boardstate


def switch_turn(tp):
    if tp == players[0]:
        return players[1]
    else:
        return players[0]


if __name__ == '__main__':
    print("Welcome To Othello!")
    print("Player 1 Will Play As Black and Player 2 as White")
    boardstate = init_board
    tp = players[0]
    while not gameover:
        print_board(boardstate)
        boardstate = player_turn(tp, boardstate)
        tp = switch_turn(tp)
