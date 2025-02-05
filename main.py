import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from bibliotheque import Bibliotheque
from livre import Livre

class BibliothequeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de la Bibliothèque")
        self.root.geometry("600x600")
        self.root.configure(bg="#f0f8ff")

        self.biblio = Bibliotheque()

        # Style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12), padding=6)
        style.configure("TLabel", background="#f0f8ff", font=("Helvetica", 12))
        style.configure("TFrame", background="#f0f8ff")

        # Titre principal
        title_label = tk.Label(root, text="Gestion de la Bibliothèque", font=("Helvetica", 18, "bold"), bg="#f0f8ff", fg="#4682b4")
        title_label.pack(pady=10)

        # Champs de saisie
        form_frame = tk.Frame(root, bg="#f0f8ff")
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Titre :").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.titre_entry = ttk.Entry(form_frame)
        self.titre_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Auteur :").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.auteur_entry = ttk.Entry(form_frame)
        self.auteur_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(form_frame, text="Année :").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.annee_entry = ttk.Entry(form_frame)
        self.annee_entry.grid(row=2, column=1, padx=10, pady=5)

        # Boutons personnalisés
        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        def create_button(text, command, color):
            button = tk.Button(button_frame, text=text, command=command, font=("Helvetica", 12, "bold"), bg=color, fg="#ffffff", activebackground="#4682b4", activeforeground="#ffffff", padx=10, pady=5)
            return button

        create_button("Ajouter Livre", self.ajouter_livre, "#4682b4").grid(row=0, column=0, padx=5)
        create_button("Supprimer Livre", self.supprimer_livre, "#d2691e").grid(row=0, column=1, padx=5)
        create_button("Lister Livres", self.lister_livres, "#4682b4").grid(row=0, column=2, padx=5)
        create_button("Sauvegarder", self.sauvegarder_livres, "#4682b4").grid(row=0, column=3, padx=5)
        create_button("Charger", self.charger_livres, "#4682b4").grid(row=0, column=4, padx=5)

        # Zone de liste
        self.liste_livres = tk.Listbox(root, width=70, height=12, font=("Courier", 11), bg="#ffffff", fg="#333333")
        self.liste_livres.pack(padx=10, pady=10)

        # Footer
        footer_frame = tk.Frame(root, bg="#f0f8ff")
        footer_frame.pack(pady=10)

        ttk.Label(footer_frame, text="Application de gestion de bibliothèque", font=("Helvetica", 10, "italic"))
        ttk.Label(footer_frame, text="2025.copyRight©ChwiaDembarque", font=("Helvetica", 9)).pack()

    def ajouter_livre(self):
        titre = self.titre_entry.get().strip()
        auteur = self.auteur_entry.get().strip()
        try:
            annee = int(self.annee_entry.get().strip())
            livre = Livre(titre, auteur, annee)
            self.biblio.ajouter_livre(livre)
            messagebox.showinfo("Succès", f"Livre ajouté : {livre}")
            self.titre_entry.delete(0, tk.END)
            self.auteur_entry.delete(0, tk.END)
            self.annee_entry.delete(0, tk.END)
            self.lister_livres()
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def supprimer_livre(self):
        titre = self.titre_entry.get().strip()
        try:
            self.biblio.supprimer_livre(titre)
            messagebox.showinfo("Succès", f"Livre supprimé : {titre}")
            self.lister_livres()
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    def lister_livres(self):
        self.liste_livres.delete(0, tk.END)  # Efface l'affichage existant
        livres = self.biblio.lister_livres()
        
        if not livres:
            self.liste_livres.insert(tk.END, "Aucun livre disponible.")
        else:
            for livre in livres:
                self.liste_livres.insert(tk.END, livre)

    def sauvegarder_livres(self):
        nom_fichier = "bibliotheque.txt"
        self.biblio.sauvegarder_livres(nom_fichier)
        messagebox.showinfo("Succès", "Liste des livres sauvegardée.")

    def charger_livres(self):
        nom_fichier = "maListe.txt"
        self.biblio.charger_livres(nom_fichier)
        self.lister_livres()
        messagebox.showinfo("Succès", "Liste des livres chargée.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliothequeGUI(root)
    root.mainloop()
