# Tic - Tac - Toe


# normalisation

 # dico_color = {element_grille : }


global grille
global end
global comb_gagnantes


grille = [1, 2, 3, 4, 5, 6, 7, 8, 9]
end = False
comb_gagnantes = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

# Affichage de la grille du jeu

def affiche_grille():
    print(grille[0], grille[1], grille[2])
    print(grille[3], grille[4], grille[5])
    print(grille[6], grille[7], grille[8])
    print()

# fonction assurant que l'on ne puisse coché une case déjà coché

def occupation_grille_1():
     n = nombre_choisi()
     if grille[n] == "X" or grille[n] == "O":
        print("\n Tu ne peux pas aller là. Essaie encore !")
        occupation_grille_1()
     else:
            grille[n] = "X"

def occupation_grille_2():
    n = nombre_choisi()
    if grille[n] == "X" or grille[n] == "O":
        print("\n Tu ne peux pas aller là. Essaie encore !")
        occupation_grille_2()
    else:
        grille[n] = "O"





# fonction vérifiant que l'input donné par l'utilisateur est du type nombre

def nombre_choisi():

    while True:
        val = input()
        try:
            val = int(val) - 1
            if -1 < val < len(grille):
                return val
            else:
                print("\nCe n'est pas dans la grille. Essaie encore")
        except ValueError:
           print("\nCe n'est pas un nombre. Essaie encore")

# Vérifie si la grille est gagnante pour un utilisateur
def verif_grille():
    global end
    global grille
    global comb_gagnantes
    compt = 0
    for a in comb_gagnantes:
        if grille[a[0]] == grille[a[1]] == grille[a[2]] == "X":
            print(" Joueur 1 gagne !\n")
            print(" Félicitations !\n")
            return True

        if grille[a[0]] == grille[a[1]] == grille[a[2]] == "O":
            print("Joueur 2 gagne !\n")
            print(" Félicitations !!!\n")
            return True
    for cellule in grille:
         if str(cellule) in "XO":
             compt += 1
         if all(str(cellule) in "XO" for cellule in grille):
           print("Match Nul\n")
           return True

# Interaction entre utilisateurs
"""if input(" Rejouer une partie (y/n)\n") == "y":
    print()
    tic_tac_toe()"""



def tic_tac_toe():
    end = False
    while not end:
        affiche_grille()
        end = verif_grille()
        if end == True:
            break
        print(" Joueur 1 choisit où placer une croix ")
        occupation_grille_1()
        print()
        affiche_grille()
        end = verif_grille()
        if end == True:
            break
        print("Joueur 2 choisit où placer un rond")
        occupation_grille_2()
        print()


tic_tac_toe()
