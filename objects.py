# Gère le compte courant et les action liées à celui-ci
class Current_account:
    
    # Initialisation des éléments lié au compte courant
    def __init__(self, actual_value: int, authorized_overdraft: int, transaction: int):   
        self.actual_value = actual_value
        self.authorized_overdraft = authorized_overdraft
        self.transaction = transaction
    
    # Gère les ajouts sur le compte
    def __add__(self, value_to_add: int):
        pass
    
    # Gère les retraits sur le compte
    def __sub__(self, value_to_sub: int):
        pass
    
    # Gère les agios si le solde est en dessous du découvert après un retrait
    def __more_than_authorized__(self, penalty_value: int):
        pass
    
    def __str__(self, transaction, actual_value) -> str:
        return "Vous avez effecter l'opération {}. \n Voici le solde de votre compte: {}." .\
            format (transaction, actual_value)
        
        
            