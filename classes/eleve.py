from classes.personne import Personne
from interfaces.icrudeleve import ICRUDEleve
import mysql.connector
from mysql.connector import Error
import datetime

class Eleve(Personne, ICRUDEleve):
    def __init__(self, id, dateNaissance, ville, prenom, nom,telephone,classe,matricule) -> None:
        super().__init__(id, dateNaissance, ville, prenom, nom,telephone)
        self.__classe = classe
        self.__matricule = matricule

    def get_classe(self):
        return self.__classe
    def set_classe(self, classe):
        self.__classe = classe
 
    def get_matricule(self):
        return self.__matricule
    def set_matricule(self, matricule):
        self.__matricule = matricule

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
                    nom = str(input('Saisir le nom de l\'eleve : '))
                    prenom = str(input('Saisir le prenom de l\'eleve : '))
                    classe = str(input('Saisir la classe : '))
                    matricule = str(input('Saisir le matricule : '))
                    telephone = str(input('Saisir le telephone : '))

                except :
                    print('Insertion impossble')

                print("Connexion réussie à la base de données MySQL")

                cursor = connection.cursor()
                insert_query = """INSERT INTO eleve (dateNaissance, ville, prenom,nom,telephone, classe, matricule)
                                VALUES (%s, %s, %s , %s, %s, %s, %s)"""

                data = (dateNaissance,ville,prenom,nom,telephone,classe,matricule)
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
                id = int(input("Saisissez l' ID : "))
                select_query = """SELECT * FROM eleve WHERE id = %s"""

                # Exécuter la requête
                cursor.execute(select_query, (id,))
                user = cursor.fetchone()
                if user:
                    print(f"L'utilisateur {id} existe dans la base de données.")
                    try:
                        dateNaissance = str(input('Date de naissance : '))
                        ville = str(input('Saisir la ville : '))
                        nom = str(input('Saisir le nom de l\'eleve : '))
                        prenom = str(input('Saisir le prenom de l\'eleve : '))
                        classe = str(input('Saisir la classe : '))
                        matricule = str(input('Saisir le matricule : '))
                        telephone = str(input('Saisir le telephone : '))
                    except :
                        print('Insertion impossble')

                    update_query = """UPDATE eleve
                                        SET dateNaissance = %s,ville = %s, prenom = %s,nom = %s, telephone = %s,classe = %s,matricule = %s,
                                        WHERE id = %s"""
                    
                    data = (dateNaissance, ville,prenom,nom,telephone, classe, matricule, id)
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
            connection = mysql.connector.connect(
                host='localhost',           
                database='etab_db',  
                user=username,   
                password=password 
            )
            if connection.is_connected():
                cursor = connection.cursor()
                try : 
                    identifiant = int(input('Saisissez votre ID : '))
                except :
                    print('Erreur saisie')

                query = """ SELECT * FROM eleve WHERE id = %s """
                print(f"resultat du cursor : {cursor}")
                cursor.execute(query,(identifiant,))
                user = cursor.fetchone()
                if user:
                    print(f"L'utilisateur {identifiant} existe dans la base de données.")
                    try:
                        print(f"L'eleve {identifiant} existe dans la base de données.")
                        cursor = connection.cursor()
                        queryDelete = """ DELETE FROM eleve WHERE id = %s """
                        cursor.execute(queryDelete, (identifiant,))
                        connection.commit()
                        print(f"Ligne avec ID {identifiant} supprimée avec succès")
                    except Error as e:
                        print(f"Erreur lors de la suppression de la ligne : {e}")
                    return True
                else:
                    print(f"L'utilisateur {identifiant} n'existe pas dans la base de données.")
                    return False
        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")

    def obtenirEleve():
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
                    SELECT * FROM eleve
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
                select_query = "SELECT * FROM eleve"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                print(f"Nombre de lignes récupérées : {cursor.rowcount}")
                for row in rows:
                    print(row)
        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")
 
    
    def menu_eleve():

        print('****************************************************************************** \n')
        print('GESTION DES ELEVES \n')
        print('****************************************************************************** \n')

        liste_menu_eleve = [
            {1:"Ajouter un eleve"},
            {2:"Supprimer un eleve"},
            {3:"Modifier un eleve"},
            {4:"Lister un eleve"},
            {5:"Obtenir le dernier élève ajouté"},
            {6:"Retour"},
            {7:"Quitter\n"}
        ]

        for element in liste_menu_eleve:
            for keys , value in element.items():
                print(f'{keys} : {value}')

        try:
            message = int (input('Veuillez saisir votre choix : '))
        except ValueError:
            print('Vous devez saisir un chiffre.')
            Eleve.menu_eleve()
        return message

    