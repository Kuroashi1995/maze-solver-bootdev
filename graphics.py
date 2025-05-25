from tkinter import Tk, BOTH, Canvas
import time

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
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
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
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)),"red")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)),"red")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)),"red")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)),"red")

    def draw_move(self, to_cell, undo=False):
        if not undo:
            color = "red"
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
        win: Window,
    ) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__nums_rows = nums_rows
        self.__nums_cols = nums_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__nums_cols):
            self.__cells.append([])
            for j in range(self.__nums_rows):
                cell = Cell(self.__win)
                self.__cells[i].append(cell)
                self.__draw_cell(i,j)

    def __draw_cell(self, i, j):
        x0 = self.__x1 + i * self.__cell_size_x
        y0 = self.__y1 + j * self.__cell_size_y
        x1 = x0 + self.__cell_size_x
        y1 = y0 + self.__cell_size_y
        self.__cells[i][j].draw(x0, y0, x1, y1)
        self.animate()

    def animate(self):
        self.__win.redraw()
        time.sleep(0.05)
