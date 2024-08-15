from classes.eleve import Eleve
from classes.utilisateur import Utilisateur
from classes.professeur import Professeur
import datetime


class Menu():
    def __init__(self) -> None:
        pass

    def affichage_principal():
        print('****************************************************************************** \n')
        print('BIENVENU DANS L\'application ETAB v1.2 \n')
        print('****************************************************************************** \n')
        liste_menu = [
            {1:"Gestion des eleves"},
            {2:"Gestion des professeur"},
            {3:"Gestion des utilisateurs"},
            {4:"Quitter \n"}
        ]

        for element in liste_menu:
            for keys , value in element.items():
                print(f'{keys} : {value}')

        
        ts = datetime.datetime.now()
        print('')
        print("Date systeme :", ts.hour ,"h" , ts.minute ,'min')
        print('')

        try:
            message = int (input('Veuillez saisir votre choix : '))
        except TypeError:
            print('Vous devez saisir un chiffre.')
            Menu.affichage_principal()
        else:
            Menu.choix_principal(message)

    def choix_principal(choix):
         choix = int(choix)
         match(choix):
            case 1 : 
                print('Nous sommes a cette etape.')
                Menu.sous_choix_eleve(Eleve.menu_eleve())
            case 2 :
                 Menu.sous_choix_professeur(Professeur.menu_professeur())
            case 3 :
                 Menu.sous_choix_utilisateur(Utilisateur.menu_utilisateur())
            case 4 : 
                 print('Nous sommes sur quitter')
                 quit()
            case _:
                 print('Choix non valide !')
                 Menu.affichage_principal()
                 

    def sous_choix_eleve(choix):
        choix = int(choix)
        match(choix):
            case 1 :
                print('Nous sommes dans le sous choix eleves !')
                Eleve.ajouter()
                Menu.sous_choix_eleve(Eleve.menu_eleve())
            case 2 : 
                Eleve.supprimer()
                Menu.sous_choix_eleve(Eleve.menu_eleve())
            case 3:
                Eleve.mettreAJour()
                Menu.sous_choix_eleve(Eleve.menu_eleve())
            case 4 :
                Eleve.obtenir()
                Menu.sous_choix_eleve(Eleve.menu_eleve())
            case 5 :
                Eleve.obtenirEleve()
                Menu.sous_choix_eleve(Eleve.menu_eleve())
            case 6 :
                Menu.affichage_principal()
            case 7:
                quit()
            case _:
                 print('Choix non valide !')
                 Menu.sous_choix_eleve(Eleve.menu_eleve())
    
    def sous_choix_professeur(choix):
        choix = int(choix)
        match(choix):
            case 1 :
                print('Nous sommes dans le sous choix professeur !')
                Professeur.ajouter()
                Menu.sous_choix_professeur(Professeur.menu_professeur())
            case 2 :
                Professeur.supprimer()
                Menu.sous_choix_professeur(Professeur.menu_professeur())
            case 3 :
                Professeur.mettreAJour()
                Menu.sous_choix_professeur(Professeur.menu_professeur())
            case 4 : 
                Professeur.obtenir()
                Menu.sous_choix_professeur(Professeur.menu_professeur())
            case 5 :
                Professeur.obtenirProfesseur()
                Menu.sous_choix_professeur(Professeur.menu_professeur())
            case 6 :
                Menu.affichage_principal()
            case 7:
                quit()
            case _:
                 print('Choix non valide !')
                 Menu.sous_choix_eleve(Eleve.menu_eleve())

    def sous_choix_utilisateur(choix):
        choix = int(choix)
        match(choix):
            case 0:
                pass
            case 1:
                Utilisateur.ajouter()
                Menu.sous_choix_utilisateur(Utilisateur.menu_utilisateur())
            case 2 :
                Utilisateur.supprimerCompte()
                Menu.sous_choix_utilisateur(Utilisateur.menu_utilisateur())
            case 3 :
                Utilisateur.modifierMotDePasse()
                Menu.sous_choix_utilisateur(Utilisateur.menu_utilisateur())
            case 4:
                Utilisateur.listerUtilisateur()
                Menu.sous_choix_utilisateur(Utilisateur.menu_utilisateur())
            case 5:
                Menu.affichage_principal()
            case _:
                 print('Choix non valide !')
                 Menu.sous_choix_eleve(Eleve.menu_eleve())