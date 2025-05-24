from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    main_point = Point(0,0)
    first_point = Point(400, 300)
    second_point = Point(600, 500)
    first_line = Line(main_point, first_point)
    second_line = Line(main_point, second_point)
    win.draw_line(first_line, "black")
    win.draw_line(second_line, "red")
    win.wait_for_close()

main()
