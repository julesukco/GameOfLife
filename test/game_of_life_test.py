import unittest

from Board import Board
from Runner import Runner


class GameOfLifeTest(unittest.TestCase):
    def test_should_do_board_setup(self):
        board = Board(10, 10)
        self.assertEqual(board.getCell(0, 0, None), None)

    def test_should_do_board_setup_at_top(self):
        board = Board(10, 5)
        self.assertEqual(board.getCell(10, 5, None), 0)

    def test_should_do_board_setup_at_edge(self):
        board = Board(10, 5)
        self.assertEqual(board.getCell(10, 6, None), None)

    def test_should_init_one_cell(self):
        board = Board(10, 10)
        board.setCellAlive(4, 5)
        self.assertEqual(board.getCell(4, 5, 0), 1)

    def test_should_count_cells_around_middle(self):
        board = Board(10, 10)
        board.setCellAlive(4, 5)
        # board.printBoard()
        self.assertEqual(board.getCellsAliveNearby(5, 5), 1)

    def test_should_count_cells_all_around(self):
        board = Board(10, 10)
        board.setCellAlive(4, 4)
        board.setCellAlive(5, 4)
        board.setCellAlive(6, 4)
        board.setCellAlive(4, 5)
        board.setCellAlive(6, 5)
        board.setCellAlive(4, 6)
        board.setCellAlive(5, 6)
        board.setCellAlive(6, 6)
        self.assertEqual(board.getCellsAliveNearby(5, 5), 8)

    def test_should_count_cells_at_bottom(self):
        board = Board(10, 10)
        board.setCellAlive(1, 2)
        board.setCellAlive(2, 2)
        board.setCellAlive(2, 1)
        self.assertEqual(board.getCellsAliveNearby(1, 1), 3)

    def test_should_count_cells_at_top(self):
        board = Board(10, 10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        self.assertEqual(board.getCellsAliveNearby(10, 10), 3)

    def test_should_count_cells_at_top_left(self):
        board = Board(10, 10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        self.assertEqual(board.getCellsAliveNearby(2, 10), 0)

    def test_should_count_cells_at_mid_top(self):
        board = Board(10, 10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        self.assertEqual(board.getCellsAliveNearby(8, 10), 2)

    def test_should_get_printed_board(self):
        board = Board(10,10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        output = board.getPrintedBoard()
        self.assertEqual(output,  "0 0 0 0 0 0 0 0 1 0 \n" + \
                                  "0 0 0 0 0 0 0 0 1 1 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n" +  \
                                  "0 0 0 0 0 0 0 0 0 0 \n")
        # print(output)

    def test_should_get_printed_count_board(self):
        board = Board(10,10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        output = board.getPrintedCountBoard()
        self.assertEqual("0 0 0 0 0 0 0 2 2 3 \n" + \
                         "0 0 0 0 0 0 0 2 2 2 \n" +  \
                         "0 0 0 0 0 0 0 1 2 2 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n" +  \
                         "0 0 0 0 0 0 0 0 0 0 \n", output)
        # print(output)

    def test_should_do_simple_cell_count(self):
        board = Board(10,10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        self.assertEqual(board.getCellsAliveNearbySimple(10,10), 1)

    def test_should_flip_board(self):
        board = Board(10,10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        board.setCellAlive(8, 8)
        board.setCellAlive(6, 6)
        newBoard = board.flipBoard()
        output = newBoard.getPrintedBoard()
        self.assertEqual("0 0 0 0 0 0 0 1 1 1 \n" +
                         "0 0 0 0 0 0 0 1 1 1 \n" +
                         "0 0 0 0 0 0 0 0 1 1 \n" +
                         "0 0 0 0 0 0 1 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n", output)

    def test_should_flip_board_twice(self):
        board = Board(10,10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        board.setCellAlive(8, 8)
        board.setCellAlive(6, 6)
        board = board.flipBoard()
        board = board.flipBoard()
        output = board.getPrintedBoard()
        self.assertEqual("0 0 0 0 0 0 1 1 0 1 \n" +
                         "0 0 0 0 0 0 1 0 0 0 \n" +
                         "0 0 0 0 0 0 1 0 0 1 \n" +
                         "0 0 0 0 0 0 0 1 1 1 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n", output)

    def test_should_run_controller(self):
        board = Board(10,10)
        board.setCellAlive(9, 10)
        board.setCellAlive(9, 9)
        board.setCellAlive(10, 9)
        board.setCellAlive(8, 8)
        board.setCellAlive(6, 6)
        runner = Runner(board)
        board = runner.run(2)
        output = board.getPrintedBoard()
        self.assertEqual("0 0 0 0 0 0 1 1 0 1 \n" +
                         "0 0 0 0 0 0 1 0 0 0 \n" +
                         "0 0 0 0 0 0 1 0 0 1 \n" +
                         "0 0 0 0 0 0 0 1 1 1 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n" +
                         "0 0 0 0 0 0 0 0 0 0 \n", output)


if __name__ == '__main__':
    unittest.main()

