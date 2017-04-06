import turtle
t = turtle.Pen()
t.speed(0)
t.turtlesize(2,2,2)
turtle.bgcolor("black")
drawcolor = "white"
t.color(drawcolor)
t.width(4)
width = 4
heading = 0
length = 50      # turtle line length
display = ""     # text display

def draw_text():
    global display # access the global variable display
    t = turtle.Pen()    # separate pen for drawing text
    t.penup()
    t.goto(-200, 200)
    t.color("black")
    t.pendown()     # 'erase' the last display by drawing black
    t.write(display, font=("Arial", 16, "bold") )
    t.penup()
    t.goto(-200, 200)
    t.color(drawcolor)
    t.pendown()     # draw the new display
    display = "Angle: " + str(heading) + "  Width: " + str(width)
    display += "  Length: " + str(length)
    t.write(display, font=("Arial", 16, "bold") )

def up():
    t.forward(length)
    draw_text()
def left():
    global heading
    heading = t.heading()
    heading += 30
    t.setheading(heading)
    draw_text()
def right():
    global heading
    heading = t.heading()
    heading -= 30
    t.setheading(heading)
    draw_text()
def smaller():
    global width
    width = t.width()-2
    t.width(width)
    draw_text()
def bigger():
    global width
    width = t.width()+2
    t.width(width)
    draw_text()
def longer():
    global length
    length=length+25
    draw_text()
def shorter():
    global length
    length=length-25
    draw_text()
turtle.onkey(up, "Up")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(bigger, "b")
turtle.onkey(smaller, "s")
turtle.onkey(longer, ">")
turtle.onkey(shorter, "<")
draw_text()
turtle.listen()
