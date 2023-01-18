import time
from objects import *

balance = 0
owner = "P'titLu"
agios = 10
authorized_overdraft = -200
amount = ()

account = Current_account(balance, owner, agios, authorized_overdraft, amount)

print("Bienvenue dans la P'tit LuCrative (banque à but lucratif)")

while True:
    choice = input("Que souhaitez-vous faire? \n 1: Un dépôt. \n 2: Un retrait. \n 3: Consulter mes comptes. \n 4: Effectuer un virement. \n 5: Quitter. \n")

    if choice == "1":
        amount = int(input("Quel montant voulez-vous déposer? \n"))
        account.__payment__(amount)
        # Code pour effectuer le dépôt ici
        time.sleep(8)
        break
    
    elif choice == "2":
        amount = int(input("Quel montant souhaitez-vous retirer? \n"))
        # Code pour effectuer le retrait ici
        time.sleep(8)
        break
       
    elif choice == "3":
        account = input("Quel compte souhaitez-vous consulter? \n")
        # Code pour afficher les informations du compte ici
        
    elif choice == "4":
        transfer_type = input("1: Compte courant vers compte épargne. \n 2: Epargne vers compte courant. \n")
        # Code pour effectuer le virement ici
        print("Virement effectué avec succès!")
        time.sleep(8)
        break
    
    elif choice == "5":
        print("Au revoir!")
        time.sleep(3)  
        break
    else:
        print("ERREUR: Veuillez choisir l'une des propositions: \n 1: pour un dépôt. \n 2: pour un retrait. \n 3: pour consulter vos comptes. \n 4: pour effectuer un virement. \n 5: pour quitter.")
