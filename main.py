import time
from objects import *

balance = 0
owner = "P'tit Lu"
agios = 10
authorized_overdraft = -200
amount = ()
interest = 5

account = Current_account(balance, owner, agios, authorized_overdraft, amount)

print("Bienvenue dans la P'tit LuCrative (banque à but Lucratif)")

while True:
    choice = input("Que souhaitez-vous faire? \n 1: Un dépôt. \n 2: Un retrait. \n 3: Consulter mes comptes. \n 4: Effectuer un virement. \n 5: Quitter. \n")

    if choice == "1":
        amount = float(input("Quel montant voulez-vous déposer? \n"))
        account.__payment__(amount)
        time.sleep(4)
            
    elif choice == "2":
        amount = float(input("Quel montant souhaitez-vous retirer? \n"))
        if (balance - amount) < (authorized_overdraft):
            account.__withdraw_with_depassed_overdraft__(amount)
            time.sleep(4)
        else:
            account.__withdraw__(amount)
            time.sleep(4)
              
    elif choice == "3":
        account_choice = input("Quel compte souhaitez-vous consulter? \n 1: Compte courant. \n 2: Compte épargne. \n Quitter.\n")
        while True:
            if account_choice == "1":
                account.__consult_current__()
                time.sleep(8)
                break
            elif account_choice == "2":
                account.__consult_saving__()
                time.sleep(8)
                break
            elif account_choice == "3":
                print ("A bientôt chez P'tit LuCrative!")
                time.sleep(4)
       
    if choice == "4":
        transfer_type = input("1: Compte courant vers compte épargne. \n 2: Epargne vers compte courant. \n")
        # Code pour effectuer le virement ici
        print("Virement effectué avec succès!")
        time.sleep(8)
        
    
    if choice == "5":
        print("A bientôt chez P'tit LuCrative!")
        time.sleep(2)  
        break
        
    else:
        print("ERREUR: Veuillez choisir l'une des propositions: \n 1: pour un dépôt. \n 2: pour un retrait. \n 3: pour consulter vos comptes. \n 4: pour effectuer un virement. \n 5: pour quitter.")
