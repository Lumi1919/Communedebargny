from django.db import models


class Album(models.Model):
    titre = models.CharField(max_length=250, blank=True, null=True)
    auteur = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo1 = models.ImageField(blank=True, null=True)
    photo2 = models.ImageField(blank=True, null=True)
    photo3 = models.ImageField(blank=True, null=True)
    photo4 = models.ImageField(blank=True, null=True)
    photo5 = models.ImageField(blank=True, null=True)
    photo6 = models.ImageField(blank=True, null=True)
    def __str__(self):

        return self.titre

class Evenement(models.Model):
    titre = models.CharField(max_length=250, blank=True, null=True)
    categorie = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.titre


class News(models.Model):
    titre = models.CharField(max_length=250, blank=True, null=True)
    texte = models.TextField()
    image = models.ImageField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.titre

class Bureau_municipal(models.Model):
    nom = models.CharField(max_length=250, blank=True, null=True)
    titre = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):

        return self.nom

class Avis(models.Model):
    titre = models.CharField(max_length=250, blank=True, null=True)
    texte = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.titre


class Une_photo(models.Model):
    image = models.ImageField(blank=True, null=True)
    titre = models.CharField(max_length=250, blank=True, null=True)
    texte = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.titre

class Doc(models.Model):
    titre = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    fichier = models.FileField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):

        return self.titre


doc_choice = {
    ('Extrait de naissance', 'Extrait de naissance'),
    ('Copie intégrale extrait de naissance', 'Copie intégrale extrait de naissance'),
    ('Certificat de mariage', 'Certificat de mariage'),
}
class Demarche(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    mail = models.EmailField(max_length=200, blank=True, null=True)
    tel = models.CharField(max_length=200, blank=True, null=True)
    document = models.CharField(max_length=200, blank=True, null=True, choices = doc_choice)
    piece_identite = models.FileField(blank=True, null=True)
    adresse = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nom