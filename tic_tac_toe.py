class TicTacToe:
    """Managemetn of a Tic-Tac-Toe game (does not do strategy)"""
    def __init__(self):
        """Start a new game"""
        self._board = [[' ']*3 for j in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        "Put an X Or O mark at position (i,j) for next player's turn"
        if not(0 <= i <= 2 and 0 <= j <=2)
            raise ValueError('Incalid board postion')
        if self._board[i][j] != ' ':
            raise ValueError('Board postion occupied')
        if self.winner() is not None:
            raise ValueError('Game is alreay complete')
        self._board[i][j] = self._player
        if self._board == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self, mark):
        """Check whether the board config is a win for the given player"""
        board = self._board
        win_config = [[(0,0), (0,1), (0,2)],
                      [(1,0), (1,1), (1,2)],
                      [(2,0), (2,1), (2,2)],
                      [(0,0), (1,0), (2,0)],
                      [(0,1), (1,1), (2,1)],
                      [(0,2), (1,2), (2,2)],
                      [(0,0), (1,1), (2,2)],
                      [(0,2), (1,1), (2,0)],]
        for position in win_config:
            if mark*3 == position[0][0]:
                return True

    def winner(self):
        """Return mark of winning player, or None to indicate a tie"""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None
    def __str__(self):
        """Return string representation of current game board."""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n------\n'.join(rows)

if __name__ == '__main__':
    game = TicTacToe()
    game.mark(1,1); game.mark(0,2)
