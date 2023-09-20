import turtle
import time

# Posponer
timestop = 0.005

# Configuración ventana
wn = turtle.Screen()
wn.title("AABB")
wn.bgcolor("gray")
wn.setup(width=600, height=600)
wn.tracer(0)

# Objeto movimiento

person = turtle.Turtle()
person.speed(2)
person.shape("square")
person.penup()
person.goto(0, 0)
person.direction = "up"

# Objetos estatico

ogject1 = turtle.Turtle()
ogject1.speed(2)
ogject1.shape("square")
ogject1.color("yellow")
ogject1.penup()
ogject1.goto(100, 50)
ogject1.direction = "stop"

# Objetos recojer 2

ogject2 = turtle.Turtle()
ogject2.speed(2)
ogject2.shape("triangle")
ogject2.color("red")
ogject2.penup()
ogject2.goto(-50, -100)
ogject2.direction = "stop"
# ogject2.shapesize(2, 2)

# Variables

# funcion retroceder


def retroced():
    if person.direction == "up":
        y = person.ycor()
        person.sety(y - 1)
    if person.direction == "down":
        y = person.ycor()
        person.sety(y + 1)
    if person.direction == "right":
        x = person.xcor()
        person.setx(x - 1)
    if person.direction == "left":
        x = person.xcor()
        person.setx(x + 1)

# Funciones moviment


def mov():
    if person.direction == "up":
        y = person.ycor()
        person.sety(y + 1)
    if person.direction == "down":
        y = person.ycor()
        person.sety(y - 1)
    if person.direction == "right":
        x = person.xcor()
        person.setx(x + 1)
    if person.direction == "left":
        x = person.xcor()
        person.setx(x - 1)

# Controles


def up():
    person.direction = "up"


def down():
    person.direction = "down"


def left():
    person.direction = "left"


def right():
    person.direction = "right"


def stop():
    global ins
    if ins == 200:
        person.direction = "stop"
        ins = 0
    ins += 1

# lectura posicion


def posiciones():
    a = person.xcor()
    b = person.ycor()
    return a, b


# Configuracion lectura teclado
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(stop, "Tab")


# Principal Code
ins = 0
hitbox = 20
while True:
    wn.update()

    a, b = posiciones()
    do1x = a - ogject1.xcor()
    do1y = b - ogject1.ycor()

    do2x = a - ogject2.xcor()
    do2y = b - ogject2.ycor()

    do1x = abs(do1x)
    do1y = abs(do1y)
    do2x = abs(do2x)
    do2y = abs(do2y)
    if do1x <= hitbox and do1y <= hitbox:
        retroced()
        person.direction = "stop"
    if do2x <= hitbox and do2y <= hitbox:
        retroced()
        person.direction = "stop"

    mov()
    stop()
    time.sleep(timestop)
