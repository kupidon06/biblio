from rest_framework import serializers
from .models import Livre, Auteur, Emprunt

class LivreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Livre
        fields="__all__"

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model=Auteur
        fields="__all__"
class EmpruntSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emprunt
        fields="__all__"
