import unittest

from graphics import Maze


class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_no_window(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        self.assertEqual(
            m1._Maze__win,
            None
        )

class TestBreakEntryAndExit(unittest.TestCase):
    def test_break_entry_and_exit(self):
        m1 = Maze(0, 0, 0, 0, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertEqual(
            len(m1._Maze__cells),
            0
        )

class TestResetVisited(unittest.TestCase):
    def test_reset_visited(self):
        m1 = Maze(0, 0, 20, 20, 5, 5)
        m1._Maze__reset_cells_visited()
        self.assertListEqual(
            [
                m1._Maze__cells[0][0].visited,
                m1._Maze__cells[m1._Maze__nums_cols // 2][m1._Maze__nums_rows // 2].visited,
                m1._Maze__cells[m1._Maze__nums_cols - 1][m1._Maze__nums_rows - 1].visited,
            ],
            [
                False,
                False,
                False
            ]
        )


if __name__ == "__main__":
    unittest.main()
