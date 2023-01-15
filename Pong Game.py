# Pong Game
import turtle
import time
# from paddles import *

#create window
wn = turtle.Screen() 
turtle.TurtleScreen._RUNNING=True
wn.title("Pong")
#change background
wn.bgcolor("black")
#change window size 
wn.setup(width=800, height=600)
wn.tracer(0) 

#apparently it lets the window to work better through limiting updating

# Score
score_a = 0
score_b = 0
winning_score = 5

# Paddle A
# paddle_a = Paddle(position=-350)
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() #we don't want any drawings
paddle_a.goto(-350, 0)

# Paddle B
# paddle_b = Paddle(position=350)
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() #we don't want any drawings
paddle_b.goto(350, 0)

# Ball
# ball = Ball()
ball = turtle.Turtle()
ball.speed(0) #speed of animation to max
ball.shape("square")
ball.color("white")
ball.penup() #we don't want any drawings
ball.goto(0, 0)
ball.dx = 0.5 
ball.dy = 0.5 

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", '24', 'normal'))


def paddlea_up():
    y = paddle_a.ycor()
    if(y<250):
        y += 20
        paddle_a.sety(y)

def paddleb_up():
    y = paddle_b.ycor()
    if(y<250):
        y += 20
        paddle_b.sety(y)

def paddlea_down():
    y = paddle_a.ycor()
    if(y>-250):
        y += -20
        paddle_a.sety(y)

def paddleb_down():
    y = paddle_b.ycor()
    if(y>-250):
        y += -20
        paddle_b.sety(y)

def won_msg(player):
    pen.write("Player {} won!".format(player) , align="center", font=("Courier", '24', 'normal'))

def game_end():
    if score_a == winning_score or score_b == winning_score: 
        pen.clear()
        
        if score_a >= winning_score: 
            won_msg("A")
            end_ball_params()
        elif score_b >= winning_score: 
            won_msg("B") 
            end_ball_params()

def end_ball_params():
    ball.color("black")
    ball.dx = 0
    ball.dy = 0 

        
# def game_restart():
#     ball.color("white")
#     score_a = 0
#     score_b = 0
#     ball.dx = 0.5
#     ball.dx = 0.5

wn.listen() #listen for keyboard input
wn.onkeypress(paddlea_up, "w")
wn.onkeypress(paddlea_down, "s")
wn.onkeypress(paddleb_up, "Up")
wn.onkeypress(paddleb_down, "Down")

# Main game loop
while True:
    wn.update() 
    #updates the screen 
    game_end()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", '24', 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  
        score_b += 1

        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", '24', 'normal'))
          
    
    if ball.xcor() > 340 and ball.xcor() <350 and ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor() -50:
        ball.setx(340)
        ball.dx *= -1
       
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor() -50:
        ball.setx(-340)
        ball.dx *= -1
    

    
    
        

