import tkinter
import random
import time

class Grid_sim:

    # Number of cells high and wide:
    WIDTH = 40
    HEIGHT = 30
    
    # Size of each cell, in pixels
    SCALE = 20
    
    # (Maximum) number of frames per second
    FPS = 20

    def __init__(self):
        # Create a master window
        self.master = tkinter.Tk()
        self.master.title("Grid Simulator")

        # Create a 'canvas' object, and put it in the master window
        self.canvas = tkinter.Canvas(self.master, width=self.WIDTH * self.SCALE, height=self.HEIGHT * self.SCALE)
        self.canvas.pack()
        
        # Create a grid of data to store the problem
        self.make_data_grid()
        
        # Create a grid of 'rectangle' objects on the Canvas
        self.make_canvas_grid()
        
        # Schedule the 'update_grid' function to run in 10 ms
        self.update_time = int(1 / self.FPS * 1000)
        self.canvas.after(self.update_time, self.update_grid)

    def make_data_grid(self):
        """ This method will create a "data grid" variable for this Grid_sim object.
            This is a two-dimensional list of integer values, each representing whatever
            value is stored in each cell of the grid for this particular simulation.
            Initializes to all 0.
        """
        self.data_grid = []
        for row in range(self.HEIGHT):
            self.data_grid.append([])
            for col in range(self.WIDTH):
                if random.randrange(4) == 0:
                    self.data_grid[row].append(True)
                else:
                    self.data_grid[row].append(False)        
        
    def make_canvas_grid(self):
        """ This method creates a "canvas grid".  This is a 2-D list of "rectangle"
            objects on the canvas.  These are stored in the grid so that they can be 
            updated quickly when that cell's data value changes.
        """
        self.canvas_grid = []
        for row in range(self.HEIGHT):
            self.canvas_grid.append([])
            for col in range(self.WIDTH):
                rectangle = self.canvas.create_rectangle(col*self.SCALE,row*self.SCALE,\
                        (col+1)*self.SCALE,(row+1)*self.SCALE, fill="white", outline="black")
                self.canvas_grid[row].append(rectangle)
        self.canvas.update()
        
    def update_grid(self):
        # Update the data grid
        next_gen = []

        for r in range(self.HEIGHT):
            next_gen.append([])
            for c in range(self.WIDTH):
                alive_neighbors = self.count_neighbors(r,c)

                if self.data_grid[r][c] == True:
                    if alive_neighbors == 2 or alive_neighbors == 3:
                        this_cell = True
                    else:
                        this_cell = False
                else:
                    if alive_neighbors == 3:
                        this_cell = True
                    else:
                        this_cell = False

                next_gen[r].append(this_cell)
                   
        self.data_grid = next_gen    
        
        # Update the canvas grid, based on what's in the data grid
        for r in range(self.HEIGHT):
            for c in range(self.WIDTH):
                color = "black"
                if self.data_grid[r][c] == 0: color = "white"
                if self.data_grid[r][c] == 1: color = "green"
                if self.data_grid[r][c] == 2: color = "blue"
                if self.data_grid[r][c] == 3: color = "yellow"
                if self.data_grid[r][c] == 4: color = "purple"
                if self.data_grid[r][c] == 5: color = "red"
                self.canvas.itemconfig(self.canvas_grid[r][c], fill=color, outline="black")
            
            
        # Update the canvas based on the new Rectangle colors
        self.canvas.update()
        
        # Schedule the update_grid function to run again after a bit.
        self.canvas.after(self.update_time, self.update_grid)

gs = Grid_sim()

tkinter.mainloop()