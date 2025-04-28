from django.contrib import admin
from .models import Invites, Billets, Admin

# Register your models here.
class InvitesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'sexe', 'age', 'adresse', 'telephone', 'email')
    search_fields = ('id', 'nom', 'prenom', 'sexe', 'age')
    list_filter = ('id', 'nom', 'prenom', 'sexe', 'age', 'adresse', 'telephone')


class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'sexe', 'age', 'adresse', 'telephone', 'email')
   

class BilletsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'num_billet')
    search_fields = ('invites', 'nom', 'num_billet')
    list_filter = ('invites', 'nom', 'num_billet')
    
    
admin.site.register(Invites, InvitesAdmin)
admin.site.register(Admin, AdminAdmin)
admin.site.register(Billets, BilletsAdmin)