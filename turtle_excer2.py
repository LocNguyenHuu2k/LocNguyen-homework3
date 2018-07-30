from turtle import *

shape('turtle')
speed(2)
colors = ['red','blue','brown','yellow','grey']


for i in range(5):
    begin_fill()
    for j in range(2):
        color(colors[i])
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)


mainloop()


