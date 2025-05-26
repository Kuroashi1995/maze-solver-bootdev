from graphics import Cell, Window, Line, Point, Maze

def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)
    padding_x = 50
    padding_y = 50
    cells_width = 40
    cells_height = 40
    cols = (win_width - 2*padding_x) // cells_width
    rows = (win_height - 2*padding_y) // cells_height
    maze = Maze(padding_x, padding_y, rows, cols, cells_width, cells_height, win)
    win.wait_for_close()

main()
