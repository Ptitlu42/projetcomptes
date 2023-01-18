# Projet de fin de module: programme comptes bancaires

Sujet
Ecrire un programme qui implémente en POO un fonctionnement bancaire basique :


une classe abstraite Compte


attributs : numero_compte, nom_proprietaire, solde

méthodes : retrait, versement, afficher_solde



une classe fille CompteCourant, qui ajoute une gestion du découvert (montant maximum négatif
possible) et des agios (pénalité de X % si le solde est inférieur à zéro) :


attributs : autorisation_decouvert, pourcentage_agios

méthodes : appliquer_agios



une classe fille CompteEpargne, qui ajoute :


attributs : pourcentage_interets

méthodes : appliquer_interets
