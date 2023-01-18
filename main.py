from objects import *
import time

print("Bienvenue dans la P'tit Lu's BANK!")

while True:
    choice = input("Que souhaitez-vous faire? \n 1: Un dépôt. \n 2: Un retrait. \n 3: Consulter mes comptes. \n 4: Effectuer un virement. \n 5: Quitter. \n")

    if choice == "1":
        transaction = int(input("Quel montant voulez-vous déposer? \n"))
        # Code pour effectuer le dépôt ici
        print("Dépôt effectué avec succès!")
        
    elif choice == "2":
        transaction = int(input("Quel montant souhaitez-vous retirer? \n"))
        # Code pour effectuer le retrait ici
        print("Retrait effectué avec succès!")
        
    elif choice == "3":
        account_choice = input("Quel compte souhaitez-vous consulter? \n")
        # Code pour afficher les informations du compte ici
        
    elif choice == "4":
        transfer_type = input("1: Compte courant vers compte épargne. \n 2: Epargne vers compte courant. \n")
        # Code pour effectuer le virement ici
        print("Virement effectué avec succès!")
        
    elif choice == "5":
        print("Au revoir!")
        time.sleep(3)  
        break
    else:
        print("ERREUR: Veuillez choisir l'une des propositions: \n 1: pour un dépôt. \n 2: pour un retrait. \n 3: pour consulter vos comptes. \n 4: pour effectuer un virement. \n 5: pour quitter.")