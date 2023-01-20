import time


class Account:
    def __init__(self, balance: int ,owner: str ,agios: int ,interest: int, authorized_overdraft: int, amount: int, saving_balance: int, saving_interest: int):
        self.balance = balance
        self.owner = owner
        self.agios = agios
        self.interest = interest
        self.authorized_overdraft = authorized_overdraft
        self.amount = amount
        self.saving_balance = saving_balance
        self.saving_interest = saving_interest
                
class Current_account(Account): 
    def __init__(self, balance, owner, agios, interest, authorized_overdraft, amount, saving_balance):
        super.__init__(self, balance, owner, agios, interest, authorized_overdraft, amount, saving_balance)
        
    def withdraw(self, amount):
        amount = int(input("Quel montant voulez-vous retirer? \n")) 
               
        if (self.balance - amount) <= self.authorized_overdraft:
            print("Découvert autorisé dépassé. \n Solde:{}$." .\
                format (self.balance))
            time.sleep(4)
        
        else:
            self.balance = (self.balance - amount)
            print ("Vous avez effectuer un retrait de {}$.\n Solde actuel: {}$." .\
                format (amount, self.balance))
            time.sleep(4)
                                        
        if (self.balance - amount) < 0 and (self.balance - amount) > self.authorized_overdraft:
            value_agios = amount * (self.agios / 100)
            self.balance = self.balance - amount - value_agios
            print ("Vous avez effectuer un retrait de {}$. Des agios d'une valeur de {} ({}%) ont été appliqués. \n Solde actuel: {}$." .\
              format(amount, value_agios, self.agios, self.balance))
            time.sleep(4)
                        
    def payment(self, amount):
        amount = int(input("Quel montant souhaitez vous déposer ? \n"))
        interest_value = amount * (self.interest / 100)
        self.balance = self.balance + amount + interest_value
        print ("Vous avez effectuer un depot de {}$. \n Vos interets: {}$ ({}%). \n Solde actuel: {}$." .\
            format (amount, interest_value, self.interest, self.balance))
        time.sleep(4)
            
    def consult_current(self):
        print ("Voici les informations concernant votre compte commun: \n \n Propriétaire: {}. \n Solde: {}$. \n Découvert autorisé: {}$. \n Intérêts: {}%." .\
            format(self.owner, self.balance, self.authorized_overdraft, self.interest))
        time.sleep(4)  
        
    def transfer_to_saving(self, amount):
        amount = int(input("Quel motant souhaitez vous versé sur votre compte épargne ? \n"))
        if self.balance - amount < self.authorized_overdraft:
            print ("Vous ne pouvez pas effectuer ce virement, votre compte courant dépasserai la limite autorisé. \n Solde compte courant: {}$. \n Solde compte épargne: {}$." .\
                format (self.balance, self.saving_balance))
            time.sleep(4)
        else:
            self.balance = self.balance - amount
            self.saving_balance = self.balance + amount
            print ("Votre virement a bien été pris en compte. \n Solde compte courant: {}$. \n Solde compte épargne: {}$." .\
                format (self.balance, self.saving_balance))
            time.sleep(4)
            
class Saving_account(Account):
    def __init__(self, balance, owner, agios, authorized_overdraft, interest, amount, saving_balance, saving_interest):
        super.__init__(self, balance, agios, owner, authorized_overdraft, interest, amount, saving_balance, saving_interest)
    
    def consult_saving(self):
        print ("Voici les informations concernant votre compte commun: \n \n Propriétaire: {}. \n Solde: {}$.\n Intérêts: {}%." .\
            format(self.owner, self.saving_balance, self.saving_interest))
        time.sleep(4) 
        
    def transfer_to_current(self, amount):
        amount = int(input("Quel motant souhaitez vous versé sur votre compte courant ? \n"))
        if self.saving_balance - amount < 0:
            print ("Vous ne pouvez pas effectuer ce virement, votre compte épargne dépasserai la limite autorisé. \n Solde compte courant: {}$. \n Solde compte épargne: {}$." .\
                format (self.balance, self.saving_balance))
            time.sleep(4)
        else:
            self.saving_balance = self.saving_balance - amount
            self.balance = self.balance + amount
            print ("Votre virement a bien été pris en compte. \n Solde compte courant: {}$. \n Solde compte épargne: {}$." .\
                format (self.balance, self.saving_balance))
            time.sleep(4)
    
        
