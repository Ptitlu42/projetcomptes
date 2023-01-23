import time
from objects import *
# from tkinter import messagebox
# from tkinter import IntVar
# from tkinter import StringVar
# from tkinter import *


balance = 1000
owner = "Erwann DuCloture-TonCompte"
agios = 5
authorized_overdraft = -200
amount = ()
interest = 1
saving_balance = 4000
saving_interest = 2

account = Account(balance, owner, agios,interest, authorized_overdraft,amount, saving_balance, saving_interest)

#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
#----------------------------------------------------------------------------#
# def debug(event):
#     print("click")
#     #----#TKINTER----#
# fenetre = Tk()
# fenetre_retrait = Toplevel()
# fenetre_depot = Toplevel()
# fenetre_consult = Toplevel()
# fenetre_virement = Toplevel()
# bitcoin_back = PhotoImage(file="background.png")
# bitcoin_second = PhotoImage(file="background2.png")
# fenetre.bind_class("<Button-1>",debug)

# #----------------------------------------------------------------------------#
#     #Tkinter fonctions
# def erreur_mauvaise_valeur():     
#     messagebox.showinfo("ERREUR", "Veuillez entrer un nombre positif entier.")
            
# def quit_page():
#     messagebox.showinfo("Bisous","Bisous bisous")
#     fenetre.destroy()
    
# def show_virement():
#     fenetre_virement.deiconify()
    
# def quit_virement():
#     fenetre_virement.withdraw()
    
# def quit_consult():
#     fenetre_consult.withdraw()
    
# def show_consult():
#     fenetre_consult.deiconify()
    
# def quit_retrait():
#     fenetre_retrait.withdraw()
    
# def show_retrait():
#     fenetre_retrait.deiconify()
    
# def quit_depot():
#     fenetre_depot.withdraw()
    
# def show_depot():
#     fenetre_depot.deiconify()
       
# def observer():
#     tk_balance.set(tk_amount_entry.get())
    
# def update_balance(new_balance):
#     welcome.itemconfig(text_id, text="Solde compte courant: {} BTC".format(new_balance))
    
# def refresh():
#     pass
    
     
    
     
     
     
    
# #----------------------------------------------------------------------------#
#     #Tkinter variables
# tk_balance = IntVar(value=balance)
# tk_owner = StringVar(value=owner)
# tk_agios = IntVar(value=agios)
# tk_authorized_overdraft = IntVar(value=authorized_overdraft)
# tk_amount = IntVar(value=amount)
# tk_interest = IntVar(value=interest)
# tk_saving_balance = IntVar(value=saving_balance)
# tk_saving_interest = IntVar(value=saving_interest)
# tk_amount_entry = IntVar(value=amount)
#     #Tkinter variables tracées
# tk_amount_entry.trace("w", observer)

# #----------------------------------------------------------------------------#
#     #Fenetre principale 
# fenetre.geometry("700x420+450+100")
# fenetre.title("P'tit LuCrative's BANK")
# fenetre["bg"] = "#00000a"
# fenetre.resizable(height=False, width=False)
# fenetre.iconbitmap("bitcoin.ico")
# mon_menu = Menu(fenetre)
# button_frame = Frame(fenetre, bg="#303030", width=100, height=100, borderwidth=4)
# welcome = Canvas(fenetre, height=400, width=700)
# welcome.create_image(0, 0, image=bitcoin_back, anchor=NW)
# welcome.create_text( 340, 30, text = "Bienvenue à la P'tit LuCrative's BANK!", font="ArialBlack, 16", fill="#FFD700")
# welcome.pack(expand=YES, fill=BOTH)
# button_frame.pack()

# #----------------------------#
#     #Fenetre retrait
# fenetre_retrait.geometry("350x210+625+220")
# fenetre_retrait.title("RETRAIT")
# fenetre_retrait["bg"] = "#00000a"
# fenetre_retrait.resizable(height=False, width=False)
# fenetre_retrait.iconbitmap("bitcoin.ico")
# retrait = Canvas(fenetre_retrait, height=350, width=210)
# retrait.create_image(0, 0, image=bitcoin_second, anchor=NW)
# retrait.create_text(170, 25, text="Retrait", font="ArialBlack, 16", fill="#FFD700")
# retrait.pack(expand=YES, fill=BOTH)
# fenetre_retrait.withdraw()

# #----------------------------#

#     #Fenetre virement
# fenetre_depot.geometry("350x210+625+220")
# fenetre_depot.title("VIREMENT")
# fenetre_depot["bg"] = "#00000a"
# fenetre_depot.resizable(height=False, width=False)
# fenetre_depot.iconbitmap("bitcoin.ico")
# depot = Canvas(fenetre_depot, height=350, width=210)
# depot.create_image(0, 0, image=bitcoin_second, anchor=NW)
# depot.create_text(170, 25, text="Virement", font="ArialBlack, 16", fill="#FFD700")
# depot.pack(expand=YES, fill=BOTH)
# fenetre_depot.withdraw()

