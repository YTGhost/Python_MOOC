import turtle


def koch(size, n):
    if n == 1:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 6
    size = 5000
    koch(size, level)
    turtle.right(120)
    koch(size, level)
    turtle.right(120)
    koch(size, level)
    turtle.hideturtle()
    turtle.done()


main()
