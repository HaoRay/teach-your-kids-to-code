import turtle   
colors=['red', 'blue','yellow']
t=turtle.Pen()
t.width(5)
for x in range(360):
    t.pencolor(colors[x%3])
    t.forward(x * 2)        
    t.left(120 - 2)