# #----------------------------#
#     #Fenetre consult
# fenetre_consult.geometry("350x210+625+220")
# fenetre_consult.title("COMPTES")
# fenetre_consult["bg"] = "#00000a"
# fenetre_consult.resizable(height=False, width=False)
# fenetre_consult.iconbitmap("bitcoin.ico")
# consult = Canvas(fenetre_consult, height=350, width=210)
# consult.create_image(0, 0, image=bitcoin_second, anchor=NW)
# consult.create_text(170, 25, text="Comptes:", font="ArialBlack, 16", fill="#FFD700")
# consult.pack(expand=YES, fill=BOTH)
# fenetre_consult.withdraw()

# #----------------------------#
#     #Fenetre Virement
# fenetre_virement.geometry("700x420+450+100")
# fenetre_consult.title("Virement")
# fenetre_consult["bg"] = "#00000a"
# fenetre_consult.resizable(height=False, width=False)
# fenetre.iconbitmap("bitcoin.ico")
# virement = Canvas(fenetre_consult, height=700, width=420)
# virement.create_image(0, 0, image=bitcoin_back, anchor=NW)
# virement.create_text(170, 25, text="Virement:", font="ArialBlack, 16", fill="#FFD700")
# virement.pack(expand=YES, fill=BOTH)
# fenetre_virement.withdraw()


# #----------------------------------------------------------------------------#
# #Boutons fenetre principale
#     #Bouton raffraichir
# button_refresh = Button(text="Rafraichir", height=1, width=8, bg="#FFD700", activebackground="#c2c78b", command=refresh)
# welcome.create_window(316, 280, anchor="nw", window=button_refresh)
#     #Bouton retrait 
# button_retrait = Button(text="Retirer des BTC", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=show_retrait)
# welcome.create_window(25, 110, anchor="nw", window=button_retrait)
#     #Bouton versement 
# buttun_versement = Button(text="Déposer des BTC", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=show_depot)
# welcome.create_window(25, 240, anchor="nw", window=buttun_versement)
#     #Bouton consult 
# button_consult = Button(text="Consulter mes comptes.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=show_consult)
# welcome.create_window(520, 110, anchor="nw", window=button_consult)
#     #Bouton virement 
# button_virement = Button(text="Transferer des BTC", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=show_virement)
# welcome.create_window(520, 240, anchor="nw", window=button_virement)
#     #Bouton quitter 
# button_quitter = Button(text="Quitter.", height=3, width=20, bg="#FFD700", activebackground="#c2c78b", command=quit_page)
# welcome.create_window(275, 315, anchor="nw", window=button_quitter)
#     #Affichage de owner
# welcome.create_text(350, 50, text="{}".format(owner), fill="#FFD700", font=("Arial", 12, "italic"))
#     #Affichage du solde current
# text_id = welcome.create_text(350, 90, text="Solde compte courant: {} BTC".format(balance), fill="#FFD700", font=("Arial", 12, "bold"))
#     #Affichage du solde saving
# welcome.create_text(350, 110, text="Solde compte épargne: {} BTC".format(saving_balance), fill="#FFD700", font=("Arial", 12, "bold"))

# #----------------------------------------------------------------------------#
#     #Onglet fichier 
# fichier = Menu(fenetre, mon_menu, tearoff=0)
# fichier.add_command(label="Enregistrer sous..")
#     #Onglet options
# options = Menu(fenetre, mon_menu, tearoff=0)
# options.add_command(label="Affichage")

# #----------------------------------------------------------------------------#

#     #Widgets fenetre retrait
    
# def entry_value():
#         value = entry.get()
#         value=int(value)
#         Current_account.withdraw(account, value)
#         #Entré user
# frame_entry = Frame(fenetre_retrait)
# entry = Entry(frame_entry, width = 20)
# entry.pack()
# retrait.create_window(112, 65, anchor="nw", window=frame_entry,tags='frame_entry')
# retrait.lift('frame_entry')
#         #Bouton valider
# frame_retrait2 = Frame(fenetre_retrait)
# button_retrait2 = Button(frame_retrait2, text="Valider", height=3, width=20, bg="#FFD700", activebackground="#c2c78b",command= entry_value)
# button_retrait2.pack()
# retrait.create_window(100, 100, anchor="nw", window=frame_retrait2,tags='frame_retrait2')
# retrait.lift('frame_retrait2')
 
#         #Bouton annuler
# frame_exit = Frame(fenetre_retrait)
# exit_button = Button(frame_exit, text="Annuler", height=1, width=6, bg="#FFD700", activebackground="#c2c78b", command=quit_retrait)
# exit_button.pack()
# retrait.create_window(150, 170, anchor="nw", window=frame_exit, tags='frame_exit')
# retrait.lift('frame_exit')

# #----------------------------#

