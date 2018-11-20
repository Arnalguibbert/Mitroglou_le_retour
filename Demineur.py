import random as rd
from tkinter import *


#remplir de bombes la matrice.

def liste_taille(n):
    M=[]
    for k in range(n):
        M+=[0]
    return M

def remplissage_taille(n):
    M=[]
    for k in range(n):
        M.append(liste_taille(n))
    return M














#mettre des bombes aléatoires,représentées par des 9


def ajout_bombes(M,n):

    for i in range(n):
        a,b = rd.randint(1,len(M)-1),rd.randint(1,len(M)-1)
        M[a][b] = 9

    return M


# On cherche ici à regarder la coordonnée choisie






def modif_coordonées(c, M):
    (a, b) = (c[0], c[1])
    n = len(M) - 1

    if M[a][b] == 9:

        print("grosse défaite")
        L=remplissage_taille(len(M))
        L[0][0] = 1998
        return (L)
        # premier cas : on tombe sur une bombe

    elif a == 0:  # deuxieme cas a == 0

        if b == 0:
            m = 0
            if M[a + 1][b] == 9:
                m += 1
            elif M[a][b + 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M

        elif b == n:
            m = 0
            if M[a + 1][b] == 9:
                m += 1
            elif M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M



        else:
            m = 0
            if M[a + 1][b] == 9:
                m += 1
            if M[a][b + 1] == 9:
                m += 1
            if M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M



    elif a == n:

        if b == 0:
            m = 0
            if M[a - 1][b] == 9:
                m += 1
            elif M[a][b + 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M


        elif b == n:
            m = 0
            if M[a - 1][b] == 9:
                m += 1
            elif M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M

        else:
            m = 0
            if M[a - 1][b] == 9:
                m += 1
            if M[a][b + 1] == 9:
                m += 1
            if M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M



    elif b == n:

        if a == 0:
            m = 0
            if M[a + 1][b] == 9:
                m += 1
            elif M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M

        elif a == n:
            m = 0
            if M[a - 1][b] == 9:
                m += 1
            elif M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M

        else:
            m = 0
            if M[a - 1][b] == 9:
                m += 1
            if M[a + 1][b] == 9:
                m += 1
            if M[a][b - 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M



    elif b == 0:

        if a == 0:
            m = 0
            if M[a + 1][b] == 9:
                m += 1
            elif M[a][b + 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M

        elif a == n:
            m = 0
            if M[a + 1][b] == 9:
                m += 1
            elif M[a][b + 1] == 9:
                m += 1
            M[a][b] = 100 + m
            return M

        else:

            m = 0
            if M[a + 1][b] == 9:
                m += 1
            if M[a][b + 1] == 9:
                m += 1
            if M[a - 1][b] == 9:
                m += 1
            M[a][b] = 100 + m
            return M


    else:
        m = 0
        if M[a + 1][b] == 9:
            m += 1
        if M[a][b + 1] == 9:
            m += 1
        if M[a - 1][b] == 9:
            m += 1
        if M[a][b - 1] == 9:
            m += 1
        M[a][b] = 100 + m

        return M




def jouer_un_coup(c,M):
    return modif_coordonées(c,M)






def init_grid():
    M=remplissage_taille(4)
    return(ajout_bombes(M,4))




#InterfaceGraphique



BACKGROUND_COLOR_CASE={0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}




DICO_COMMAND={"Keypress-1":jouer_un_coup([0,0],M),"Keypress-2":jouer_un_coup([0,1],M),"Keypress-3":jouer_un_coup([0,2],M),"Keypress-4":jouer_un_coup([0,3],M),"Keypress-a":jouer_un_coup([1,0],M),"Keypress-z":jouer_un_coup([1,1],M),"Keypress-e":jouer_un_coup([1,2],M),"Keypress-r":jouer_un_coup([1,3],M),"Keypress-q":jouer_un_coup([2,0],M),"Keypress-s":jouer_un_coup([2,1],M),"Keypress-d":jouer_un_coup([2,2],M),"Keypress-f":jouer_un_coup([2,3],M),"Keypress-w":jouer_un_coup([3,0],M),"Keypress-x":jouer_un_coup([3,1],M),"Keypress-c":jouer_un_coup([3,2],M),"Keypress-v":jouer_un_coup([3,3],M)}




from tkinter import *




size=500
grid_padd=5
M=[[0, 0, 0, 0], [0, 0, 0, 9], [0, 9, 101, 102], [0, 0, 0, 9]]
fenetre=Tk()

def creation_grid(GRID_LEN, color_dico, windows, grid_game, GRID_PADDLE, SIZE):
    for i in range(GRID_LEN):
        for j in range(GRID_LEN):
            Backroundcase=color_dico[grid_game[i][j]]
            cell=Frame(windows, bg=Backroundcase[0], width=SIZE / GRID_LEN, height=SIZE / GRID_LEN).grid(row=i, column=j, padx=GRID_PADDLE, pady=GRID_PADDLE)
            Label(cell,text=Backroundcase[1],bg=Backroundcase[0]).grid(row=i,column=j)


def create_fenetre_jeu():
    windows=Tk()
    windows.title('Game Interface')
    return windows

BACKGROUND_COLOR_CASE={0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}



def init_interface(f):
    size = 500
    grid_padd = 5
    M = init_grid
    creation_grid(4,BACKGROUND_COLOR_CASE, f, M, 5, 500)



