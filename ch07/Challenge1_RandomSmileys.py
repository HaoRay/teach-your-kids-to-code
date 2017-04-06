#RandomSmileys.py
import random
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor('black')
def draw_smiley(x,y):      
    t.penup()
    t.setpos(x,y)
    t.pendown()
    # Face
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    # Left Eye
    t.setpos(x-15, y+60)
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Right Eye
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    # Mouth
    t.setpos(x-25,y+40)
    t.pencolor('black')
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)

for n in range(50):
    x = random.randrange(int(-turtle.window_width()/2 + 50),
                         int(turtle.window_width()/2 - 50))
    y = random.randrange(int(-turtle.window_height()/2),
                         int(turtle.window_height()/2) - 100)
    draw_smiley(x,y)
