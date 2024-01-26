from rest_framework import serializers
from .models import Livre, Auteur, Emprunt
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password','email']
        extra_kwargs={'password':{'write_only':True}}

