from django.db import models

# Create your guest models here.
class Invites(models.Model):
    
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    sexe = models.CharField(max_length=10)
    age = models.IntegerField(default=1)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=12, unique =True)
    email = models.EmailField( unique=True)

    def __str__(self):
        return self.nom
    


class Admin(models.Model):
    nom = models.CharField(max_length=25, default="nom de l'administrateur")
    prenom = models.CharField(max_length=25, default="prenom de l'administrateur")
    sexe = models.CharField(default="masculin", max_length=10)
    age = models.IntegerField(default=25)
    adresse = models.CharField(max_length=50, default="mon quartier")
    telephone = models.CharField(max_length=12, default="1234567890")
    email = models.EmailField(default='exemple@gmail.com')
    mot_de_passe = models.CharField(max_length=12, default="1234567890", null=False)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)    
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return  f"{self.nom} {self.prenom}"
    
    
    
class Billets(models.Model):
    
    #nom de l'invité
    invites = models.ForeignKey(Invites, on_delete=models.CASCADE, null=False)
    nom = models.CharField(max_length=25, default="nom de l'invité")
    prenom = models.CharField(max_length=15, default= "prenom de l'invité")
    num_billet = models.CharField(max_length=3) 
    
    
    def __str__(self):
        return self.num_billet
    