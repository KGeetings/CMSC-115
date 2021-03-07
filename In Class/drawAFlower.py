import turtle

def drawAPetal(t, length, angle):
    t.right(angle/2)
    for i in range(2):
        t.fd(length)
        t.left(angle)
        t.fd(length)
        t.left(angle)
        t.fd(length)
        t.left(180 - (2 * angle))
    t.left(angle/2)

def drawAFlower(numPetals, length, angle, theTurtle):
    for i in range(numPetals):
        drawAPetal(theTurtle, length, angle)
        theTurtle.left(360/numPetals)
        
topLeft = turtle.Turtle()
topLeft.speed(0)
topLeft.goto(-50,50)
topLeft.pencolor("green")

topRight = turtle.Turtle()
topRight.speed(0)
topRight.goto(50,50)
topRight.pencolor("blue")

bottomLeft = turtle.Turtle()
bottomLeft.speed(0)
bottomLeft.goto(-50,-50)
bottomLeft.pencolor("orange")

bottomRight = turtle.Turtle()
bottomRight.speed(0)
bottomRight.goto(50,-50)
bottomRight.pencolor("pink")

drawAFlower(10, 50, 20, topLeft)
drawAFlower(10, 50, 20, topRight)
drawAFlower(10, 50, 20, bottomLeft)
drawAFlower(10, 50, 20, bottomRight)

turtle.done()