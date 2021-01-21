import numpy as np
import copy


#========== var globales =============

nbl = 10
nbc = 10
world = np.zeros((nbl+2,nbc+2))
world[5][3] = 1
world[5][4] = 1
world[5][5] = 1
world[5][6] = 1
world[5][7] = 1
world[4][4] = 1
future_world = copy.deepcopy(world)



def print_tab(tab,nbl,nbc):
    for i in range(0,nbl):
        print(tab[i])

def birth_and_death(future_world, world, nbl, nbc):

    for i in range(1, nbl+1):
        for j in range(1, nbc+1):
            count = 0
            if world[i+1][j+1] == 1 :
                count += 1
            if world[i+1][j] == 1 :
                count += 1
            if world[i+1][j-1] == 1 :
                count += 1
            if world[i][j-1] == 1 :
                count += 1
            if world[i-1][j-1] == 1 :
                count += 1
            if world[i-1][j] == 1 :
                count += 1
            if world[i-1][j+1] == 1 :
                count += 1
            if world[i][j+1] == 1 :
                count += 1
                    
            if world[i][j] == 1 :
                if (count != 2) and (count != 3) :
                    future_world[i][j] = 0
            else :
                if count == 3 :
                    future_world[i][j] = 1




     
def game_of_life(future_world, world, nbl, nbc) :
    
    tour = 0
    while (tour < 100) :
        print(tour)
        tour += 1
        print_tab(world, nbl+2, nbc+2)
        birth_and_death(future_world, world, nbl, nbc)

        if np.array_equal(future_world,world,equal_nan=False) :
            print('Stable !')
            return
        else :
            world = copy.deepcopy(future_world)
    print('fin !')
                     
        
game_of_life(future_world, world, nbl, nbc)
