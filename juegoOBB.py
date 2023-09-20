import turtle
import time

# Variables globales
ins = 0
hitbox = 25
# Posponer
aguanta = 0.005
# Puntaje
Puntaje = 0
# retroceso  (>= 1)
retroces = 1

# Configuración ventana
wn = turtle.Screen()
wn.title("JUEGO OBB")
wn.bgcolor("gray")
wn.setup(width=800, height=500)
wn.tracer(0)

################################
########## OBJETOS #############
# Objeto movimiento

yo = turtle.Turtle()
yo.speed(2)
yo.shape("square")
yo.penup()
yo.goto(0, 0)
yo.direction = "stop"

# Circulo estatico

circulo = turtle.Turtle()
circulo.speed(2)
circulo.shape("circle")
circulo.color("red")
circulo.penup()
circulo.goto(-200, 90)
circulo.direction = "stop"

# Circulo grande

circulobig = turtle.Turtle()
circulobig.speed(2)
circulobig.shape("circle")
circulobig.color("red")
circulobig.penup()
circulobig.goto(300, 100)
circulobig.direction = "stop"
circulobig.shapesize(1.3, 1.3)
# Circulo pequeño

circulosmall = turtle.Turtle()
circulosmall.speed(2)
circulosmall.shape("circle")
circulosmall.color("red")
circulosmall.penup()
circulosmall.goto(150, -100)
circulosmall.direction = "stop"
circulosmall.shapesize(0.5, 0.5)
# Trangulo estatico

triangulo = turtle.Turtle()
triangulo.speed(2)
triangulo.shape("triangle")
triangulo.color("brown")
triangulo.penup()
triangulo.goto(-200, -150)
triangulo.direction = "stop"

# Rectangulo estatico

rectangulo = turtle.Turtle()
rectangulo.speed(2)
rectangulo.shape("square")
rectangulo.color("green")
rectangulo.penup()
rectangulo.goto(200, -40)
rectangulo.direction = "stop"

# Cuadrado estatico

cuadrado1 = turtle.Turtle()
cuadrado1.speed(2)
cuadrado1.shape("square")
cuadrado1.color("green")
cuadrado1.penup()
cuadrado1.goto(-50, -100)
cuadrado1.direction = "stop"


################################
####### FUNCIONAMIENTO #########

### FUNCION DE MOVIMIENTO ###


def mov():
    if yo.direction == "up":
        y = yo.ycor()
        yo.sety(y + 1)
    if yo.direction == "down":
        y = yo.ycor()
        yo.sety(y - 1)
    if yo.direction == "right":
        x = yo.xcor()
        yo.setx(x + 1)
    if yo.direction == "left":
        x = yo.xcor()
        yo.setx(x - 1)


### EVITAR QUE SE QUEDE QUIETO ###


def retroced():
    global retroces
    if yo.direction == "up":
        yo.direction = "down"
        for n in range(retroces):
            mov()
    elif yo.direction == "down":
        yo.direction = "up"
        for n in range(retroces):
            mov()
    elif yo.direction == "right":
        yo.direction = "left"
        for n in range(retroces):
            mov()
    elif yo.direction == "left":
        yo.direction = "right"
        for n in range(retroces):
            mov()
# Controles


def up():
    yo.direction = "up"


def down():
    yo.direction = "down"


def left():
    yo.direction = "left"


def right():
    yo.direction = "right"


def stop():
    global ins
    if ins == 200:
        yo.direction = "stop"
        ins = 0
    ins += 1

# lectura posicion


def posiciones():
    global Puntaje
    a = yo.xcor()
    b = yo.ycor()
    dist1x = abs(a - cuadrado1.xcor())
    dist1y = abs(b - cuadrado1.ycor())

    dist2x = abs(a - rectangulo.xcor())
    dist2y = abs(b - rectangulo.ycor())

    dist3x = abs(a - circulosmall.xcor())
    dist3y = abs(b - circulosmall.ycor())

    dist4x = abs(a - circulo.xcor())
    dist4y = abs(b - circulo.ycor())

    dist5x = abs(a - circulobig.xcor())
    dist5y = abs(b - circulobig.ycor())

    dist6x = abs(a - triangulo.xcor())
    dist6y = abs(b - triangulo.ycor())

    rad1 = pow(pow(dist1x, 2) + pow(dist1y, 2), 0.5)
    rad2 = pow(pow(dist2x, 2) + pow(dist2y, 2), 0.5)
    rad3 = pow(pow(dist3x, 2) + pow(dist3y, 2), 0.5)
    rad4 = pow(pow(dist4x, 2) + pow(dist4y, 2), 0.5)
    rad5 = pow(pow(dist5x, 2) + pow(dist5y, 2), 0.5)
    rad6 = pow(pow(dist6x, 2) + pow(dist6y, 2), 0.5)

    if rad1 <= hitbox:
        retroced()
        yo.direction = "stop"
    if rad2 <= hitbox:
        retroced()
        yo.direction = "stop"
    if rad3 <= hitbox and Puntaje == 0:
        Puntaje = 1
        circulosmall.hideturtle()
        yo.shapesize(1.3, 1.3)
        retroced()
        yo.direction = "stop"

    if rad4 <= hitbox and Puntaje == 1:
        Puntaje = 2
        circulo.hideturtle()
        yo.shapesize(1.5, 1.5)
        retroced()
        yo.direction = "stop"
    if rad5 <= hitbox and Puntaje == 2:
        Puntaje = 3
        circulobig.hideturtle()
        yo.shapesize(1.7, 1.7)
        retroced()
        yo.direction = "stop"
    if rad6 <= hitbox:
        yo.hideturtle()
        yo.shapesize(1.7, 1.7)
        yo.direction = "stop"


# Configuracion lectura teclado
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")
wn.onkeypress(stop, "Tab")


# Principal Code

while True:
    wn.update()
    posiciones()
    mov()
    stop()
    time.sleep(aguanta)
