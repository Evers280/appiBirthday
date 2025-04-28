from .models import Invites, Admin, Billets
from rest_framework import serializers


class InvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invites
        fields = '__all__'
        

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        
        
class BilletsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billets
        fields = '__all__'
                