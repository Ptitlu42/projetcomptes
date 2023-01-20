import time
from objects import *

balance = 1000
owner = "Erwann DuCloture-TonCompte"
agios = 10
authorized_overdraft = -200
amount = ()
interest = 5
saving_balance = 4000
saving_interest = 10

account = Account(balance, owner, agios,interest, authorized_overdraft,amount, saving_balance, saving_interest)

print("Bienvenue dans la P'tit LuCrative")

while True:
    choice = input("Que souhaitez-vous faire? \n 1: Un retrait. \n 2: Un dépot. \n 3: Consulter mes comptes. \n 4: Effectuer un virement. \n 5: Quitter. \n")
    
    if choice == "1": #ok
        Current_account.withdraw(account, amount)
    
    if choice == "2": #ok
        Current_account.payment(account, amount)
        
    if choice == "3": #ok
        account_choice = input("Quel compte souhaitez vous consulter ? \n 1: Compte courant. \n 2: Compte épargne. \n")
        if account_choice == "1": #ok
            Current_account.consult_current(account)
        if account_choice == "2": #ok
            Saving_account.consult_saving(account)
            
    if choice == "4": #pasok
        account_choice = input("Que type de virement souhaitez-vous effectuer ? \n 1: Compte courant --> compte épargne. \n 2: Compte épargne --> compte courant. \n")
        if account_choice =="1": #pasok
            Current_account.transfer_to_saving(account, amount)
        if account_choice =="2": #pasok
            Saving_account.transfer_to_current(account, amount)
           
        
              
    
