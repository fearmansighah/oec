from input_settings import set_size
from stones import grid

def main():
    ###############

    xdims, ydims, num_stones = set_size() # initialise settings
    stone_grid = grid(xdims,ydims) # initialise stone grid class
    boxes, beforeStart, startEnd = stone_grid.init_grid() # initialise user's grid

    ###############

    # deploying stones

    stones_grid_status = stone_grid.generate_cells()
    #print(stones_grid_status)
    #print('')

    stone_grid.generate_stones(num_stones, stones_grid_status)
    #print(stones_grid_status)
    #print('')

    ####################

    stone_grid.disp_grid((0,0), 0, boxes, beforeStart, startEnd, "start")
    print('')

    ####################

    #begin game 

    num_of_guesses = 0
    num_of_eboxes = xdims*ydims - num_stones
    coordinates_guessed = [(-1,-1)]

    z = 1
    while(z == 1):

        x = ord(input('column letter: ')) - 65
        y = int(input('row number: '))

        # neighbor detection algorithm
        if (x > xdims-1 or y > ydims-1 or x < 0 or y < 0):
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
            print('field Cleared!')
            break
                
        value = stone_grid.stones_surrounding(x,y,stones_grid_status)
        
        if value == 9:
            break        

        stone_grid.disp_grid((x,y), value, boxes, beforeStart, startEnd, "play")
        print('')

if __name__ == "__main__":
    main()