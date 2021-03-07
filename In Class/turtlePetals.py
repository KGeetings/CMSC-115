import turtle

petal_length = 15
petal_angle = 50
num_petals = 360 // petal_angle // 2

for petals in range(num_petals):
    if petals % 3 == 0:
        turtle.color("red")
    elif petals % 3 == 1:
        turtle.color("pink")
    else:
        turtle.color("purple")
   
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(petal_length)
        turtle.left(petal_angle)
        turtle.fd(petal_length)
        turtle.left(petal_angle)
        turtle.fd(petal_length)
        turtle.left(180 - 2 * petal_length)
    turtle.left(360/num_petals)
    turtle.end_fill()
turtle.exitonclick()
