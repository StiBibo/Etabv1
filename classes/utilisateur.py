from classes.eleve import Eleve
import mysql.connector
from mysql.connector import Error
import datetime


class Utilisateur():
    def __init__(self,id,identifiant,motDePasse,dateCreation) -> None:
        self.__id = id
        self.__identifiant = identifiant
        self.__motDePasse = motDePasse
        self.__dateCreation = dateCreation

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id

    def get_identifiant(self):
        return self.__identifiant
    def set_identifiant(self, identifiant):
        self.__identifiant = identifiant

    def get_motDePasse(self):
        return self.__motDePasse
    def set_motDePasse(self, motDePasse):
        self.__motDePasse = motDePasse
    
    def get_dateCreation(self):
        return self.__dateCreation
    def set_dateCreation(self, dateCreation):
        self.__dateCreation = dateCreation

    def connexion_to_db():
        connection = None 
        try:
            connection = mysql.connector.connect(
                host='localhost',            
                database='etab_db', 
                user='root',
                password='bibo1996'
            )
            if connection.is_connected():
                print("Connexion réussie à la base de données MySQL")
                db_info = connection.get_server_info()
                print(f"Version du serveur MySQL : {db_info}")
                cursor = connection.cursor()
                cursor.execute("SELECT DATABASE();")
                db_name = cursor.fetchone()
                print(f"Vous êtes connecté à la base de données : {db_name[0]}")
                cursor.close()

        except Error as e:
            print(f"Erreur lors de la connexion à MySQL : {e}")
        finally:
            if connection and connection.is_connected():
                connection.close()
                print("La connexion MySQL est fermée")

    def authentification(search_username, motDePasse):
        print('****************************************************************************** \n')
        print('BIENVENU DANS L\'application ETAB v1.2 \n')
        print('****************************************************************************** \n')
        print('CONNEXION \n')
        username = 'root'
        password = 'bibo1996'
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',           
                database='etab_db',   
                user=username,              
                password=password          
            )
            if connection.is_connected():
                print(f"Connexion réussie pour l'utilisateur {username}")
                cursor = connection.cursor()
                select_query = """SELECT * FROM utilisateur WHERE pseudo = %s AND motDePasse = %s  """
                cursor.execute(select_query,(search_username, motDePasse))
                user = cursor.fetchone()
                if user:
                    print(f"L'utilisateur {search_username} existe dans la base de données.")
                    return True
                else:
                    print(f"L'utilisateur {search_username} n'existe pas dans la base de données.")
                    try :
                        insert_query = """INSERT INTO utilisateur (pseudo, motDePasse, dateCreation)
                                VALUES (%s, %s, %s)"""
                        data = ("admin", "admin", datetime.datetime.now())
                        cursor.execute(insert_query, data)
                        connection.commit()
                        # search_username = input("Saisissez votre identifiant :")
                        # motDePasse = input("Saisissez votre mot de passe : ")
                        # Utilisateur.authentification(search_username,motDePasse)
                    except Error as e:
                        print("Erreur lors de l'insertion dans MySQL", e)
                    return False

        except Error as e:
            print(f"Erreur lors de la vérification de l'utilisateur : {e}")

        finally:
            if connection and connection.is_connected():
                connection.close()
                print(f"La connexion MySQL pour l'utilisateur {username} est fermée")

    def ajouter():
        try:
            connection = mysql.connector.connect(
                host='localhost',           
                database='etab_db',   
                user='root',    
                password='bibo1996' 
            )

            if connection.is_connected():
                try :
                    identifiant = str(input("Saisir l'identification : "))
                    motDePasse = str(input("Saisir mot de passe : "))
                except : 
                    print('Insertion impossble')
                print("Connexion réussie à la base de données MySQL")
                cursor = connection.cursor()
                insert_query = """INSERT INTO utilisateur (pseudo, motDePasse, dateCreation)
                                VALUES (%s, %s, %s)"""

                data = (identifiant, motDePasse, datetime.datetime.now())
                cursor.execute(insert_query, data)
                connection.commit()
                print(f"Nombre de lignes insérées : {cursor.rowcount}")
        except Error as e:
            print("Erreur lors de l'insertion dans MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("La connexion MySQL est fermée")

    def modifierMotDePasse():
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
                    identifiant = input("Saisissez votre identifiant : ")
                except :
                    pass
                select_query = """SELECT * FROM utilisateur WHERE id = %s"""
                cursor.execute(select_query, (identifiant,))
                user = cursor.fetchone()
                if user:
                    print(f"L'utilisateur {identifiant} existe dans la base de données.")
                    print(f"Connexion réussie pour l'utilisateur {username}")
                    motDePasse = input("Saisissez votre mot de passe : ")
                
                    update_query = """UPDATE utilisateur
                                    SET motDePasse = %s
                                    WHERE pseudo = %s"""
                    cursor.execute(update_query, ( motDePasse, identifiant,))
                    connection.commit()
                    print(f"Ligne avec ID {identifiant} modifiée avec succès")
                    return True
                else:
                    print(f"L'utilisateur {identifiant} n'existe pas dans la base de données.")   
                    return False

        except Error as e:
            print(f"Erreur lors de la modification de la ligne : {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print(f"La connexion MySQL pour l'utilisateur {username} est fermée")

    def supprimerCompte():
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
                try :
                    identifiant = int(input("Saisissez votre identifiant : "))
                except : 
                    print('Insertion error')
                cursor = connection.cursor()
                query = """ SELECT * FROM utilisateur WHERE id = %s """
                cursor.execute(query,(identifiant,))
                user = cursor.fetchone()
                if user:
                    try:
                        print(f"L'utilisateur {identifiant} existe dans la base de données.")
                        cursor = connection.cursor()
                        motDePasse = input("Saisissez votre mot de passe : ")
                        queryDelete = """ DELETE FROM utilisateur WHERE id = %s """
                        cursor.execute(queryDelete, (identifiant,))
                        connection.commit()
                        print(f"Ligne avec ID {identifiant} supprimée avec succès")
                    except Error as e:
                        print(f"Erreur lors de la suppression de la ligne : {e}")
                    return True
                else:
                    print(f"L'utilisateur {identifiant} n'existe pas dans la base de données.") 
                    return False
        except:
            print(f"Erreur lors de la modification de la ligne : {e}")

    def listerUtilisateur():
        username = 'root'
        password = 'bibo1996'
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',           
                database='etab_db',   
                user=username,               
                password=password         
            )

            if connection.is_connected():
                print(f"Connexion réussie pour l'utilisateur {username}")
                cursor = connection.cursor()
                select_query = "SELECT * FROM utilisateur"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                print(f"Nombre de lignes récupérées : {cursor.rowcount}")
                for row in rows:
                    print(row)
        except Error as e:
            print(f"Erreur lors de la récupération des lignes : {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
                print(f"La connexion MySQL pour l'utilisateur {username} est fermée")

    def menu_utilisateur():
        print('****************************************************************************** \n')
        print('GESTION DES UTILISATEURS \n')
        print('****************************************************************************** \n')

        liste_menu_utilisateur = [
            {1:"Ajouter un utilisateur"},
            {2:"Supprimer un utilisateur"},
            {3:"Modifier un utilisateur"},
            {4:"Lister un utilisateur"},
            {5:"Retour"},
            {0:"Acceuil"},
        ]

        for element in liste_menu_utilisateur:
            for keys , value in element.items():
                print(f'{keys} : {value}')

        try:
            message = int (input('Veuillez saisir votre choix : '))
        except ValueError:
            print('Vous devez saisir un chiffre.')
            Eleve.menu_eleve()
        return message
