from graphics import Cell, Window, Line, Point

def main():
    win = Window(800, 600)
    first_point = Point(2, 2)
    second_point = Point(102, 102)
    to_point1 = Point(2,104)
    to_point2 = Point(104, 204)
    cell = Cell(win)
    cell.draw(first_point.x, first_point.y, second_point.x, second_point.y)
    to_cell = Cell(win)
    to_cell.draw(to_point1.x, to_point1.y, to_point2.x, to_point2.y)
    cell.draw_move(to_cell)
    win.wait_for_close()

main()
