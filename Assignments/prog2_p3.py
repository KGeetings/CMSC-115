import turtle

#simple way of figuring the degree turn
userSides = int(input("Enter the number of sides for your polygon: "))
angle = 360 / userSides

for move in range(userSides):
  turtle.speed(0)
  turtle.forward(2)
  turtle.right(angle)

turtle.exitonclick()