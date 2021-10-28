import numpy as np
import random

# creating an object to handle deploying the stones    
class grid():
    
    def __init__(self, xdims, ydims):
        self.xdims = xdims
        self.ydims = ydims

    # initialise empty cells
    def generate_cells(self):
        shape = (self.xdims, self.ydims)
        grid = np.zeros(shape,int)

        return grid

    def generate_stones(self, num_stones, grid):
        possible_locations = []
        num_tiles = self.xdims * self.ydims
        
        # create a list of all possible coordinates
        for i in range(self.xdims):
            for j in range(self.ydims):
                possible_locations.append([i,j])

        # sample unque pairs randomly
        stone_locations = random.sample(possible_locations, num_tiles)

        # assign a unique pair of coordinates to stones
        for i in range(num_stones):
            x_loc = stone_locations[i][0]
            y_loc = stone_locations[i][1]
            grid[x_loc, y_loc] = 1


    # initialise GUI for user's grid
    def init_grid(self):
        beforeStart = "  |"
        for i in range(self.xdims):
            beforeStart+=f' {chr(65+i)} |' 


        startEnd = "--+"
        for i in range(self.ydims):
            startEnd+="---+" 

        boxes = np.empty((self.xdims,self.ydims),dtype='str')
        for i in range(self.xdims):
            for j in range(self.ydims):
                boxes[i][j] = "x"

        return boxes, beforeStart, startEnd

    # display GUI of user's grid everytime they select a tile
    def disp_grid(self, coords,val, boxes, beforeStart, startEnd, initialise):

        x,y = coords
        
        if initialise == "start":
            val = "x"
        else:
            boxes[x][y] = val

        print(beforeStart)
        print(startEnd)

        for i in range(self.xdims):
            print(f'{i:>2}|', end="")
            for j in range(self.ydims):
                print(f' {boxes[i][j]} |', end="")
            print("\n",end="")
            print(startEnd)


    def stones_surrounding(self, i,j, grid):
        
        iter_i = i-1 #i is input from user
        iter_j = j-1 # j is input  from use
        
        
        if(grid[i][j] == 1):
            #end the game
            print("game over")
            
            return 9
            
        else:
            value = 0
            max_i = iter_i+3
            max_j = iter_j+3
            
            #iterate through the cells around the cell that the user selects
            while (iter_i < max_i):
                while (iter_j < max_j):

                    if(iter_i == i and iter_j == j):
                        value = value

                    if(iter_i < 0 or iter_j<0 or iter_i > self.xdims-1 or iter_j > self.ydims-1):
                        value = value
                    else:
                        value = value + grid[iter_i][iter_j]

                    iter_j  += 1

                iter_i += 1
                iter_j = j-1

            # value holds the sum of the squares around the cell 
            #in which  the user selects

            return value

        
    
    