import turtle, pyautogui
turtle.title("turtlePaint")
wn = turtle.Screen()
wn.setup(1200, 1200)
screen = wn.getcanvas()
t = turtle.Turtle()
t.speed('fastest')
turtle.tracer(0, 0)
t.hideturtle()
x = 600
y = 600
t.penup()
def paint(x, y):
    t.pendown()

turtle.onscreenclick(paint)
def setCrds(event):
    global x, y
    x = event.x
    y = event.y
screen.bind('<Motion>', setCrds)
while True:
    t.setposition(x-600, (y*-1)+600)
    turtle.update()
