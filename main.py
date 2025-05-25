from graphics import Cell, Window, Line, Point, Maze

def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 20, 20, 50, 50, win)
    win.wait_for_close()

main()
