from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, fill_color="white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, fill_color="white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, fill_color="white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, fill_color="white")

    def draw_move(self, to_cell, undo=False):
        c1 = Point(
            self.__x1 + abs(self.__x2 - self.__x1) // 2,
            self.__y1 + abs(self.__y2 - self.__y1) // 2,
        )
        c2 = Point(
            to_cell.__x1 + abs(to_cell.__x2 - to_cell.__x1) // 2,
            to_cell.__y1 + abs(to_cell.__y2 - to_cell.__y1) // 2,
        )
        fill_color = "red" if undo else "black"
        line = Line(c1, c2)
        if self.__win:
            self.__win.draw_line(line, fill_color=fill_color)
