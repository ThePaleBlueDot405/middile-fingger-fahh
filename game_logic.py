WIN_CASES = {
    "RED": [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ],
    "BLUE": [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ],
}


class TicTacToe:
    def __init__(self):
        self.reset()
    def reset(self):
        self.moves = {"RED": [], "BLUE": []}
        self.turn_count = 0
        self.winner = None
        self.winning_line = None
    @property
    def current_player(self):
        if self.turn_count % 2 == 0:
            return "RED"
        else:
            return "BLUE"
    @property
    def is_draw(self):
        if self.turn_count == 9:
            if self.winner is None:
                return True
        return False
    @property
    def is_over(self):
        if self.winner is not None:
            return True
        if self.is_draw:
            return True
        return False
    def is_taken(self, index):
        if index in self.moves["RED"]:
            return True
        if index in self.moves["BLUE"]:
            return True
        return False
    def play(self, index):
        if self.is_over:
            return False
        if self.is_taken(index):
            return False
        player = self.current_player
        self.moves[player].append(index)
        self.turn_count += 1
        self.check_winner(player)
        return True
    def check_winner(self, player):
        for case in WIN_CASES[player]:
            matches = 0
            for cell in case:
                if cell in self.moves[player]:
                    matches += 1
            if matches == 3:
                self.winner = player
                self.winning_line = case
                return True
        return False
