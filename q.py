import turtle


def draw_line(pos1: list, pos2: list) -> None:
    """
    Draw a straight line between two points.

    Args:
        pos1 (list): Starting position as [x, y] coordinates
        pos2 (list): Ending position as [x, y] coordinates

    Return:
        None
    """
    turtle.penup()
    turtle.goto(pos1[0], pos1[1])
    turtle.pendown()
    turtle.goto(pos2[0], pos2[1])


def H_recursive(x: float, y: float, width: float, height: float, count: int) -> None:
    """
    Recursively draw a fractal pattern of interconnected lines.

    This function creates a fractal pattern by drawing three lines forming
    an H-shape and then recursively calling itself for four quadrants.

    Args:
        x (float): X-coordinate of the current section's origin
        y (float): Y-coordinate of the current section's origin
        width (float): Width of the current drawing section
        height (float): Height of the current drawing section
        count (int): Current recursion depth (stops when count <= 0)

    Return:
        None
    """
    draw_line(
        [x + width * 0.25, height // 2 + y],
        [x + width * 0.75, height // 2 + y])
    draw_line(
        [x + width * 0.25, (height * 0.5) // 2 + y],
        [x + width * 0.25, (height * 1.5) // 2 + y])
    draw_line(
        [x + width * 0.75, (height * 0.5) // 2 + y],
        [x + width * 0.75, (height * 1.5) // 2 + y])

    if count <= 0:
        return
    else:
        count -= 1
        H_recursive(x, y, width // 2, height // 2, count)

        H_recursive(x + width // 2, y, width // 2, height // 2, count)

        H_recursive(x, y + width // 2, width // 2, height // 2, count)

        H_recursive(x + width // 2, y + width // 2,
                    width // 2, height // 2, count)


screen = turtle.Screen()
screen.setup(800, 800)

turtle.speed(0)

H_recursive(0, 0, 250, 250, 2)

turtle.done()
