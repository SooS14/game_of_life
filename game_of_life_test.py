from tkinter import *
import numpy as np
import copy
import time


#========== var globales =============

nbl = 100
nbc = 100
tour = 0
world = np.zeros((nbl+2,nbc+2))

"""
#ruche :

world[53][56] = 1
world[53][55] = 1
world[54][54] = 1 ; world[54][56] = 1
world[55][54] = 1 ; world[55][56] = 1
world[56][55] = 1

"""

"""
#génération de planeurs :

world[55][55] = 1
world[55][56] = 1
world[56][55] = 1
world[56][54] = 1
world[57][55] = 1
"""

"""
#pulsar : oscillateur de période 3

world[48][48] = 1;world[49][48] = 1;world[50][48] = 1;world[51][48] = 1;world[52][48] = 1
world[48][52] = 1;world[49][52] = 1;world[50][52] = 1;world[51][52] = 1;world[52][52] = 1
world[48][50] = 1
world[52][50] = 1
"""

"""
#pintadecathlon : oscillateur de période 15
world[50][45] = 1;world[50][46] = 1;world[50][47] = 1;world[50][48] = 1;world[50][49] = 1
world[50][50] = 1;world[50][51] = 1;world[50][52] = 1;world[50][53] = 1;world[50][54] = 1
"""

"""
#vaisseaux spatiaux
world[50][5] = 1;world[50][6] = 1;world[50][7] = 1;world[50][8] = 1;world[50][9] = 1;world[50][10] = 1
world[51][4] = 1;world[51][10] = 1
world[52][10] = 1
world[53][4] = 1;world[53][9] = 1;
world[54][6] = 1;world[54][7] = 1;

world[20][5] = 1;world[20][6] = 1;world[20][7] = 1;world[20][8] = 1;world[20][9] = 1
world[21][4] = 1;world[21][9] = 1
world[22][9] = 1
world[23][4] = 1;world[23][8] = 1;
world[24][6] = 1;

world[70][5] = 1;world[70][6] = 1;world[70][7] = 1;world[70][8] = 1
world[71][4] = 1;world[71][8] = 1
world[72][8] = 1
world[73][4] = 1;world[73][7] = 1;
"""


#canon à planeur
world[80][3] = 1;world[80][4] = 1
world[81][3] = 1;world[81][4] = 1

world[82][36] = 1;world[82][37] = 1
world[83][36] = 1;world[83][37] = 1

world[77][14] = 1;world[77][15] = 1
world[78][13] = 1;world[78][17] = 1
world[79][12] = 1;world[79][18] = 1
world[80][12] = 1;world[80][16] = 1;world[80][18] = 1;world[80][19] = 1
world[81][12] = 1;world[81][18] = 1
world[82][13] = 1;world[82][17] = 1
world[83][14] = 1;world[83][15] = 1

world[79][26] = 1
world[80][24] = 1;world[80][26] = 1
world[81][22] = 1;world[81][23] = 1
world[82][22] = 1;world[82][23] = 1
world[83][22] = 1;world[83][23] = 1
world[84][24] = 1;world[84][26] = 1
world[85][26] = 1

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
                    can1.create_rectangle(j*10-5,i*10-5,j*10+5,i*10+5, fill='grey') 
            else :
                if count == 3 :
                    future_world[i][j] = 1
                    can1.create_rectangle(j*10-5,i*10-5,j*10+5,i*10+5, fill='red')

                    
def game_of_life() :
    global nbl, nbc, world, future_world, tour
    #print(tour)
    tour += 1
    #print_tab(world, nbl+2, nbc+2)
    
    birth_and_death(future_world, world, nbl, nbc)

    if np.array_equal(future_world,world,equal_nan=False):
        print('stable !')
    else :
        world = copy.deepcopy(future_world)
        texte.configure(text="Compteur:"+str(tour))
        fen1.after(250,game_of_life)
                     
        


fen1 = Tk()
fen1.title("The Game of Life")


can1 = Canvas(fen1,bg='grey',height=(nbc*10), width=(nbl*10))
can1.pack(side=LEFT, padx =5, pady =5)

for i in range(0, nbl):
    for j in range(0, nbc):
        if world[i][j] == 1:
            can1.create_rectangle(j*10-5,i*10-5,j*10+5,i*10+5, fill='red')

bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width =8, command=game_of_life)
bou2.pack()
texte = Label(fen1,text="Compteur:0")
texte.pack()
fen1.mainloop()
fen1.destroy()
