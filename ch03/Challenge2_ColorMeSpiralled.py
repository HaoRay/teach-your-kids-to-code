# ColorMeSpiralled.py 

import turtle   # set up turtle graphics
t=turtle.Pen()  
turtle.bgcolor('black')
# Set up a list of any 10 valid Python color names
colors=['red', 'yellow', 'blue', 'green', 'orange',
        'purple', 'white', 'gray', 'brown', 'sea green']

# ask the user's name using turtle's textinput popup window
your_name = turtle.textinput("Enter your name", "What is your name?")

# ask the number of sides
sides = int(turtle.numinput("Number of sides",
                            "How many sides do you want (1-10)?", 5, 1, 10))

# draw a spiral of the name on the screen, written 100 times
for x in range(100):
    t.pencolor(colors[x%sides%10]) # rotate through the 10 colors
    t.penup()       # don't draw the regular spiral lines
    t.forward(x*4)  # just move the turtle on the screen
    t.pendown()     # now, write the user's name, bigger each time
    t.write(your_name, font=("Arial", int( (x*2 + 4) / 4), "bold") )
    t.left(360/sides+2)      # turn left 360/sides+2 degrees for sides

