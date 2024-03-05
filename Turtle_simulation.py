import turtle
import random

g = 9.81    
dt = 0.01   
mnoznik = 0.1  

def koloruj(obiekt):
    kolor1 = random.randint(0, 255)
    kolor2 = random.randint(0, 255)
    kolor3 = random.randint(0, 255)
    obiekt.pencolor(kolor1,kolor2,kolor3)
    obiekt.fillcolor(kolor1,kolor2,kolor3)


turtle.colormode(255)
turtle.screensize(1000,600,bg="black")
turtle.setup(1100,700)

t = turtle.Turtle()
t.up()
t.fillcolor("white")
t.pencolor("white")


x = -400
y = 200
vy = 0
vx = 300
q = 20
skala = 1

r = turtle.Turtle()
r.pencolor("white")
r.hideturtle()
r.up()
r.speed(0)
r.setpos(-500,0)
r.down()
r.forward(1000)
r.left(90)
r.forward(300)
r.left(90)
r.forward(1000)
r.left(90)
r.forward(300)

while True:
    ay = -g
    ax = 0
    for i in range(1,q):
        vy += ay * dt
        y += vy * dt * mnoznik
        x += vx * dt * mnoznik
    t.sety(y)
    t.setx(x)
    t.down()
    if vx < 5 and vx > -5:
        break
    if y <= 0:
        vy = -vy*0.75
        y = 0.1
        vx = vx*0.8*skala
        koloruj(t)
        if skala > 0.7:
            skala = skala - 0.05
    if y >= 300:
        vy = -vy*0.75
        y = 299.9
        vx = vx*0.8*skala
        koloruj(t)
        if skala > 0.7:
            skala = skala - 0.05
    if x >= 500:
        vx = -vx
        x = 500.1
        vx = vx*0.8
        t.speed(0)
        t.right(180)
        koloruj(t)
    if x<= -500:
        vx = -vx
        x = -499.9
        vx = vx*0.8
        t.speed(0)
        t.right(180)
        koloruj(t)

turtle.done()