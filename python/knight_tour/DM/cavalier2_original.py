# -*- coding : utf-8 -*-



from random import randint  # Module importé

N = 6; HISTORIQUE = []      # Variables globales


def afficher():
    """ Dessine la grille  n x n """
    liste = [' .'] * (N**2)
    for i in range(len(HISTORIQUE)):
        (x,y) = HISTORIQUE[i]
        liste[x + y * N] = i

    Espace = "\n" * 15
    Titre = "TOUR {}. Cavalier en {}.\n\n".format(len(HISTORIQUE), (x,y))
    L1 = " " + ("|{:2} " * N)[1:] + "\n"
    L2 = " " + ("+---"   * N)[1:] + "\n"
    Grille = (L1 + (L2 + L1) * (N-1)).format(*liste)
    print(Espace + Titre + Grille)


def proposer(x, y):
    """ Retourne sous forme de liste l'éventail des possibles. """
    poss  = []
    for dx,dy in [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]:
        if 0 <= x+dx < N and 0 <= y+dy < N and (x+dx, y+dy) not in HISTORIQUE:
            poss.append((dx,dy))
    return poss


def presenter(poss):
    """ Présenter les choix à l'utilisateur. """
    prop  = "CHOIX :"                   + "\n"
    prop += "    espace : arrière"      + "\n"
    prop += "    entrée : automatique"  + "\n"
    prop += "    autre  : hasard"       + "\n"
    for i in range(8):
        if i < len(poss):
            prop += "         {}:{}\n".format(i, poss[i])
        else:
            prop += "\n"
    print(prop)



def choisir(poss):
    """ Choisir le mouvement. """
    reponse = input(" ? ")
    if reponse == "": return poss[0] # Choix automatique :
    if reponse in "_ ": return (0,0) # On demande un retour en arrière
    try:
        return poss[int(p)]          # Choix de l'utilisateur
    except:
        return poss[randint(0, len(poss)-1)]  # Choix au hasard
    

def course(x=0, y=0):
    """ Faire avancer le cavalier autant que possible. """
    HISTORIQUE.append((x,y))
    afficher()

    while 1:
        (x,y) = HISTORIQUE[-1]
        poss = proposer(x, y)

        if poss == []:
            input("BLOQUE ! Seul choix possible : arrière." + "\n" * 13)
            (dx,dy) = (0,0)                  # on est coincé, donc : retour en arrière
        else:
            presenter(poss)
            (dx,dy) = choisir(poss)

        if (dx, dy) == (0,0):               # Retour en arrière
            if len(HISTORIQUE) > 1:         # Seulement si c'est possible !
                HISTORIQUE.pop()
        else:
            HISTORIQUE.append((x+dx, y+dy))

        afficher()    


if __name__ == '__main__': #==============MAIN==============
    print("Par défaut, la taille de la grille est de 6 * 6.")
    print("   - pour garder cette valeur, appuyer sur entrée,")
    p = input("   - sinon, proposer une valeur : ")
    try:
        assert 2 < int(p) < 12
        N = int(p)
    except:
        pass
    course()
    
    
