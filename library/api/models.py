from django.db  import models
from django.conf import settings

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    bio = models.TextField()


    def __str__(self):
        return self.nom


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50)
    date_publication = models.DateField()

    def __str__(self):
        return self.titre
class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    emprunteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_emprunt = models.DateField()

    def __str__(self):
        return f"{self.livre.titre} emprunté par {self.emprunteur}"