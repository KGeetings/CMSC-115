import turtle
import random

window = turtle.Screen()

window.title("Here's a window title.")
scrnHeight = 400
scrnWidth = 400
window.screensize(scrnWidth, scrnHeight)
fdDistance = 20
xTarget = 0
yTarget = 0

t = []
for i in range(20):
    t.append(turtle.Turtle())
    t[-1].pencolor(random.choice(("red","blue","green","yellow","black","purple","pink","cyan")))
    t[-1].hideturtle()
    t[-1].speed(0)

def wiggle():
    for i in range(20):
        x,y = t[i].position()
        if x > scrnWidth/2 or x < -scrnWidth/2 or y > scrnHeight/2 or y < -scrnHeight/2:
            t[i].left(180)
            t[i].fd(fdDistance*2)
        t[i].fd(fdDistance)
        t[i].left(random.randrange(-15,16))
        window.ontimer(wiggle, 10)
    
def increaseSpeed():
    global fdDistance
    fdDistance += 5
    print(f"Okay, the turtle is now moving at {fdDistance} pixels.")

def decreaseSpeed():
    global fdDistance
    fdDistance -= 5
    print(f"Okay, the turtle is now moving at {fdDistance} pixels.")

def windowClick(x,y):
    for i in range(20):
        t[i].setheading(x,y)
    
window.ontimer(wiggle, 100)
window.onkey(increaseSpeed, "Up")
window.onkey(decreaseSpeed, "Down")
window.onclick(windowClick)
window.listen()

turtle.mainloop()

turtle.done()

