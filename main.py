from graphics import Cell, Window, Line, Point

def main():
    win = Window(800, 600)
    main_point = Point(0,0)
    first_point = Point(400, 300)
    second_point = Point(600, 500)
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(first_point.x, first_point.y, second_point.x, second_point.y)
    win.wait_for_close()

main()
