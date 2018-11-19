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
        return ()
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





#InterfaceGraphique



BACKGROUND_COLOR_CASE={0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}




