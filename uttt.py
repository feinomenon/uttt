class Game(object):
    """The Ultimate game class."""

    def __init__(self):
        self.p1 = Player('x')
        self.p2 = Player('o')
        self.current_player = None  # self.decide_order()
        self.subboards = [Board() for _ in range(9)]
        self.mainboard = Board()

    def decide_order(self):
        # TODO: Add random option
        text = "Who would like to go first? (1 / 2): "
        while True:
            player = input(text)
            if player == "1":
                return self.p1
            elif player == "2":
                return self.p2
            else:
                print("Please select either 1 or 2")

    def has_winner(self):
        pass

    def get_board(self):
        pass

    def next_move(self):
        pass

    def message(self, msg):
        pass

    def run(self):
        self.current_player = self.decide_order()
        # TODO: Implement the main game loop
        while True:
            print("Nyaa~")

    def __repr__(self):
        pass

    def __str__(self):
        return self.get_board()


class Board(object):
    """Represents a standard 3x3 tic-tac-toe board."""
    def __init__(self):
        self.spaces = [" " for i in range(9)]
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
        return str(self.spaces)

    def __str__(self):
        # TODO: List comprehensions yo
        divider = "-----"
        row1 = "{}|{}|{}".format(*self.spaces[:3])
        row2 = "{}|{}|{}".format(*self.spaces[3:6])
        row3 = "{}|{}|{}".format(*self.spaces[6:])
        return "\n".join([row1, divider, row2, divider, row3])


# Is this class even necessary?
# Probably not. It should be removed.
class Player(object):
    """The player object"""
    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return self.symbol


if __name__ == "__main__":
    Game().run()
