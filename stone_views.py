
import math
def print_grid(puzzle):
    list1=[' ']+[' '+item+' |' for item in puzzle]
    length=len(puzzle)
    iter_=math.ceil(math.sqrt(length))

    fallout=(iter_)**2-length
    if fallout:
        list1=list1+['   |']*fallout

    for i in range(0,length,iter_):
        print('+---'*(iter_)+'+')
        pp=''.join(list1[i+1:i+iter_+1])
        print('|'+ pp)
    
    print('+---'*(iter_)+'+')


print_grid('    ')