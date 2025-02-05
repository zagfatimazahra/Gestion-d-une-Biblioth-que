# bibliotheque.py
import os
from livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre: Livre):
        if not isinstance(livre, Livre):
            raise TypeError("L'objet ajouté doit être une instance de la classe Livre.")
        self.livres.append(livre)
        print(f"Livre ajouté : {livre}")

    def supprimer_livre(self, titre: str):
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                print(f"Livre supprimé : {livre}")
                return
        raise ValueError("Livre non trouvé : impossible de supprimer.")

    def lister_livres(self):
        return [str(livre) for livre in self.livres] if self.livres else []

    def sauvegarder_livres(self, nom_fichier: str):
        try:
            with open(nom_fichier, 'w', encoding='utf-8') as fichier:
                for livre in self.livres:
                    fichier.write(f"{livre.titre};{livre.auteur};{livre.annee_publication}\n")
            print("Liste des livres sauvegardée avec succès.")
        except IOError:
            print("Erreur lors de la sauvegarde des livres.")

    def charger_livres(self, nom_fichier: str):
        if not os.path.exists(nom_fichier):
            print("Fichier inexistant.")
            return
        try:
            with open(nom_fichier, 'r', encoding='utf-8') as fichier:
                self.livres = []
                for ligne in fichier:
                    titre, auteur, annee_publication = ligne.strip().split(';')
                    self.ajouter_livre(Livre(titre, auteur, int(annee_publication)))
            print("Liste des livres chargée avec succès.")
        except (IOError, ValueError):
            print("Erreur lors du chargement des livres.")
