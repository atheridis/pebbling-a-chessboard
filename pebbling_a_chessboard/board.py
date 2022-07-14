class Board:
    def __init__(self):
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board[0][0] = 1
        self.board[0][1] = 1
        self.board[1][0] = 1
        self.win = False
        self.print_board()

    def _expand_board(self, units=1):
        for i in range(units):
            # add column
            self.board.append([0 for _ in range(len(self.board[0]))])

            # add row
            for row in self.board:
                row.append(0)

    def play(self, posx, posy):
        if self.board[posx][posy] == 1:
            if self.board[posx + 1][posy] == 0 and self.board[posx][posy + 1] == 0:
                self.board[posx + 1][posy] = 1
                self.board[posx][posy + 1] = 1
                self.board[posx][posy] = 0

                if (
                    posx + 1 == len(self.board) - 1
                    or posy + 1 == len(self.board[posx]) - 1
                ):
                    self._expand_board()
        self.print_board()
        self._check_win_con()

    def _check_win_con(self):
        if self.board[0][0] + self.board[0][1] + self.board[1][0] == 0:
            self.win = True

    def print_board(self):
        for row in self.board:
            print(row)

        print()
