# Pong in Python3
# by @ManzelGomez
#

import turtle

window = turtle.Screen()
window.title("Pong by @ManzelGomez | First to 3")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)



#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = .25
ball.dy = .25

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 20, "normal"))


#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#Keyboard Bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_up, "W")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_a_down, "S")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    window.update()


    #move ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    #Bouncing the ball off the Paddles
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-330)
        ball.dx *= -1   
    
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(330)
        ball.dx *= -1


    #Winning Screen
    if score_a > 2:
        ball.color("black")
        paddle_b.color("black")
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write("Player A wins", align="center", font=("Courier", 20, "normal"))

    if score_b > 2:
        ball.color("black")
        paddle_a.color("black")
        ball.dx = 0
        ball.dy = 0
        pen.clear()
        pen.write("Player B wins", align="center", font=("Courier", 20, "normal"))



