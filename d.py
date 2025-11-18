import turtle


def ice_fract(rec_num: int, size: float) -> None:
    """
    Draw an ice fractal using recursion.

    This function recursively draws a fractal pattern that resembles ice crystals
    or snowflakes by repeatedly dividing the line segments and adding perpendicular branches.

    Args:
        rec_num (int): The recursion depth
        size (float): The size of the fractal segment

    Return:
        None
    """
    if rec_num == 0:
        turtle.forward(size/2)
        turtle.left(90)
        turtle.forward(size/3)

        turtle.back(size/3)
        turtle.right(90)
        turtle.forward(size/2)

    else:
        ice_fract(rec_num-1, size/4)
        turtle.left(90)
        ice_fract(rec_num-1, size/6)
        turtle.right(180)

        ice_fract(rec_num-1, size/6)
        turtle.left(90)
        ice_fract(rec_num-1, size/4)


turtle.tracer(0)
ice_fract(5, 1000)
turtle.done()
