import turtle
import time
import random

speed= 0.14
window = turtle.Screen()
window.title('Snake Game by asiancart')
window.bgcolor('lightgreen')
window.setup(width=600,height=600)
window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("red")
food.penup()
food.goto(0,0)
food.shapesize(0.80,0.80)

tails = []
points = 0

write = turtle.Turtle()
write.speed(0)
write.shape('square')
write.color("white")
write.penup()
write.goto(0,260)
write.hideturtle()
write.write("Points: {}".format(points), align='center', font=('Courier', 24, 'normal'))


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"

def goRight():
    if head.direction != "left":
        head.direction = "right"

def goLeft():
    if head.direction != "right":
        head.direction = "left"


window.listen()
window.onkey(goUp, 'Up')
window.onkey(goDown, 'Down')
window.onkey(goRight, 'Right')
window.onkey(goLeft, 'Left')


while True:
    window.update()
    move()
    time.sleep(speed)

    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        for tail in tails:
            tail.goto(1000,1000)
        tails = []
        points = 0

        speed = 0.14

    if head.distance(food) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)
        speed -= 0.005
        points += 10
        write.clear()
        write.write("Points: {}".format(points), align='center', font=('Courier', 24, 'normal'))


        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape("square")
        newTail.color("white")
        newTail.penup()
        tails.append(newTail)

    for i in range(len(tails)-1,0,-1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x,y)

    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x,y)
