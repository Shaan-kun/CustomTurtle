import turtle
import math


def dot(x: float, y: float):
    """Ставит точку в позиции с координатами (x, y)."""
    turtle.tracer(0)
    turtle.speed(0)
    turtle.penup()
    turtle.hideturtle()
    turtle.setposition(x, y)
    turtle.dot()


def line(x1: float, y1: float, x2: float, y2: float):
    """Рисует линию от точки (x1, y1) до точки (x2, y2)."""

    # первой точкой считается та, что левее
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    s = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    delta = (x2 - x1) / s

    # частный случай, когда координата x совпадает
    if x2 == x1:
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        delta = (y2 - y1) / s
        while y1 < y2:
            dot(x1, y1)
            y1 += delta

        return None

    k = (y2 - y1) / (x2 - x1)
    while x1 < x2:
        dot(x1, y1)
        x1 += delta
        y1 += k * delta


def rectangle(x1: float, y1: float, x2: float, y2: float):
    """Рисует прямоугольник.

    (x1, y1) -> левый верхний угол
    (x2, y2) -> правый нижний угол
    """
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)

    # собираем 4 точки - углы прямоугольника
    a1 = x_min, y_min
    a2 = x_max, y_min
    a3 = x_max, y_max
    a4 = x_min, y_max

    line(*a1, *a2)
    line(*a2, *a3)
    line(*a3, *a4)
    line(*a4, *a1)


def triangle(x1, y1, x2, y2, x3, y3):
    """Рисует треугольник."""
    line(x1, y1, x2, y2)
    line(x2, y2, x3, y3)
    line(x3, y3, x1, y1)


def circle(x0: float, y0: float, r: float):
    """Рисует окружность радиуса r с центром в точке (x0, y0)."""
    phi = 0
    while phi < 2 * math.pi:
        phi += 1 / r  # (2 * Pi) / (2 * Pi * r) - шаг
        x, y = x0 + r * math.cos(phi), y0 + r * math.sin(phi)
        dot(x, y)
