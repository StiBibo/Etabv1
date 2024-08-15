from abc import ABC, abstractmethod

class ICRUDEleve(ABC):
    @abstractmethod
    def ajouter(self,eleve):
        pass

    @abstractmethod
    def mettreAJour(self,eleve):
        pass

    @abstractmethod
    def supprimer(self,identifiant:int):
        pass

    @abstractmethod
    def obtenirEleve(self) -> list:
        pass

    @abstractmethod
    def obtenir(self,identifiant:int):
        pass