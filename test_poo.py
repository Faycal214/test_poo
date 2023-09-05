import random

class player :
    def __init__(self,pseudo,health):
        self.pseudo=pseudo
        self.health=health
        print(f"bienvenue le joueur {pseudo} | point de vie {health}")
    
    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health

pseudo_1=str(input("donner le nom de 1ere joueur :"))
pseudo_2=str(input("donner le nom de 2ere joueur :"))

joueur_1=player(pseudo_1,100)
joueur_2=player(pseudo_2,100)

# dans ce jeu, les joueurs auront deux chances d'attaquer, si l'attaque rèussit
# il fera des dègats a l'autre joueur, sinon ce sera le tour de l'autre joueur
# et vice versa, le joueur avec le plus de points de vie gagne

i=1
j=1
somme1=0
somme2=0
boolean=[True,False]

for n in range(1,5):
    
    if(n % 2 != 0):
        print(f"le tour {i} de {joueur_1.pseudo}: ")
        bool=random.choice(boolean)
        
        if(bool==True):
            print(f"l'attaque de {joueur_1.pseudo} est rèussit")
            nb=random.randint(0,50)
            somme1 += nb
            joueur_2.health -= nb
            print(f"il a fait un dègat de {nb} au {joueur_2.pseudo}")
            print(f"vie {joueur_1.pseudo} est {joueur_1.health} | vie {joueur_2.pseudo} est {joueur_2.health}\n")
        
        if(bool==False):
            print(f"l'attaque de {joueur_1.pseudo} est echouè\n")
        
        i += 1
    
    if(n % 2 == 0):
        print(f"le tour {j} de {joueur_2.pseudo}: ")
        bool=random.choice(boolean)
        
        if(bool==True):
            print(f"l'attaque de {joueur_2.pseudo} est rèussit")
            nb=random.randint(0,50)
            somme2 += nb
            joueur_1.health -= nb
            print(f"il a fait un dègat de {nb} au {joueur_1.pseudo}")
            print(f"vie {joueur_2.pseudo} est {joueur_2.health} | vie {joueur_1.pseudo} est {joueur_1.health}\n")
        
        if(bool==False):
            print(f"l'attaque de {joueur_2.pseudo} est echouè\n")
        
        j += 1
    
if(somme1 > somme2):
    print(f"{joueur_1.pseudo} a gagnè")
else :
    print(f"{joueur_2.pseudo} a gagnè")