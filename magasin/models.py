from django.db import models
from datetime import date


class Categorie(models.Model):
    TYPE_CHOICES = [
        ("Al", "Alimentaire"),
        ("Mb", "Meuble"),
        ("Sn", "Sanitaire"),
        ("Vs", "Vaisselle"),
        ("Vt", "Vêtement"),
        ("Jx", "Jouets"),
        ("Lg", "Linge de Maison"),
        ("Bj", "Bijoux"),
        ("Dc", "Décor"),
    ]
    name = models.CharField(max_length=50, choices=TYPE_CHOICES, default="Alimentaire")

    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adressse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom + " " + self.adressse + " " + self.email + " " + self.telephone


class Produit(models.Model):
    type_choices = [("fr", "frais"), ("cs", "conserver"), ("em", "emballé")]
    libelle = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3)
    type = models.CharField(max_length=2, choices=type_choices, default="em")
    img = models.ImageField(blank=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return (
            self.libelle
            + " "
            + self.description
            + " "
            + str(self.prix)
            + " "
            + self.type
        )


class ProduitNC(Produit):
    Duree_garantie = models.CharField(max_length=100)


class ProduitC(Produit):
    Duree_garantie = models.CharField(max_length=100)

from decimal import Decimal

class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    produits = models.ManyToManyField('Produit')
    totalCde = models.DecimalField(max_digits=10, decimal_places=3, default=Decimal('0.000'))

    def calcTotCde(self):
        total = Decimal('0.000')  # Initialize total as Decimal
        for produit in self.produits.all():
            total += produit.prix  # Add each product's price to total
        self.totalCde = total + totalCde# Update the totalCde field with the calculated total
        self.save()  # Save the changes to the instance
        return self.totalCde

    def __str__(self):
        affichage = str(self.dateCde) + " " + str(self.totalCde)
        for produit in self.produits.all():
            affichage += ' ' + produit.libelle + ' ' + str(produit.prix) + 'DT' + ' ' + produit.description + '/'
        return affichage
