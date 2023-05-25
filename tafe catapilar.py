import turtle

from itertools import cycle
colors=cycle(['blue','yellow','green','purple','red',
'pink'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    tright.right(angle)
    turtle.forward(shift)
    draw_circle(size+5,anglft+1)

    turtle.bgcolor('orang')
    turtle.speed('fast')
    turtle.pensize(35)
    draw_circle(30,0,1)               
    
