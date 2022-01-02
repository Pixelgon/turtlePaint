# -----------------------------------------------------------
# Jednoduchy graficky editor
# Vytvoril Matej Matejka
# -----------------------------------------------------------
# Ovladani:
#   Tecka symbolizuje místo kde bude kreslit,
#   kreslit zacneme stiskem leveho tlacitka na mysi
#   a pro ukonceni leve tlacitko mysi pustime.
#   Pokud chceme obrazec vyplint barvou,
#   tak musime stisknout prave tlacitko u mysi.
#   Pokud chceme smazat to co jsme nakreslili,
#   tak jednoduse stiskneme kalvesu delete
#   Jestlize chceme zmenit barvu, kterou piseme stiskneme c
#   Pokud chceme ulozit obrazek stiskneme s,
#   nas vytvor najdeme na plose pod nazvem img.eps
#   Jestlize jsme uz hotovy,
#   tak program ukoncime klavesou escape
# -----------------------------------------------------------
import turtle, tkinter ,os
from tkinter import colorchooser
turtle.title("TurtlePaint")
wn = turtle.Screen()
img = tkinter.Image("photo", file="TurtlePaint.ico")
turtle._Screen._root.iconphoto(True, img)
wn.setup(width=1.0, height=1.0)
screen = wn.getcanvas()
t = turtle.Turtle()
write = turtle.Turtle()
t.speed('fastest')
write.speed('fastest')
turtle.tracer(0, 0)
t.hideturtle()
turtle.hideturtle()
x = 600
y = 600
t.penup()
write.shape('circle')
write.shapesize(0.2, 0.2, 1)
write.penup()

# Ulozeni obrazku (Klavesa s)
def sv():
    turtle.getscreen()
    turtle.getcanvas().postscript(file="~/Desktop/img.eps")

# Zmena barvy (Klavesa c)
def chcl():
    clfull = colorchooser.askcolor(title ="Vyberte jsi barvu")
    clhex = (clfull[1])
    t.pencolor(clhex)
    t.fillcolor(clhex)

# Mys kresli (leve mysitko)
def paint(x, y):
    t.pendown()
    t.fillcolor()
    t.begin_fill()

# Mys nekresli (pusten leveho mysitka)
def move(x, y):
    t.penup()

# Vypln obrazce (prave mysitko)
def fill(x, y):
    t.end_fill()

# Smazani vseho (klavesa delete)
def cln():
    t.clear()

# Ukonceni programu (klavesa escape)
def ext():
    turtle.bye()

turtle.listen()
write.onclick(paint)
write.onrelease(move)
write.onclick(fill, btn=3)
turtle.onkey(cln, 'Delete')
turtle.onkey(ext, 'Escape')
turtle.onkey(chcl, 'c')
turtle.onkey(sv, 's')

# Nastaveni souradnic
def setCrds(event):
    global x, y
    x = event.x
    y = event.y

screen.bind('<Motion>', setCrds)

# Turlte sleduje kurzor
while True:
    t.setposition(x-(wn.window_width() * 0.5), (y*-1)+(wn.window_height() * 0.5))
    write.setposition(x-(wn.window_width() * 0.5), (y*-1)+(wn.window_height() * 0.5))
    turtle.update()