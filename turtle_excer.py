from turtle import *

shape("turtle")
speed(3)

colors = ['red','blue','brown','yellow','grey']

n_angle = 3

for i in range(5):
    for j in range(n_angle):
        forward(100)
        color(colors[i])
        left(360/n_angle)
    n_angle += 1

mainloop()