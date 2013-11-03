class Game(object):
    """The Ultimate game class."""

    def __init__(self):
        self.p1 = Player(1, 'x')
        self.p2 = Player(2, 'o')
        self.current_player = self.p1

    def has_winner(self):
        pass

    def get_board(self):
        pass

    def next_move(self):
        pass

    def message(self, msg):
        pass

    def run(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        return self.get_board()

class Board(object):
    """Represents a standard 3x3 tic-tac-toe board."""
    def __init__(self):
        self.spaces = [i for i in range(9)]
        self.avail = set(self.spaces)
        self.won = False    # make property

    def check_if_won(self):
        win_conds = {self.spaces[0] == self.spaces[1] == self.spaces[2],
                     self.spaces[3] == self.spaces[4] == self.spaces[5],
                     self.spaces[6] == self.spaces[7] == self.spaces[8],
                     self.spaces[0] == self.spaces[3] == self.spaces[6],
                     self.spaces[1] == self.spaces[4] == self.spaces[7],
                     self.spaces[2] == self.spaces[5] == self.spaces[8],
                     self.spaces[0] == self.spaces[4] == self.spaces[8],
                     self.spaces[2] == self.spaces[4] == self.spaces[6]}

        self.won = True in win_conds

    def make_move(self, index, player):
        """Mark the space at the given index with the given player's symbol"""
        if index in self.avail:
            self.spaces[index] = player.symbol
            self.avail.remove(index)
            self.check_if_won(player)
        else:
            raise Exception("Invalid Move! >:(")

    def __repr__(self):
        return self.spaces

    def __str__(self):
        divider = "-------"
        row1 = "{}|{}|{}".format(*self.spaces[:3]) # TODO: stop printing initialized numbers


class Player(object):
    """The player object"""
    def __init__(self, turn, symbol):
        self.turn = turn    # 1st or 2nd
        self.symbol = symbol

    def __repr__(self):
        return self.symbol


if __name__ == "__main__":
    Game().run()
