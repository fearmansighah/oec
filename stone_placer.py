import numpy as np
import random

class grid:
    def __init__(self, size):
        self.xdims = size[0]
        self.ydims = size[1]

    def generate_cells(self):
        shape = (self.xdims, self.ydims)
        grid = np.zeros(shape,int)

        return grid

    def generate_stones(self, num_stones, grid):
        possible_locations = []
        num_tiles = self.xdims * self.ydims
        for i in range(self.xdims):
            for j in range(self.ydims):
                possible_locations.append([i,j])

        stone_locations = random.sample(possible_locations, num_tiles)
    
        for i in range(num_stones):
            x_loc = stone_locations[i][0]
            y_loc = stone_locations[i][1]
            grid[x_loc, y_loc] = 1
    


stone_status = grid(16, 16)

stones_grid_status = stone_status.generate_cells()
print(stones_grid_status)

stone_status.generate_stones(num_stones=40, grid=stones_grid_status)
print(stones_grid_status)