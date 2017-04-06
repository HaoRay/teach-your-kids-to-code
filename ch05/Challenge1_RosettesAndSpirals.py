# RosettesAndSpirals.py - a spiral of shapes AND rosettes!
import turtle
t=turtle.Pen()
t.penup()
t.speed(0)
turtle.bgcolor('black')
# Ask the user for the number of sides, default to 4, min 2, max 6
sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral?", 4,2,6))
colors=['red', 'yellow', 'blue', 'green', 'purple', 'orange']
# Our outer spiral loop
for m in range(1,60):
    t.forward(m*4)
    t.width(m//25+1)
    position = t.position() # remember this corner of the spiral
    heading = t.heading()   # remember the direction we were heading
    # Our 'inner' spiral loop,
    # draws a little rosette at each corner of the big spiral
    if (m % 2 == 0):
        for n in range(sides):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.circle(m/4)
            t.right(360/sides - 2)
            t.penup()
    # OR, draws a little spiral at each corner of the big spiral
    else:
        for n in range(3,m):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.forward(n)
            t.right(360/sides - 2)
            t.penup()
    t.setx(position[0])     # go back to the big spiral's x location
    t.sety(position[1])     # go back to the big spiral's y location
    t.setheading(heading)   # point in the big spirals direction/heading
    t.left(360/sides + 4)   # move to the next point on the big spiral


