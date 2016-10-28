"""http://www.1point3acres.com/bbs/thread-207550-1-1.html
题目没法描述，哪天画个图片再贴上来，和图形有关的，三角形套三角形，问怎么输出一堆点
,然后用已知的画线api生成某一depth的图形，
"""


import turtle


ninja = turtle.Turtle()
ninja.speed(10)


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_line(p1, p2):
    ninja.penup()
    ninja.goto(p1.x, p1.y)
    ninja.pendown()
    ninja.goto(p2.x, p2.y)


def draw_triangle(p1, p2, p3):
    draw_line(p1, p2)
    draw_line(p2, p3)
    draw_line(p3, p1)


def dfs(p1, p2, p3, depth):
    draw_triangle(p1, p2, p3)
    if depth:
        m1 = Point((p1.x+p2.x)/2., (p1.y+p2.y)/2.)
        m2 = Point((p2.x+p3.x)/2., (p2.y+p3.y)/2.)
        m3 = Point((p3.x+p1.x)/2., (p3.y+p1.y)/2.)
        depth -= 1
        dfs(p1, m1, m3, depth)
        dfs(p2, m1, m2, depth)
        dfs(p3, m2, m3, depth)


if __name__ == '__main__':
    p1 = Point(-100, 0)
    p2 = Point(100, 0)
    p3 = Point(0, 173)
    dfs(p1, p2, p3, 2)
    turtle.mainloop()
