# colorspiral.py
"""A module for drawing colorful spirals of up to 6 sides"""
import turtle
def cspiral(sides=6, size=360, x=0, y=0):
    """Draws a colorful spiral on a black background.
    Arguments:
    sides -- the number of sides in the spiral (default 6)
    size -- the length of the last side (default 360)
    x, y -- the location of the spiral, from the center of the screen
    """
    t=turtle.Pen()
    t.speed(0)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    turtle.bgcolor("black")
    colors=["red", "yellow", "blue", "orange", "green", "purple"]
    for n in range(size):
        t.pencolor(colors[n%sides])
        t.forward(n * 3/sides + n)
        t.left(360/sides + 1)
        t.width(n*sides/100)

