from turtle import *

shape("turtle")
speed(3)

colors = ['red','blue','brown','yellow','grey']

n_angle = 3

for i in range(6):
    for i in range(n_angle):
        forward(100)
        color(colors[n_angle-3])
        left(360/n_angle)
    n_angle += 1

mainloop()