from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Livre, Auteur, Emprunt
from .serializers import LivreSerializer, AuteurSerializer, EmpruntSerializer

class Auteurdetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Détails d'un auteur

    Cette vue gère les requêtes GET pour un auteur spécifique, permettant de récupérer ses détails.
    Elle gère également les requêtes PUT et DELETE pour mettre à jour ou supprimer un auteur.
    L'identifiant de l'auteur est fourni dans l'URL.
    """
    serializer_class = AuteurSerializer
    permission_classes = [IsAuthenticated]
    queryset = Auteur.objects.all()

class Auteurlist(generics.ListCreateAPIView):
    """
    Liste des auteurs

    Cette vue gère les requêtes GET et POST pour les auteurs.
    GET retourne une liste de tous les auteurs.
    POST permet de créer un nouvel auteur avec les données fournies dans le corps de la requête.
    """
    serializer_class = AuteurSerializer
    permission_classes = [IsAuthenticated]
    queryset = Auteur.objects.all()

class Livredetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Détails d'un livre

    Cette vue gère les requêtes GET pour un livre spécifique, permettant de récupérer ses détails.
    Elle gère également les requêtes PUT et DELETE pour mettre à jour ou supprimer un livre.
    L'identifiant du livre est fourni dans l'URL.
    """
    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticated]
    queryset = Livre.objects.all()

class Livrelist(generics.ListCreateAPIView):
    """
    Liste des livres

    Cette vue gère les requêtes GET et POST pour les livres.
    GET retourne une liste de tous les livres avec la possibilité de filtrer par date de publication et genre.
    POST permet de créer un nouveau livre avec les données fournies dans le corps de la requête.
    """
    serializer_class = LivreSerializer
    permission_classes = [IsAuthenticated]
    queryset = Livre.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_publication', 'genre']

class Emprunteurdetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Détails d'un emprunt

    Cette vue gère les requêtes GET pour un emprunt spécifique, permettant de récupérer ses détails.
    Elle gère également les requêtes PUT et DELETE pour mettre à jour ou supprimer un emprunt.
    L'identifiant de l'emprunt est fourni dans l'URL.
    """
    serializer_class = EmpruntSerializer
    permission_classes = [IsAuthenticated]
    queryset = Emprunt.objects.all()

class Emprunteurlist(generics.ListCreateAPIView):
    """
    Liste des emprunts

    Cette vue gère les requêtes GET et POST pour les emprunts.
    GET retourne une liste de tous les emprunts.
    POST permet de créer un nouvel emprunt avec les données fournies dans le corps de la requête.
    """
    serializer_class = EmpruntSerializer
    permission_classes = [IsAuthenticated]
    queryset = Emprunt.objects.all()
