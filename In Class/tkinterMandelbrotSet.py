import tkinter
import random

master = tkinter.Tk()

canvasHeight = 400
canvasWidth = 800
cellSize = 5

image = tkinter.Canvas(master, width=canvasWidth, height=canvasHeight)
image.pack()

for row in range(canvasHeight//cellSize):
    for col in range(canvasWidth//cellSize):
        if isInMandelbrot(row, col):
            color = "black"
        else:
            color = "white"

        x = image.create_rectangle(col*cellSize, row*cellSize, (col+1)*cellSize, (row+1)*cellSize, fill=color)

tkinter.mainloop()
