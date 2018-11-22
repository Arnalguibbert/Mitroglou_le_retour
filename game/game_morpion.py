#FONCTIONS VITALES:

def move_possible(M,r):
    return True

def init_game(n=3):
    M = remplissage_taille(n)
    return M


def jouer_un_coup(a,b,M):
    return(tictac_IA_forte(a,b,M))


def is_game_over(M):
    m=0
    for k in range(3):
        for i in range(3):
            if M[k][i] == 0:
                m+=1
    return m == 0


def is_game_won(M):
    return casetriple(M)





#Commande de jeu

def jouer_un_coup00(M):
    return jouer_un_coup(0,0,M)


def jouer_un_coup01(M):
    return jouer_un_coup(0,1,M)

def jouer_un_coup02(M):
    return jouer_un_coup(0,2,M)

def jouer_un_coup10(M):
    return jouer_un_coup(1,0,M)

def jouer_un_coup11(M):
    return jouer_un_coup(1,1,M)

def jouer_un_coup12(M):
    return jouer_un_coup(1,2,M)


def jouer_un_coup20(M):
    return jouer_un_coup(2,0,M)

def jouer_un_coup21(M):
    return jouer_un_coup(2,1,M)

def jouer_un_coup22(M):
    return jouer_un_coup(2,2,M)




#Fonctions qui permettent le jeu


def liste_taille(n):
    M = []
    for k in range(n):
        M += [0]
    return (M)


def remplissage_taille(n):
    M = []
    for k in range(n):
        M.append(liste_taille(n))
    return M


def somme(M):
    c = 0
    for k in range(3):
        for i in range(3):
            c += M[k][i]
    return c


def ajout_case(a, b, M):
    M[a][b] = 2
    return M

#code qui bloque les coups facile

def casedouble(M):
    L = []
    for k in range(3):
        if M[k][1] == M[k][2] == 1 and M[k][0] == 0:
            L = [k, 0]
        if M[k][0] == M[k][1] == 1 and M[k][2] == 0:
            L = [k, 2]
        if M[1][k] == M[2][k] == 1 and M[0][k] == 0:
            L = [0, k]
        if M[1][k] == M[0][k] == 1 and M[2][k] == 0:
            L = [2, k]
        if M[k][0] == M[k][2] == 1 and M[k][1] == 0:
            L = [k, 1]
        if M[0][k] == M[2][k] == 1 and M[1][k] == 0:
            L = [1, k]

    if M[0][0] == M[1][1] == 1 and M[2][2] == 0:
        L = [2, 2]
    if M[2][2] == M[1][1] == 1 and M[0][0] == 0:
        L = [0, 0]
    if M[0][2] == M[1][1] == 1 and M[2][0] == 0:
        L = [2, 0]
    if M[2][0] == M[1][1] == 1 and M[0][2] == 0:
        L = [0, 2]
    return L

#code du premier tour

def test_premier(M):
    if M[1][1] == 1:
        M[0][0] = 2

    elif M[0][0] == 1:
        M[1][1] = 2

    elif M[0][2] == 1:
        M[1][1] = 2

    elif M[2][0] == 1:
        M[1][1] = 2

    elif M[2][2] == 1:
        M[1][1] = 2

    else:
        return test_aléa(M)
    return M

#ajout d'une case linéairement

def test_aléa(M):
    for k in range(3):
        for i in range(3):
            if M[k][i] != 1:
                M[k][i] = 2
                return M


#IA effective

def tictac_IA_forte(a, b, M):
    if M[a][b] == 1 or M[a][b] == 2:
        return ("gros naze")

    M[a][b] = 1

    if somme(M) == 1:
        return test_premier(M)

    L = casedouble(M)

    print(L)

    if len(L) == 0:
        return test_aléa(M)
    K = ajout_case(L[0], L[1], M)

    return K

#IA aléatoire

def tictac_IA_nulle(a, b, M):

    if M[a][b] == 1 or M[a][b] == 2:
        return ("gros naze")

    M[a][b] = 1

    return test_aléa(M)


#victoire

def casetriple(M):
    L = []
    for k in range(3):
        if M[k][1] == M[k][2] == M[k][0]:
            return True
        if M[k][0] == M[k][1] == M[k][2]:
            return True
        if M[1][k] == M[2][k] == M[0][k]:
            return True
        if M[1][k] == M[0][k] == M[2][k]:
            return True
        if M[k][0] == M[k][2] == M[k][1]:
            return True
        if M[0][k] == M[2][k] == M[1][k]:
            return True

    if M[0][0] == M[1][1] == M[2][2]:
        return True
    if M[0][2] == M[1][1] == M[2][0]:
        return True

    return False


#Dicoassocié
GRID_LEN = 3
GRID_PADDLE = 5
SIZE = 500
color_dico = {0: ["#000000", ''], 1: ["#9cff00", 'X'], 2: ["#ff9000", 'O'], }
dico_command = {1: [jouer_un_coup00, '', [0, 0]], 2: [jouer_un_coup01, '', [0, 1]], 3: [jouer_un_coup02, '', [0, 2]],
                4: [jouer_un_coup10, '', [1, 0]], 5: [jouer_un_coup11, '', [1, 1]], 6: [jouer_un_coup12, '', [1, 2]],
                7: [jouer_un_coup20, '', [2, 0]], 8: [jouer_un_coup21, '', [2, 1]], 9: [jouer_un_coup22, '', [2, 2]]}


def info_necessary():
    return GRID_LEN,GRID_PADDLE,dico_command,color_dico,SIZE,init_game,is_game_over,move_possible,is_game_won
