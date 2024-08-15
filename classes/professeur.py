from classes.personne import Personne
from interfaces.icrudprofesseur import ICRUDProfesseur
from interfaces.ieducation import IEducation
import mysql.connector
from mysql.connector import Error
import datetime

class Professeur(Personne, ICRUDProfesseur, IEducation):
    def __init__(self, id, dateNaissance, ville, prenom, nom , vacant, matiereEnseigne, prochainCours, sujetProchaineReunion) -> None:
        super().__init__(id, dateNaissance, ville, prenom, nom)
        self.__vacant = vacant
        self.__matiereEnseigne = matiereEnseigne
        self.__prochainCours = prochainCours
        self.__sujetProchaineReunion = sujetProchaineReunion

    def get_vacant(self):
        return self.__vacant
    def set_vacant(self, vacant):
        self.__vacant = vacant

    def get_matiereEnseigne(self):
        return self.__matiereEnseigne
    def set_matiereEnseigne(self, matiereEnseigne):
        self.__matiereEnseigne = matiereEnseigne

    def get_prochainCours(self):
        return self.__prochainCours
    def set_prochainCours(self, prochainCours):
        self.__prochainCours = prochainCours

    def get_sujetProchaineReunion(self):
        return self.__sujetProchaineReunion
    def set_sujetProchaineReunion(self, sujetProchaineReunion):
        self.__sujetProchaineReunion = sujetProchaineReunion
    
    def ajouter():
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',            # Nom d'hôte ou adresse IP
                database='etab_db',   # Nom de la base de données
                user='root',    # Nom d'utilisateur MySQL
                password='bibo1996' # Mot de passe MySQL
            )

            if connection.is_connected():
                try:
                    dateNaissance = str(input('Date de naissance : '))
                    ville = str(input('Saisir la ville : '))
                    nom = str(input('Saisir le nom du professeur: '))
                    prenom = str(input('Saisir le prenom du professeur : '))
                    vacant = str(input('Saisir la vacant : '))
                    matiereEnseigne = str(input('Saisir la matiere enseigné : '))
                    prochainCours = str(input('Saisir le prochain cour : '))
                    sujetProchaineReunion = str(input('Saisir le sujet de la prochaine reunion : '))
                except :
                    print('Insertion impossble')

                print("Connexion réussie à la base de données MySQL")
                cursor = connection.cursor()
                insert_query = """INSERT INTO professeur (dateNaissance, ville, prenom, nom, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion)
                                VALUES (%s, %s, %s , %s, %s, %s, %s, %s)"""

                data = (dateNaissance,ville,prenom,nom,vacant,matiereEnseigne,prochainCours,sujetProchaineReunion)
                cursor.execute(insert_query, data)
                connection.commit()
                print(f"Nombre de lignes insérées : {cursor.rowcount}")
        except Error as e:
            print("Erreur lors de l'insertion dans MySQL", e)
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print("La connexion MySQL est fermée")

    def mettreAJour():
        try:
            connection = mysql.connector.connect(
                host='localhost',            # Nom d'hôte ou adresse IP
                database='etab_db',   # Nom de la base de données
                user='root',    # Nom d'utilisateur MySQL
                password='bibo1996' # Mot de passe MySQL
            )
            if connection.is_connected():
                cursor = connection.cursor()
                try:
                    id = int(input("Saisir l'id du professeur : "))
                except :
                    print("Id ne correspond a aucun professeur !")

                verification_prof = """ SELECT * FROM professeur WHERE id = %s """
                cursor.execute(verification_prof, (id,))
                user = cursor.fetchone()
                if user:
                    print(f"L'utilisateur {id} existe dans la base de données.")
                    try:
                        dateNaissance = str(input('Date de naissance : '))
                        ville = str(input('Saisir la ville : '))
                        nom = str(input('Saisir le nom de l\'eleve : '))
                        prenom = str(input('Saisir le prenom de l\'eleve : '))
                        vacant = str(input('Saisir la vacant : '))
                        matiereEnseigne = str(input('Saisir le matricule : '))
                        prochainCours = str(input('Saisir le prochain cours : '))
                        sujetProchaineReunion = str(input('Saisir le sujet de la prochaine reunion : '))
                    except :
                        print('Insertion impossble')

                    update_query = """UPDATE professeur
                                        SET dateNaissance = %s,ville = %s, prenom = %s,nom = %s, vacant = %s, matiereEnseigne = %s, prochainCours = %s, sujetProchaineReunion = %s
                                        WHERE id = %s"""
                    
                    data = (dateNaissance, ville, nom,prenom, vacant, matiereEnseigne, prochainCours, sujetProchaineReunion, id)
                    cursor.execute(update_query, data)
                    connection.commit()
                    print(f"Ligne avec ID {id} modifiée avec succès")
                    return True
                else:
                    print(f"L'utilisateur {id} n'existe pas dans la base de données.")   
                    return False
        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")

    def supprimer():
        username = 'root'
        password = 'bibo1996'
        try:
            try:
                identifiant = int(input("Saisissez votre ID : "))
            except :
                pass
            connection = mysql.connector.connect(
                host='localhost',            # Nom d'hôte ou adresse IP du serveur MySQL
                database='etab_db',   # Nom de la base de données à laquelle se connecter
                user=username,               # Nom d'utilisateur MySQL
                password=password            # Mot de passe MySQL
            )
            if connection.is_connected():
                cursor = connection.cursor()
                query = """ SELECT * FROM professeur WHERE id = %s"""
                cursor.execute(query,(identifiant,))
                user = cursor.fetchall()
                if user:
                    try:
                        print(f"Le professeur {identifiant} existe dans la base de données.")
                        cursor = connection.cursor()
                        queryDelete = """ DELETE FROM professeur WHERE id = %s """
                        cursor.execute(queryDelete,(identifiant,))
                        connection.commit()
                        print(f"Ligne avec ID {identifiant} supprimée avec succès")
                    except Error as e:
                        print(f"Erreur lors de la suppression de la ligne : {e}")
        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")

    def obtenirProfesseur():
        username = 'root'
        password = 'bibo1996'
        try:
            connection = mysql.connector.connect(
                host='localhost',            # Nom d'hôte ou adresse IP du serveur MySQL
                database='etab_db',   # Nom de la base de données à laquelle se connecter
                user=username,               # Nom d'utilisateur MySQL
                password=password            # Mot de passe MySQL
            )
            if connection.is_connected():
                cursor = connection.cursor()
                select_query = """
                    SELECT * FROM professeur
                    ORDER BY id DESC
                    LIMIT 1
                """
                cursor.execute(select_query)
                last_row = cursor.fetchone()
                if last_row:
                    print("Dernière ligne ajoutée :")
                    print(last_row)
                else:
                    print("Aucune ligne trouvée.")
        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")

    def obtenir():
        username = 'root'
        password = 'bibo1996'
        try:
            connection = mysql.connector.connect(
                host='localhost',            # Nom d'hôte ou adresse IP du serveur MySQL
                database='etab_db',   # Nom de la base de données à laquelle se connecter
                user=username,               # Nom d'utilisateur MySQL
                password=password            # Mot de passe MySQL
            )
            if connection.is_connected():
                cursor = connection.cursor()
                select_query = "SELECT * FROM professeur"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                print(f"Nombre de lignes récupérées : {cursor.rowcount}")
                for row in rows:
                    print(row)
        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")

    def enseigner():
        pass

    def preparerCours():
        pass

    def assisterReunion():
        pass

    def menu_professeur():
        print('****************************************************************************** \n')
        print('GESTION DES PROFESSEURS \n')
        print('****************************************************************************** \n')

        liste_menu_professeur = [
            {1:"Ajouter un professeur"},
            {2:"Supprimer un professeur"},
            {3:"Modifier un professeur"},
            {4:"Lister un professeur"},
            {5:"Obtenir le dernier professeur ajouté"},
            {6:"Retour"},
            {7:"Quitter\n"}
        ]

        for element in liste_menu_professeur:
            for keys , value in element.items():
                print(f'{keys} : {value}')
        try:
            message = int (input('Veuillez saisir votre choix : '))
        except ValueError:
            print('Vous devez saisir un chiffre.')
            Professeur.menu_professeur()
        return message