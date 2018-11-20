
import numpy as np




def liste_taille(n): M=[]
    for k in range(n):
        M+=[0 ]
    return (M)

def


remplissage_taille(n):
    M=[]
    for k in range(n):
        M.append(liste_taille(n))
    return M



def ajout_case(a,b,M ):
    M[a][b] = 2
    return M


def casedouble(M):
    L=[]
    for k in range(3):
        if M[k][1]==M [k ][2] == 1:
            L = [k,0]
        if M[k][0]==M [k ][1] == 1:
            L = [k, 2]
        if M[1][k]==M [2 ][k] == 1:
            L = [0, k]
        if M[1][k]==M [0 ][k] == 1:
            L = [2, k]
        if M[k][0]==M [k ][2] == 1 and M[k][1] == 0:
            L = [k,1]
        if M[0][k]==M [2 ][k] == 1 and M[1][k] == 0:
            L = [1,k]




    if

    M[0][0]== M [1][1] == 1:
        L = [2, 2]
    if M[2][2]== M [1][ 1] ==1:
        L = [0, 0]
    if M[0][2]== M [1][1] == 1:
        L = [2, 0]
    if M[2][0]== M [1][1]== 1 :
        L = [0, 2]
    return


L



def test_premier(M \
    ):

    if M[1][1] == 1 :
        M[0][0] = 2

    elif M[0][0] == 1 :
        M[1][1] = 2

    elif M[0][2] == 1 :
        M[1][1] = 2

    elif M[2][0] == 1 :
        M[1][1] = 2

    elif M[2][2] == 1 :
        M[1][1] = 2

    else:
        return test_aléa(M)
    return M



def test_aléa(M):
    for k in range(3):
        for i in range(3):
            if M[k][i] != 1:
                M[k][i] = 2
                return M



def tictac
    (a,b,M):

    if M[a][b] == 1 or M[a][b] == 2:
    return("gros naze")

M[a][b] = 1

if somme(M) == 1:
    return test_premier(M)

L  = casedouble(M)

p rint(L)

if len(L)==0:

    return test_aléa(M) K = ajo ut_case(L[0],L[1],M)

return K


def somme(M):
    c=0
    for k in range(3):
        for i in range (3):
            c+= M[k][i]
    return c





