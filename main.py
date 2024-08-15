from menu.menu import Menu
from classes.utilisateur import Utilisateur


class Etab:
    def main():
        print('****************************************************************************** \n')
        print('BIENVENU DANS L\'application ETAB v1.2 \n')
        print('****************************************************************************** \n')
        print('CONNEXION \n')
        identifiant = input("Saisissez votre identifiant :")
        motDePasse = input("Saisissez votre mot de passe : ")


        if Utilisateur.authentification(identifiant,motDePasse):
            Menu.affichage_principal()

if __name__ == "__main__":
    Etab.main()


 