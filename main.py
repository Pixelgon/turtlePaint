import turtle

def setCrds(event):
    global x, y
    x = event.x
    y = event.y
wn = turtle.Screen()
wn.setup(1200, 1200)
screen = wn.getcanvas()
t = turtle.Turtle()
x = 600
y = 600
screen.bind('<Motion>', setCrds)
t.speed('fastest')
turtle.tracer(0, 0)
t.hideturtle()
turtle.title("turtlePaint")
while True:
    t.setposition(x-600, (y*-1)+600)
    turtle.update()
