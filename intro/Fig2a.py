import turtle   
colors=['red', 'blue','yellow']
t=turtle.Pen()
t.width(3)
for x in range(360):
    t.pencolor(colors[x%3])
    t.forward(x * 3)        
    t.left(120 - 1)
