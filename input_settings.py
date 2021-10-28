def set_size():
    z = 1

    while z == 1:
        size = int(input('''
1. small 9x9 grid with 10 stones
2. medium 16x16 with 40 stones
3. large 16x30 with 99 stones
4. demo 3x3 with 2 stones

select 1, 2 , 3 or 4 to choose your settings: '''))

        if size == 1:
            xdims = 9
            ydims = 9
            num_stones = 10
            z = 0
        
        elif size == 2:
            xdims = 16
            ydims = 16
            num_stones = 40
            z = 0
        
        elif size == 3:
            xdims = 16
            ydims = 30
            num_stones = 99
            z = 0
        
        elif size == 4:
            xdims = 3
            ydims = 3
            num_stones = 2
            z = 0
        
        else:
            print('invalid input, try again! \n')

       
       
    print(f'grid size selcted: {xdims}x{ydims}')
    print(f'number of stones in grid: {num_stones}')

    return xdims, ydims, num_stones



