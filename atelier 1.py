class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print(f"Matricule:{self.matricule}")
        print(f"Marque: {self.marque}")
        print(f"Couleur: {self.couleur}")

class Parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def entrerVoiture(self, voiture):
        for v in self.listeVoitures:
            if v.matricule == voiture.matricule:
                print("La voiture existe déjà dans le parc.")
                return
            if len(self.listeVoitures) < self.capacite:
                self.listeVoitures.append(voiture)
                print("Voiture ajoutée dans le parc.")
            else:
                print("Le parc est plein.")

    def sortirVoiture(self, voiture):

        if voiture in self.listeVoitures:
            self.listeVoitures.remove(voiture)
            print("Voiture retirée du parc.")
            print("Places libres:", self.calculerNbrPlacesLibres())
        else:
            print("Cette voiture n'est pas dans le parc.")

    def calculerNbrPlacesLibres(self):
        return self.capacite - len(self.listeVoitures)
parc1 = Parc(5, "QUEBEC", 3)

v1 = Voiture("H475S", "Honda", "Noir")
v2 = Voiture("JH56H", "Tesla", "Gris")
v3 = Voiture("UH35JH", "GMC", "Blanc")
v4 = Voiture("YTR587", "KIA", "Bleu")

parc1.entrerVoiture(v1)
parc1.entrerVoiture(v2)
parc1.entrerVoiture(v3)
parc1.entrerVoiture(v4)

v1.afficherInformations()
v2.afficherInformations()

parc1.sortirVoiture(v2)
