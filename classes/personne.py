from datetime import date

class Personne():
    def __init__(self,id,dateNaissance,ville,prenom,nom, telephone) -> None:
        self.__id = id
        self.__dateNaissance = dateNaissance
        self.__ville = ville
        self.__prenom = prenom
        self.__nom = nom
        self.__telephone = telephone
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    
    def get_dateNaissance(self):
        return self.__dateNaissance
    def set_dateNaissance(self, dateNaissance):
        self.__dateNaissance = dateNaissance
    
    def get_ville(self):
        return self.__ville
    def set_ville(self, ville):
        self.__ville = ville
    
    def get_prenom(self):
        return self.__prenom
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def get_nom(self):
        return self.__nom
    def set_nom(self, nom):
        self.__nom = nom
    
    def get_telephone(self):
        return self.__telephone
    def set_telephone(self, telephone):
        self.__telephone = telephone
    
    
    def __str__(self) -> str:
        return f"Personne {self.get_id()} : {self.get_nom()} {self.get_prenom()} née a {self.get_ville()} "
    
    def supprimer():
        pass

    def lister():
        pass

    def obtenirAge(self):
        today = date.today()
        return today.year - self.get_dateNaissance().year - \
               ((today.month, today.day) < (self.get_dateNaissance.month, self.get_dateNaissance.day))