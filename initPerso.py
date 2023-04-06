from personne import personnage


def initVagueTrolls(vague, n, x):
    for i in range(n):
        x+=1
        vague.append(personnage("Troll "+str(x), "Troll", 5, 4, 0, 0))
    return(vague)

# Les méchants sont initialisés dans une liste de listes, chaque liste agissant comme une vague d'ennemis
vilains = [[], [], [], [], []]
for i in range(3):
    vilains[i] = initVagueTrolls(vilains[i], i + 3, (i * (i + 1)) // 2 + 2 * i)

vilains[3].append(personnage("Troll le Troll", "Troll Guerrier", 10, 4, 0, 0))
vilains[3].append(personnage("Spyro le Petit Dragon", "Petit Dragon", 8, 5, 1, 0))

vilains[4].append(personnage("Smaug le Dragon", "Dragon", 15, 6, 2, 0))

# Les héros sont initialisés dans un dictionnaire.
heros = {"Guerrier": personnage("Ares le Guerrier", "Guerrier", 10, 5, 0, 0),
         "Chasseur": personnage("Artemis le Chasseur", "Chasseur", 10, 3, 0, 0),
         "Guerisseur": personnage("Apollo le Guerisseur", "Guerisseur", 10, 1, 0, 2),
         "Mage": personnage("Athena le Mage", "Mage", 10, 4, 2, 0)}