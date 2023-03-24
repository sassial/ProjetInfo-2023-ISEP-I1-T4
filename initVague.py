from personne import personnage

def initVagueTrolls(vague, n, x):
    for i in range(n):
        x+=1
        vague.append(personnage("Troll "+str(x), "Troll", 5, 4, 0, 0))
    return(vague)