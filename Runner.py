class Runner:
    def __init__(self, board):
        self._board = board

    def run(self, iterations):
        for i in range(iterations):
            newBoard = self._board.flipBoard()
            self._board = newBoard
        return self._board
