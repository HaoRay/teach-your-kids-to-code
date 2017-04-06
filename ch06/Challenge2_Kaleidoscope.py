#KaleidoscopeChallenge2.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
colors=['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray']
for n in range(50):
    # generate spirals of random sizes/colors at random locations on the screen
    t.pencolor(random.choice(colors))   # pick a random color from colors[]
    size = random.randint(10,40)        # random size spiral from 10 to 40
    sides = random.randint(3,9)        # random number of sides in spiral
    thick = random.randint(1,6)         # random thickness of the lines
    t.width(thick)
    angle = t.heading()
    # generate a random (x,y) location on the screen
    x = random.randrange(size,turtle.window_width()//2)
    y = random.randrange(size,turtle.window_height()//2)
    # first spiral
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
    # second spiral
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    t.setheading(180-angle)
    for m in range(size):
        t.forward(m*2)
        t.right(360/sides + 2)    
    # third spiral
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    t.setheading(angle-180)
    for m in range(size):
        t.forward(m*2)
        t.left(360/sides + 2)
    # fourth spiral
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    t.setheading(360-angle)
    for m in range(size):
        t.forward(m*2)
        t.right(360/sides + 2)
