# livre.py
class Livre:
    def __init__(self, titre: str, auteur: str, annee_publication: int):
        if not titre or not auteur:
            raise ValueError("Le titre et l'auteur sont obligatoires.")
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"{self.titre} par {self.auteur}, publié en {self.annee_publication}"
    
        

