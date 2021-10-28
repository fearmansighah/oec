import numpy as np

# initialise GUI for user's grid
def init_grid(xdims, ydims):
    beforeStart = "  |"
    for i in range(xdims):
        beforeStart+=f' {i} |' 


    startEnd = "--+"
    for i in range(ydims):
        startEnd+="---+" 

    boxes = np.empty((xdims,ydims),dtype='str')
    for i in range(xdims):
        for j in range(ydims):
            boxes[i][j] = "x"

    return boxes, beforeStart, startEnd

# display GUI of user's grid everytime they select a tile
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