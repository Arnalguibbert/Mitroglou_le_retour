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




def jouer_coup(c,M):
    return modif_coordonées(c,M)


#InterfaceGraphique



BACKGROUND_COLOR_CASE={0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}




DICO_COMMAND={&:jouer_un_coup([0,0],M),é:jouer_un_coup([0,1],M),"":jouer_un_coup([0,2],M),'':jouer_un_coup([0,3],M),a:jouer_un_coup([1,0],M),z:jouer_un_coup([1,1],M),e:jouer_un_coup([1,2],M),r:jouer_un_coup([1,3],M),q:jouer_un_coup([2,0],M),s:jouer_un_coup([2,1],M),d:jouer_un_coup([2,2],M),f:jouer_un_coup([2,3],M),w:jouer_un_coup([3,0],M),x:jouer_un_coup([3,1],M),c:jouer_un_coup([3,2],M),v:jouer_un_coup([3,3],M)}
