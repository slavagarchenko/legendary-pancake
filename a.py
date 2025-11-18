import turtle


def mink_curve(rec_num: int, size: float) -> None:
    """
    Draw the Minkowski curve fractal using recursion.

    This function recursively draws the Minkowski curve, a fractal pattern
    that fills a square area with a continuous but non-differentiable curve.

    Args:
        rec_num (int): The recursion depth
        size (float): The size of the fractal curve

    Return:
        None
    """
    if rec_num == 0:
        turtle.forward(size)

    else:
        mink_curve(rec_num-1, size/4)
        turtle.left(90)
        mink_curve(rec_num-1, size/4)
        turtle.right(90)
        mink_curve(rec_num-1, size/4)
        turtle.right(90)
        mink_curve(rec_num-1, size/4)

        mink_curve(rec_num-1, size/4)
        turtle.left(90)
        mink_curve(rec_num-1, size/4)
        turtle.left(90)
        mink_curve(rec_num-1, size/4)
        turtle.right(90)
        mink_curve(rec_num-1, size/4)


turtle.tracer(0)
mink_curve(5, 1000)
turtle.done()
