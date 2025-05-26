from tkinter import Tk, BOTH, Canvas
import time
import random

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__point1.x,
            self.__point1.y,
            self.__point2.x,
            self.__point2.y,
            fill=fill_color,
            width=2
        )

class Window:
    def __init__(self, width: int, height: int) -> None:
        self._root = Tk()
        self._root.title('title')
        self.__canvas = Canvas(height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

class Cell:
    def __init__(self, window: None | Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1: int, y1: int, x2: int, y2: int):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),"#d9d9d9")
        self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),"#d9d9d9")
        self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),"#d9d9d9")
        self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),"#d9d9d9")
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),"black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),"black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),"black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),"black")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        if not undo:
            color = "black"
        else:
            color = "gray"
        line = Line(
            Point(
                (self.__x1 + self.__x2)//2,
                (self.__y1 + self.__y2)//2),
            Point(
                (to_cell.__x1 + to_cell.__x2)//2,
                (to_cell.__y1 + to_cell.__y2)//2,
            )
        )
        self.__win.draw_line(line, color)

class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        nums_rows: int,
        nums_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: None | Window = None,
        seed: None | int = None
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__nums_rows = nums_rows
        self.__nums_cols = nums_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        random.seed(seed)
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__nums_cols):
            self.__cells.append([])
            for j in range(self.__nums_rows):
                cell = Cell(self.__win)
                self.__cells[i].append(cell)
                self.__draw_cell(i,j)
        self.__break_entrance_and_exit()
        self.__break_walls_r(random.randint(0, self.__nums_cols), random.randint(0, self.__nums_rows))

    def __draw_cell(self, i, j):
        x0 = self.__x1 + i * self.__cell_size_x
        y0 = self.__y1 + j * self.__cell_size_y
        x1 = x0 + self.__cell_size_x
        y1 = y0 + self.__cell_size_y
        self.__cells[i][j].draw(x0, y0, x1, y1)
        self.animate()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        if self.__win is None:
            return
        else:
            if len(self.__cells) == 0:
                return
            self.__cells[0][0].has_top_wall = False
            self.__draw_cell(0,0)
            self.__cells[self.__nums_cols - 1][self.__nums_rows - 1].has_bottom_wall = False
            self.__draw_cell(self.__nums_cols - 1, self.__nums_rows - 1)

    def __break_walls_r(self, i:int, j: int):
        self.__draw_cell(i, j)
        self.__cells[i][j].visited = True
        up = True
        down = True
        left = True
        right = True
        while (up or down or left or right):
            way = random.randrange(1, 5, 1)
            if way == 1:
                left = False
                if i - 1 >= 0 and not self.__cells[i - 1][j].visited:
                    self.__cells[i][j].has_left_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i - 1][j].has_right_wall = False
                    self.__break_walls_r(i - 1, j)
            elif way == 2:
                down = False
                if j - 1 >= 0 and not self.__cells[i][j - 1].visited:
                    self.__cells[i][j].has_top_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i][j - 1].has_bottom_wall = False
                    self.__break_walls_r(i, j - 1)
            elif way == 3:
                right = False
                if i + 1 < self.__nums_cols and not self.__cells[i + 1][j].visited:
                    self.__cells[i][j].has_right_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i + 1][j].has_left_wall = False
                    self.__break_walls_r(i + 1, j)
            elif way == 4:
                up = False
                if j + 1 < self.__nums_rows and not self.__cells[i][j + 1].visited:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i][j + 1].has_top_wall = False
                    self.__break_walls_r(i, j + 1)
        return
