import random as rd

#Fonctionsnécessaires

def jouer_un_coup(c,M):
    return modif_coordonées(c,M)


def is_game_over(M):
    return M[0][0] == 1998

def move_possible(M,c):
    return True

def init_game(n=5):
    M = remplissage_taille(n)
    return ajout_bombes(M,6)

def is_game_won(M):
    m=0
    for k in range(5):
        for i in range (5):
            if M[i][k] <= 8:
                m+=1
    return m == 0



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


def jouer_un_coup(c,M):
    return modif_coordonées(c,M)

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




def jouer_un_coup00(M):
    return jouer_un_coup([0,0],M)

def jouer_un_coup01(M):
    return jouer_un_coup([0,1],M)

def jouer_un_coup02(M):
    return jouer_un_coup([0,2],M)

def jouer_un_coup03(M):
    return jouer_un_coup([0,3],M)

def jouer_un_coup04(M):
    return jouer_un_coup([0,4],M)

def jouer_un_coup10(M):
    return jouer_un_coup([1,0],M)

def jouer_un_coup11(M):
    return jouer_un_coup([1,1],M)

def jouer_un_coup12(M):
    return jouer_un_coup([1,2],M)

def jouer_un_coup13(M):
    return jouer_un_coup([1,3],M)

def jouer_un_coup14(M):
    return jouer_un_coup([1,4],M)


def jouer_un_coup20(M):
    return jouer_un_coup([2,0],M)

def jouer_un_coup21(M):
    return jouer_un_coup([2,1],M)

def jouer_un_coup22(M):
    return jouer_un_coup([2,2],M)

def jouer_un_coup23(M):
    return jouer_un_coup([2,3],M)

def jouer_un_coup24(M):
    return jouer_un_coup([2,4],M)

def jouer_un_coup30(M):
    return jouer_un_coup([3,0],M)

def jouer_un_coup31(M):
    return jouer_un_coup([3,1],M)

def jouer_un_coup32(M):
    return jouer_un_coup([3,2],M)

def jouer_un_coup33(M):
    return jouer_un_coup([3,3],M)

def jouer_un_coup34(M):
    return jouer_un_coup([3,4],M)

def jouer_un_coup40(M):
    return jouer_un_coup([4,0],M)

def jouer_un_coup41(M):
    return jouer_un_coup([4,1],M)

def jouer_un_coup42(M):
    return jouer_un_coup([4,2],M)

def jouer_un_coup43(M):
    return jouer_un_coup([4,3],M)


def jouer_un_coup44(M):
    return jouer_un_coup([4,4],M)





from tkinter import *

color_dico={1998:["#000000",''],0:["#000000",''],9:["#000000",''],100:["#9cff00",'0'],101:["#ff9000",'1'],102:["#d0630b",'2'],103:["#ff2df3",'3'],104:["#ff1e00",'4']}

dico_command={1:[jouer_un_coup00,'',[0,0]],2:[jouer_un_coup01,'',[0,1]],3:[jouer_un_coup02,'',[0,2]],4:[jouer_un_coup03,'',[0,3]],5:[jouer_un_coup10,'',[1,0]],6:[jouer_un_coup11,'',[1,1]],7:[jouer_un_coup12,'',[1,2]],8:[jouer_un_coup13,'',[1,3]],9:[jouer_un_coup20,'',[2,0]],10:[jouer_un_coup21,'',[2,1]],11:[jouer_un_coup22,'',[2,2]],12:[jouer_un_coup23,'',[2,3]],13:[jouer_un_coup30,'',[3,0]],14:[jouer_un_coup31,'',[3,1]],15:[jouer_un_coup32,'',[3,2]],16:[jouer_un_coup33,'',[3,3]],17:[jouer_un_coup04,'',[0,4]],18:[jouer_un_coup14,'',[1,4]],19:[jouer_un_coup24,'',[2,4]],20:[jouer_un_coup34,'',[0,4]], 21:[jouer_un_coup40,'',[4,0]],22:[jouer_un_coup41,'',[4,1]],23:[jouer_un_coup42,'',[4,2]],24:[jouer_un_coup43,'',[4,3]],25:[jouer_un_coup44,'',[4,4]]}

GRID_LEN = 5
GRID_PADDLE = 5
SIZE = 500


def info_necessary():
    return GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won


