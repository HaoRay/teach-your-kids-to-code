# CircleSpiralInput.py - Challenge Problem
import turtle   # set up turtle graphics
t=turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
# Set up a list of any 8 valid Python color names
colors=['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray']
# Ask the user for the number of sides, between 1 and 8, default of 4
sides = int(turtle.numinput("Number of circles",
                            "How many circles do you want (1-8)?", 4, 1, 8))
# Draw a colorful spiral with the user-specified number of circles
for x in range(180):
    t.pencolor(colors[x % sides])   # only use the right number of colors
    t.circle(x)                     # change the size to match the # of sides
    t.left(360 / sides + 1)         # turn 360 degrees / # of sides, plus 1
    t.width(x * sides / 200)        # make the pen larger as it goes outward
    
