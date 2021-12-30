import turtle, pyautogui
turtle.title("turtlePaint")
wn = turtle.Screen()
wn.setup(1200, 1200)
screen = wn.getcanvas()
t = turtle.Turtle()
write = turtle.Turtle()
t.speed('fastest')
write.speed('fastest')
turtle.tracer(0, 0)
t.hideturtle()
x = 600
y = 600
t.penup()
write.shape('circle')
write.shapesize(0.2, 0.2, 1)
write.penup()
def paint(x, y):
    t.pendown()
def move(x, y):
    t.penup()

write.onclick(paint)
write.onrelease(move)
def setCrds(event):
    global x, y
    x = event.x
    y = event.y
screen.bind('<Motion>', setCrds)
while True:
    t.setposition(x-600, (y*-1)+600)
    write.setposition(x-600, (y*-1)+600)
    turtle.update()
