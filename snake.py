import random
import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

segment = turtle.Turtle()
segment.shape("square")
segment.color("darkblue")
segment.speed(0)
segment.penup()

snake = [segment]

dir = "right"
def move():
    head = snake[0]
    tail = snake[-1]
    x = head.xcor()
    y = head.ycor()

    if dir == "up" :
        tail.goto(x, y + 22)
    elif dir == "down" :
        tail.goto(x, y - 22)
    elif dir == "left" :
        tail.goto(x - 22, y)
    else:
        tail.goto(x + 22, y)


    snake.insert(0,tail)
    snake.pop()

def up():
    global dir
    if dir != "down":
        dir = "up" 

def down() :
    global dir
    if dir != "up":
        dir = "down"

def left() :
    global dir
    if dir != "right":
        dir = "left"

def right() :
    global dir
    if dir != "left":
        dir = "right"     


screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

def update() :
    move()
    screen.ontimer(update, 500)
 
update()




























turtle.mainloop()