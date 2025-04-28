from django.db import transaction
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Invites, Billets, Admin
from .serializers import InvitesSerializer, AdminSerializer, BilletsSerializer
from .permissions import IsAdminUser
from .email_utils import send_confirmation_email


# Create your views here.   
class InvitesViewSet(viewsets.ModelViewSet):
    queryset = Invites.objects.all()
    serializer_class = InvitesSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        elif self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdminUser()]
        else:    
            return [permissions.IsAuthenticated(), IsAdminUser()]
        

    def perform_create(self, serializer):
        with transaction.atomic():
            serializer.is_valid(raise_exception=True)
            invites = serializer.save()
            print(f"Invité créé : {invites.id}")
            try:
                billets = Billets.objects.create(
            
                    invites=invites,
                    nom = invites.nom,
                    prenom = invites.prenom,
                    num_billet = str(invites.id), 
                )
                print(f"Billet créé : {billets.num_billet}")
                send_confirmation_email(invites, billets)
                print("Email envoyé")   
                     
            except Exception as e:
                raise ValidationError(f"Erreur lors de la création du billet : {str(e)}") 
        
            

class AdminViewSet(viewsets.ModelViewSet): 
    queryset = Admin.objects.all()  
    serializer_class = AdminSerializer

    
    def get_permissions(self):
        if self.action in ['list', 'destroy']:
            return [IsAuthenticated()]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            return [permissions.IsAuthenticated(), IsAdminUser()]
        return [AllowAny()]
    

            

class BilletsViewSet(viewsets.ModelViewSet):
    queryset = Billets.objects.all()
    serializer_class = BilletsSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticated(), IsAdminUser()]
        return [permissions.IsAuthenticated(), IsAdminUser()]