class Board:
    def __init__(self, length, width):
        self._board = [[0 for x in range(width)] for y in range(length)]

    def getCell(self, x, y, retValue):
        # print(str(x) + "(" + str(len(self._board)) + ")" + str(y) + "(" + str(len(self._board[0])) + ")")
        if x < 1 or y < 1:
            return retValue
        elif x - 1 < len(self._board) and y - 1 < len(self._board[0]):
            return self._board[x - 1][y - 1]
        else:
            return retValue

    def setCellAlive(self, x, y):
        self._board[x - 1][y - 1] = 1

    def setCellDead(self, x, y):
        self._board[x - 1][y - 1] = 0

    def getCellsAliveNearbySimple(self, x, y):
        numAlive = self.getCell(x - 1, y - 1, 0)
        return numAlive

    def getCellsAliveNearby(self, x, y):
        numAlive = self.getCell(x - 1, y - 1, 0) + \
                   self.getCell(x - 1, y, 0) + \
                   self.getCell(x - 1, y + 1, 0) + \
                   self.getCell(x, y - 1, 0) + \
                   self.getCell(x, y + 1, 0) + \
                   self.getCell(x + 1, y - 1, 0) + \
                   self.getCell(x + 1, y, 0) + \
                   self.getCell(x + 1, y + 1, 0)
        return numAlive

    def getPrintedBoard(self):
        result = ""
        for x in reversed(range(len(self._board))):
            for y in range(len(self._board[0])):
                result += str(self._board[x][y]) + " "
            result += "\n"
        return result

    def getPrintedCountBoard(self):
        result = ""
        for x in reversed(range(len(self._board))):
            for y in range(len(self._board[0])):
                result += str(self.getCellsAliveNearby(x+1, y+1)) + " "
            result += "\n"
        return result

    def flipBoard(self):
        newBoard = Board(len(self._board), len(self._board[0]))
        for x in reversed(range(len(self._board))):
            for y in range(len(self._board[0])):
                neighborsAlive = self.getCellsAliveNearby(x+1, y+1)
                if neighborsAlive < 2:
                    newBoard.setCellDead(x+1, y+1)
                elif neighborsAlive > 3:
                    newBoard.setCellDead(x+1, y+1)
                elif neighborsAlive == 3:
                    newBoard.setCellAlive(x+1, y+1)
                else:
                    newBoard.setCellAlive(x+1, y+1)
        return newBoard

