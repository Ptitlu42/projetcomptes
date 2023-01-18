class Account:
    def __init__(self, balance: int, owner: str, agios: int): # Définition de Account
        self.balance = balance # Solde
        self.owner = owner # Propriétaire


class Current_account: # Definition du compte courant avec l'héritage de Account
    def __init__(Account, balance: int, owner: str, agios: int, authorized_overdraft, amount): # Initialisation des éléments liés au compte courant   
        Account.authorized_overdraft = authorized_overdraft # Découvert autorisé
        Account.amount = amount # Montant de la transaction
        Account.balance = balance
    
    def __payment__(self, amount): # Gère les versements sur le compte
        self.balance += amount
        print ("Versement de {}$ effectué. \n Solde actuel: {}$".\
            format(amount, self.balance))
            
    def __withdraw__(Account, amount): # Gère les retraits sur le compte 
        balance = balance - amount
        print ("Retrait de {} effectué. \n Solde actuel: {}") .\
            format (amount, balance)
            
    def __withdraw_with_depassed_overdraft__ (Account, amount): # Gère les retrait si le solde dépasse le découvert autorisé après le retrait      
          balance = Account.balance
          agios = Account.agios
          value_agios = amount * (agios / 100) # Calcule le montant de taxe agios qui va être prelever en plus du retrait
          balance = balance - amount - value_agios # Calcule le sole après le retrait et après les agios
          print ("Vous avez effectuer un retrait de {}. Des agios d'une valeur de {} ({}%) ont été appliqués. \n Solde actuel: {}.") .\
              format(amount, value_agios, agios, balance)
          
          
    def __consult__(Account, balance, authorized_overdraft, owner): #Gère la partit pour consulter le compte
        balance = Account.balance
        authorized_overdraft = Account.authorized_overdraft
        owner = Account.owner
        print ("Voici les informations concernant votre compte commun: \n Propriétaire: {}. \n Solde: {}$. \n Découvert authorisé: {}.") .\
            format(owner, balance, authorized_overdraft)
            
        
        
        
        
    
    
    
            
