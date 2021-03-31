import tkinter
import random

master = tkinter.Tk()

canvasHeight = 400
canvasWidth = 800

image = tkinter.Canvas(master, width=canvasWidth, height=canvasHeight)
image.pack()

for row in range(50):
    for col in range(100):
        x = image.create_rectangle(col*8, row*8, (col+1)*8, (row+1)*8, fill=random.choice( ("black","white","red","blue") ))

tkinter.mainloop()
