# Copyright: Thomas Oakes 2021
# Pong
# This is Pong created using turtle library
# This code was inspired by Christian Thompson tutorial
# His version can be found at http://christianthompson.com/sites/default/files/Pong/pong.py

#imports
import turtle
import winsound

#Global initializations
#Initializes window
window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()                #makes it so that the paddle isnt a continuous line when it moves
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()                #makes it so that the paddle isnt a continuous line when it moves
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()                #makes it so that the paddle isnt a continuous line when it moves
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#Functions
#Function that increases paddle_a's y-coordinate by 20
def paddle_a_up():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)
    
#Function that decrease paddle_a's y-coordinate by 20
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)

#Function that increases paddle_b's y-coordinate by 20
def paddle_b_up():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)
    
#Function that decrease paddle_b's y-coordinate by 20
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)
    
#Key binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    window.update()
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Checks border
    if ball.ycor() > 290:
        ball.sety(290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))        
        
    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.dx *= -1