import time
from objects import *
from tkinter import messagebox
from tkinter import IntVar
from tkinter import StringVar
from tkinter import *

balance = 1000
owner = "Erwann DuCloture-TonCompte"
agios = 5
authorized_overdraft = -200
amount = ()
interest = 1
saving_balance = 4000
saving_interest = 1

account = Account(balance, owner, agios,interest, authorized_overdraft,amount, saving_balance, saving_interest)

#----------------------------------------------------------------------------#
    #Tkinter
fenetre = Tk()
bitcoin_back = PhotoImage(file="background.png")


    #Tkinter fonctions
def erreur_mauvaise_valeur():     
    messagebox.showinfo("ERREUR", "Veuillez entrer un nombre positif entier.")
            
def quit_page():
    messagebox.showinfo("Bisous","Merci d'avoir choisis la P'tit LuCrative's BANK, à bientôt!")
    fenetre.destroy()
    
def observer():
    tk_amount.set(tk_amount_entry.get())
        
    #Tkinter variables
tk_balance = IntVar(value=balance)
tk_owner = StringVar(value=owner)
tk_agios = IntVar(value=agios)
tk_authorized_overdraft = IntVar(value=authorized_overdraft)
tk_amount = IntVar(value=amount)
tk_interest = IntVar(value=interest)
tk_saving_balance = IntVar(value=saving_balance)
tk_saving_interest = IntVar(value=saving_interest)
tk_amount_entry = IntVar(value=amount)
    #Tkinter variables tracées
tk_amount_entry.trace("w", observer)

    #Fenetre principale 
fenetre.geometry("700x400+575+100")
fenetre.title("P'tit LuCrative's BANK")
fenetre["bg"] = "#303030"
fenetre.resizable(height=False, width=False)
fenetre.iconbitmap("bitcoin.ico")
mon_menu = Menu(fenetre)
button_frame = Frame(fenetre, bg="#303030", width=100, height=100, borderwidth=4)



    #Affichage fenetre principale 
welcome = Label(fenetre, text="Bienvenue à la P'tit LuCrative's BANK!", bg="#303030", font="Arial, 19", image=bitcoin_back)
welcome.pack()
button_frame.pack()
    #Bouton retrait 
button_retrait = Button(button_frame,text="Effectuer un retrait.", height=5, width=40, bg="#FFE436", activebackground="#F7FF3C", anchor="nw")
button_retrait.pack()
    #Bouton versement 
buttun_versement = Button(button_frame, text="Effectuer un versement.", height=5, width=40, bg="#FFE436")
buttun_versement.pack()
    #Bouton consult 
button_consult = Button(button_frame,text="Consulter mes comptes.", height=5, width=40, bg="#FFE436")
button_consult.pack()
    #Bouton virement 
button_virement = Button(button_frame,text="Effectuer un virement.", height=5, width=40, bg="#FFE436")
button_virement.pack()
    #Bouton quitter 
button_quitter = Button(button_frame,text="Quitter.", height=5, width=40, bg="#FFE436", command=quit_page)
button_quitter.pack()
    #Affichage de owner
tk_affiche_owner = Label(fenetre, textvariable=tk_owner, bg="#303030", font="Arial, 12", foreground="#F0C300")
tk_affiche_owner.pack()
    #Affichage du solde current
tk_affiche_current = Label(fenetre, text="Solde compte courant:", bg="#303030", font="Arial, 12", foreground="#F0C300")
tk_affiche_current.pack()
tk_current = Label(fenetre, textvariable=tk_balance, bg="#303030", font="Arial, 12", foreground="#F0C300")
tk_current.pack()
    #Affichage du solde saving
tk_affiche_saving = Label(fenetre, text="Solde compte épargne:", bg="#303030", font="Arial, 12", foreground="#F0C300")
tk_affiche_saving.pack()
tk_saving = Label(fenetre, textvariable=tk_saving_balance, bg="#303030", font="Arial, 12", foreground="#F0C300")
tk_saving.pack()    
    #Onglet fichier 
fichier = Menu(fenetre, mon_menu, tearoff=0)
fichier.add_command(label="Enregistrer sous..")
    #Onglet options
options = Menu(fenetre, mon_menu, tearoff=0)
options.add_command(label="Affichage")

    #Onglets 
mon_menu.add_cascade(label="Fichier", menu=fichier)
mon_menu.add_cascade(label="Options", menu=options)
fenetre.config(menu=mon_menu)

fenetre.mainloop()

#----------------------------------------------------------------------------#

print("Bienvenue dans la P'tit LuCrative")

# while True:
#     choice = input("Que souhaitez-vous faire? \n 1: Un retrait. \n 2: Un dépot. \n 3: Consulter mes comptes. \n 4: Effectuer un virement. \n 5: Quitter. \n")
    
#     if choice == "1": 
#         Current_account.withdraw(account, amount)
    
#     if choice == "2": 
#         Current_account.payment(account, amount)
        
#     if choice == "3": 
#         account_choice = input("Quel compte souhaitez vous consulter ? \n 1: Compte courant. \n 2: Compte épargne. \n")
#         if account_choice == "1": 
#             Current_account.consult_current(account)
#         if account_choice == "2": 
#             Saving_account.consult_saving(account)
        
#     if choice == "4": 
#         account_choice = input("Que type de virement souhaitez-vous effectuer ? \n 1: Compte courant --> compte épargne. \n 2: Compte épargne --> compte courant. \n")
#         if account_choice =="1": 
#             Current_account.transfer_to_saving(account, amount)
#         if account_choice =="2": 
#             Saving_account.transfer_to_current(account, amount)
            
#     if choice == "5":
#         print ("A bientôt chez P'tit LuCrative!")
#         time.sleep(2)
#         break
           
        
              
    
