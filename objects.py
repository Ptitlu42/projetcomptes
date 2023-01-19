class Account:
    def __init__(self, balance: float, owner: str, agios: float, interest: int): # Définition de Account
        self.balance = balance # Solde
        self.owner = owner
        self.interest = interest
        self.agios = agios# Propriétaire
        
    


class Current_account: # Definition du compte courant avec l'héritage de Account
    def __init__(Account, balance: float, owner: str, agios: float, authorized_overdraft, amount): # Initialisation des éléments liés au compte courant   
        Account.authorized_overdraft = authorized_overdraft # Découvert autorisé
        Account.amount = amount # Montant de la transaction
        Account.balance = balance
        Account.owner = owner
        Account.agios = agios
        
    def __payment__(self, amount): # Gère les versements entre les comptes
            self.balance += amount
            print ("Versement de {}$ effectué. \n Solde actuel: {}$".\
                format(amount, self.balance))
             
    def __withdraw__(self, amount): # Gère les retraits sur le compte       
        self.balance = self.balance - amount
        print ("Retrait de {}$ effectué. \n Solde actuel: {}$" .\
            format (amount, self.balance))
            
    def __withdraw_with_depassed_overdraft__ (self, amount): # Gère les retrait si le solde dépasse le découvert autorisé après le retrait      
          self.agios = self.agios
          value_agios = amount * (self.agios / 100) # Calcule le montant de taxe agios qui va être prelever en plus du retrait
          self.balance = self.balance - amount - value_agios # Calcule le sole après le retrait et après les agios
          print ("Vous avez effectuer un retrait de {}$. Des agios d'une valeur de {} ({}%) ont été appliqués. \n Solde actuel: {}$." .\
              format(amount, value_agios, self.agios, self.balance))
          
          
    def __consult_current__(self): #Gère la partit pour consulter le compte
        self.balance = self.balance
        self.authorized_overdraft = self.authorized_overdraft
        self.owner = self.owner
        print ("Voici les informations concernant votre compte commun: \n Propriétaire: {}. \n Solde: {}$. \n Découvert authorisé: {}$." .\
            format(self.owner, self.balance, self.authorized_overdraft)) 
        
class Saving_account: # Definition du compte courant avec l'héritage de Account
    def __init__(Account, balance: float, owner: str, agios: float, amount, interest: int): # Initialisation des éléments liés au compte courant   
        Account.amount = amount # Montant de la transaction
        Account.balance = balance
        Account.owner = owner
        Account.agios = agios
        
    def __consult_saving__(self):
        self.interest = self.interest#Gère la partit pour consulter le compte
        self.balance = self.balance
        self.owner = self.owner
        print ("Voici les informations concernant votre compte épargne: \n Propriétaire: {}. \n Taux d'intéret: {}%. \n Solde: {}$." .\
            format(self.owner, self.balance,)) 
