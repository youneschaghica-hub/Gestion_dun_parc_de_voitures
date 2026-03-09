class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print(f"Matricule:{self.matricule}")
        print(f"Marque: {self.marque}")
        print(f"Couleur: {self.couleur}")