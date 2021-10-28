import numpy as np
import random

def stonessurrounding(i,j,max_grid_i,max_grid_j,grid):
    
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

                if(iter_i < 0 or iter_j<0 or iter_i > max_grid_i-1 or iter_j > max_grid_j-1):
                    value = value
                else:
                    value = value + grid[iter_i][iter_j]

                iter_j  += 1

            iter_i += 1
            iter_j = j-1

        # value holds the sum of the squares around the cell 
        #in which  the user selects

        return value


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


# creating a function to accept user inputs
def set_size():
    z = 1

    while z == 1:
        size = int(input('''
1. small 9x9 grid with 10 stones
2. medium 16x16 with 40 stones
3. large 16x30 with 99 stones
4. demo 3x3 with 3 stones

select 1, 2 or 3 to choose your settings: '''))

        if size == 1:
            xdims = 9
            ydims = 9
            num_stones = 10
        
        elif size == 2:
            xdims = 16
            ydims = 16
            num_stones = 40
        
        elif size == 3:
            xdims = 16 
            ydims = 30
            num_stones = 99
        
        elif size == 4:
            xdims = 3
            ydims = 3
            num_stones = 3

        z = 0
       

    return xdims, ydims, num_stones

def init_grid(xdims, ydims):
    beforeStart = "  |"
    for i in range(xdims):
        beforeStart+=f' {chr(65+i)} |' 


    startEnd = "--+"
    for i in range(ydims):
        startEnd+="---+" 

    boxes = np.empty((xdims,ydims),dtype='str')
    for i in range(xdims):
        for j in range(ydims):
            boxes[i][j] = "x"

    return boxes, beforeStart, startEnd


def disp_grid(coords,val, boxes, beforeStart, startEnd, initialise, xdims, ydims):

    x,y = coords

    
    if initialise == "start":
        val = "x"
    else:
        boxes[x][y] = val

    print(beforeStart)
    print(startEnd)

    for i in range(xdims):
        print(f'{i:>2}|', end="")
        for j in range(ydims):
            print(f' {boxes[i][j]} |', end="")
        print("\n",end="")
        print(startEnd)

xdims, ydims, num_stones = set_size()
boxes, beforeStart, startEnd = init_grid(xdims, ydims)

###############

stone_status = grid(xdims,ydims)

stones_grid_status = stone_status.generate_cells()
print(stones_grid_status)

stone_status.generate_stones(num_stones=num_stones, grid=stones_grid_status)
print(stones_grid_status)

####################

disp_grid((0,0), 0, boxes, beforeStart, startEnd, "start", xdims, ydims)

####################

max_grid_i = xdims
max_grid_j = ydims
num_of_guesses = 0
num_of_eboxes = max_grid_i*max_grid_j - num_stones
coordinates_guessed = [(-1,-1)]

guessIdx=random.sample(range(num_of_eboxes), num_of_eboxes)

z = 1
while(z == 1):
    allCoords = []
    for i in range(max_grid_i):
        for j in range(max_grid_j):
              allCoords.append((i,j))

    guesses = []
    for i in range(num_of_eboxes):
        guesses.append(allCoords[guessIdx[i]])

    for i in guesses:
        x,y = i
        if (x > max_grid_i-1 or y > max_grid_j-1 or x < 0 or y < 0):
            print("please re-evaluate coordinates")
            continue
        if (x,y) in coordinates_guessed:
            num_of_guesses = num_of_guesses
            print('coordinates already cleared')
            continue
        else:
            num_of_guesses = num_of_guesses + 1
            coordinates_guessed.append((x,y))
        if num_of_guesses == num_of_eboxes:
            print('Field Cleared!')
            break

        value = stonessurrounding(int(x),int(y),max_grid_i,max_grid_j, stones_grid_status)
        
        if value == 9:
            break

    disp_grid((x,y), value, boxes, beforeStart, startEnd, "play", xdims, ydims)
