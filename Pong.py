# Pong in Python3
# by @ManzelGomez
#

import turtle

window = turtle.Screen()
window.title("Pong by @ManzelGomez")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Paddle A
paddle_a = turtle.Turle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B



#Ball



#main game loop
while True:
    window.update()