# #Widgets fenetre versement
#         #Bouton valider
# frame_depot2 = Frame(fenetre_depot)
# button_depot2 = Button(frame_depot2, text="Valider", height=3, width=20, bg="#FFD700", activebackground="#c2c78b")
# button_depot2.pack()
# depot.create_window(100, 100, anchor="nw", window=frame_depot2,tags='frame_depot2')
# depot.lift('frame_depot2')
#         #Entré user
# frame_entry2 = Frame(fenetre_depot)
# entry2 = Entry(frame_entry2, width = 20)
# entry2.pack()
# depot.create_window(112, 65, anchor="nw", window=frame_entry2,tags='frame_entry2')
# depot.lift('frame_entry2')
#         #Bouton annuler
# frame_exit2 = Frame(fenetre_depot)
# exit_button2 = Button(frame_exit2, text="Annuler", height=1, width=6, bg="#FFD700", activebackground="#c2c78b", command=quit_depot)
# exit_button2.pack()
# depot.create_window(150, 170, anchor="nw", window=frame_exit2, tags='frame_exit2')
# depot.lift('frame_exit2')

# #----------------------------#
# #Widgets fenetre consult
# frame_consult2 = Frame(fenetre_consult)
# consult.create_text(170, 50, text="{}".format(owner), font=("ArialBlack", 10), fill="#FFD700")
#     #Affichage courant
# consult.create_text(80, 80, text="--Compte courant--", font =("ArialBlack", 10, "bold"), fill="#FFD700")
# consult.create_text(80,100, text="Solde: {} BTC".format(balance), font=("ArialBlack", 10), fill="#FFD700")
# consult.create_text(80,115, text="Agios: {}%".format(agios), font=("ArialBlack", 10), fill="#FFD700")
# consult.create_text(80,130, text="Intérets: {}%".format(interest), font=("ArialBlack", 10), fill="#FFD700")
# consult.create_text(80, 145, text="Découvert: {} BTC".format(authorized_overdraft), font=("ArialBlack", 10), fill="#FFD700")
#     #Affichage épargne
# consult.create_text(270, 80, text="--Compte épargne--", font =("ArialBlack", 10, "bold"), fill="#FFD700")
# consult.create_text(270,100, text="Solde: {} BTC".format(saving_balance), font=("ArialBlack", 10), fill="#FFD700")
# consult.create_text(270,115, text="Intérets: {}%".format(saving_interest), font=("ArialBlack", 10), fill="#FFD700")
#     #Affichage retour button 
# frame_exit = Frame(fenetre_consult)
# exit_button = Button(frame_exit, text="Retour", height=1, width=6, bg="#FFD700", activebackground="#c2c78b", command=quit_consult)
# exit_button.pack()
# consult.create_window(150, 170, anchor="nw", window=frame_exit, tags='frame_exit')
# consult.lift('frame_exit')
    
#----------------------------#
# #Widgets fenetre virement
#     #Boutons valider
# frame_virement2 = Frame(fenetre_virement)
# button_virement2 = Button(frame_retrait2, text="Valider", height=1, width=10, font="#FFD700", activebackground="#c2c78b")
# button_virement3= Button(frame_retrait2, text="Valider", height=1, width=10, font="#FFD700", activebackground="#c2c78b")
# button_virement2.pack
# button_virement3.pack
#     #Entrées user
# frame_entry2= Frame(fenetre_virement)
# entry2 = Entry(frame_entry2, width=20)
# entry3 = Entry(frame_entry2, width=20)
# entry2.pack()
# entry3.pack()
# virement.create_window(112, 65, anchor="nw", window=frame_entry2, tags='frame_entry2')
# virement.lift('frame_entry')
#     #Bouton annuler
# frame_exit3 = Frame(fenetre_virement)
# exit_button3 = Button(frame_exit3, text="Annuler", height=1, width=6, bg="#FFD700", activebackground="#c2c78b", command=quit_virement)
# exit_button3.pack()
# virement.create_window(150, 170, anchor="nw", window=frame_exit3, tags='frame_exit3')
# virement.lift('frame_exit3')








#----------------------------------------------------------------------------#

#     #Onglets 
# mon_menu.add_cascade(label="Fichier", menu=fichier)
# mon_menu.add_cascade(label="Options", menu=options)
# fenetre.config(menu=mon_menu)

#----------------------------------------------------------------------------#

# fenetre.mainloop()



#----------------------------------------------------------------------------#

print("Bienvenue dans la P'tit LuCrative")

while True:
    choice = input("Que souhaitez-vous faire? \n 1: Un retrait. \n 2: Un dépot. \n 3: Consulter mes comptes. \n 4: Effectuer un virement. \n 5: Quitter. \n")
    
    if choice == "1": 
        Current_account.withdraw(account, amount)
    
    if choice == "2": 
        Current_account.payment(account, amount)
        
    if choice == "3": 
        account_choice = input("Quel compte souhaitez vous consulter ? \n 1: Compte courant. \n 2: Compte épargne. \n")
        if account_choice == "1": 
            Current_account.consult_current(account)
        if account_choice == "2": 
            Saving_account.consult_saving(account)
        
    if choice == "4": 
        account_choice = input("Que type de virement souhaitez-vous effectuer ? \n 1: Compte courant --> compte épargne. \n 2: Compte épargne --> compte courant. \n")
        if account_choice =="1": 
            Current_account.transfer_to_saving(account, amount)
        if account_choice =="2": 
            Saving_account.transfer_to_current(account, amount)
            
    if choice == "5":
        print ("A bientôt chez P'tit LuCrative!")
        time.sleep(2)
        break
           
        
              
    