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
fenetre_retrait = Toplevel()
bitcoin_back = PhotoImage(file="background.png")
bitcoin_second = PhotoImage(file="background2.png")
    #Tkinter fonctions
def erreur_mauvaise_valeur():     
    messagebox.showinfo("ERREUR", "Veuillez entrer un nombre positif entier.")
            
def quit_page():
    messagebox.showinfo("Bisous","Merci d'avoir choisis la P'tit LuCrative's BANK, à bientôt!")
    fenetre.destroy()
    
def quit_window():
    fenetre_retrait.withdraw()
    
def show_retrait():
    fenetre_retrait.deiconify()
    
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
fenetre.geometry("700x420+450+100")
fenetre.title("P'tit LuCrative's BANK")
fenetre["bg"] = "#00000a"
fenetre.resizable(height=False, width=False)
fenetre.iconbitmap("bitcoin.ico")
mon_menu = Menu(fenetre)
button_frame = Frame(fenetre, bg="#303030", width=100, height=100, borderwidth=4)
welcome = Canvas(fenetre, height=400, width=700)
welcome.create_image(0, 0, image=bitcoin_back, anchor=NW)
welcome.create_text( 340, 30, text = "Bienvenue à la P'tit LuCrative's BANK!", font="ArialBlack, 16", fill="#FFD700")
welcome.pack(expand=YES, fill=BOTH)
button_frame.pack()
    #Fenetre retrait
fenetre_retrait.geometry("350x210+625+220")
fenetre_retrait.title("P'tit LuCrative's BANK")
fenetre_retrait["bg"] = "#00000a"
fenetre_retrait.resizable(height=False, width=False)
fenetre_retrait.iconbitmap("bitcoin.ico")
retrait = Canvas(fenetre_retrait, height=350, width=210)
retrait.create_image(0, 0, image=bitcoin_second, anchor=NW)
retrait.create_text(170, 25, text="Retrait", font="ArialBlack, 16", fill="#FFD700")
retrait.pack(expand=YES, fill=BOTH)
fenetre_retrait.withdraw()
    #Bouton retrait 
button_retrait = Button(text="Effectuer un retrait.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=show_retrait)
welcome.create_window(25, 110, anchor="nw", window=button_retrait)
    #Bouton versement 
buttun_versement = Button(text="Effectuer un versement.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b")
welcome.create_window(25, 240, anchor="nw", window=buttun_versement)
    #Bouton consult 
button_consult = Button(text="Consulter mes comptes.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b")
welcome.create_window(520, 110, anchor="nw", window=button_consult)
    #Bouton virement 
button_virement = Button(text="Effectuer un virement.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b")
welcome.create_window(520, 240, anchor="nw", window=button_virement)
    #Bouton quitter 
button_quitter = Button(text="Quitter.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=quit_page)
welcome.create_window(275, 315, anchor="nw", window=button_quitter)
    #Affichage de owner
welcome.create_text(350, 50, text="{}".format(owner), fill="#FFD700", font=("Arial", 12, "italic"))
    #Affichage du solde current
#tk_affiche_current = Label(fenetre, text="Solde compte courant: {}BTC".format(tk_balance), bg="#303030", font="Arial, 12", foreground="#F0C300")
welcome.create_text(350, 90, text="Solde compte courant: {} BTC".format(balance), fill="#FFD700", font=("Arial", 12, "bold"))
    #Affichage du solde saving
welcome.create_text(350, 110, text="Solde compte épargne: {} BTC".format(saving_balance), fill="#FFD700", font=("Arial", 12, "bold"))
    #Onglet fichier 
fichier = Menu(fenetre, mon_menu, tearoff=0)
fichier.add_command(label="Enregistrer sous..")
    #Onglet options
options = Menu(fenetre, mon_menu, tearoff=0)
options.add_command(label="Affichage")
    #Widgets fenetre retrait
        #Bouton valider
frame_retrait2 = Frame(fenetre_retrait)
button_retrait2 = Button(frame_retrait2, text="Valider", height=3, width=20, bg="#FFD700", activebackground="#c2c78b")
button_retrait2.pack()
retrait.create_window(100, 100, anchor="nw", window=frame_retrait2,tags='frame_retrait2')
retrait.lift('frame_retrait2')
        #Entré user
frame_entry = Frame(fenetre_retrait)
entry = Entry(frame_entry, width = 20)
entry.pack()
retrait.create_window(112, 65, anchor="nw", window=frame_entry,tags='frame_entry')
retrait.lift('frame_entry')
        #Bouton annuler
frame_exit = Frame(fenetre_retrait)
exit_button = Button(frame_exit, text="Annuler", height=1, width=6, bg="#FFD700", activebackground="#c2c78b", command=quit_window)
exit_button.pack()
retrait.create_window(150, 170, anchor="nw", window=frame_exit, tags='frame_exit')
retrait.lift('frame_exit')




    #Onglets 
mon_menu.add_cascade(label="Fichier", menu=fichier)
mon_menu.add_cascade(label="Options", menu=options)
fenetre.config(menu=mon_menu)

fenetre.mainloop()


#----------------------------------------------------------------------------#

#print("Bienvenue dans la P'tit LuCrative")

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
           
        
              
    
