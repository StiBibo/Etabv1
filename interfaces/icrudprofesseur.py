from abc import ABC, abstractmethod

class ICRUDProfesseur(ABC):
    @abstractmethod
    def ajouter(self,professeur):
        pass

    @abstractmethod
    def mettreAJour(self,professeur):
        pass

    @abstractmethod
    def supprimer(self,identifiant:int):
        pass

    @abstractmethod
    def obtenirProfesseur(self) -> list:
        pass

    @abstractmethod
    def obtenir(self,identifiant:int):
        pass