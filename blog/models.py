from django.db import models

loko = (
    ('Rouge', 'Rouge'),
    ('Blanc', 'Blanc'),
    ('Jaune', 'Jaune'),
)

lehibe = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL'),
    ('Autre', 'Autre'),
)

class InfoPerso1(models.Model):
    nom1 = models.CharField(max_length = 30, verbose_name = 'Nom')
    prenom1 = models.CharField(max_length = 50, verbose_name = 'Prénoms')
    contact1 = models.CharField(max_length = 10, verbose_name = 'Contact')
    domicile1 = models.CharField(max_length = 30, verbose_name = 'Lieu')

    def __str__(self):
        return (str(self.id) + " " + self.nom1 + " " + self.prenom1)

class InfoCommande1(models.Model):
    id_commande1 = models.DateTimeField(primary_key = True, auto_now = True)
    couleur1 = models.CharField(help_text = u'Choisir une couleur', max_length = 10, choices = loko, default = 'Rouge')
    taille = models.CharField(help_text = u'Choisir une taille', max_length = 10, choices = lehibe, default = 'L')
    comment = models.CharField(help_text = u'Votre Commentaire', max_length = 100, blank = True)
    nombre = models.IntegerField(default = 1)
    avance = models.IntegerField(default = 15000)
    reste = models.IntegerField(default = 5000)
    payement = models.BooleanField(help_text=u'Payé?', default=False, unique = False,)
    id_client1 = models.ForeignKey(InfoPerso1, help_text = u'Choisir le Client', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id_client1)

class InfoPerso2(models.Model):
    nom2 = models.CharField(max_length = 30, verbose_name = 'Nom')
    prenom2 = models.CharField(max_length = 50, verbose_name = 'Prénoms')
    contact2 = models.CharField(max_length = 10, verbose_name = 'Contact')
    domicile2 = models.CharField(max_length = 30, verbose_name = 'Lieu')

    def __str__(self):
        return (str(self.id) + " " + self.nom2 + " " + self.prenom2)

class InfoCommande2(models.Model):
    id_commande2 = models.DateTimeField(primary_key = True, auto_now = True)
    taille = models.CharField(help_text = u'Choisir une taille', max_length = 10, choices = lehibe, default = 'L')
    comment = models.CharField(help_text = u'Votre Commentaire', max_length = 100, blank = True)
    nombre = models.IntegerField(default = 1)
    avance = models.IntegerField(default = 10000)
    reste = models.IntegerField(default = 5000)
    payement = models.BooleanField(help_text=u'Payé?', default=False, unique = False,)
    id_client2 = models.ForeignKey(InfoPerso2, help_text = u'Choisir le Client', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id_client2)


    