from django.urls import path, include

from .views import Livrelist,Livredetails,Auteurlist,Auteurdetails,Emprunteurlist,Emprunteurdetails


urlpatterns=[
    path('auteur/',Auteurlist.as_view()),
    path('auteur/<int:pk>/',Auteurdetails.as_view()),
    path('livres/',Livrelist.as_view()),
    path('livres/<int:pk>/',Livredetails.as_view()),
    path('emprunt/',Emprunteurlist.as_view()),
    path('emprunt/<int:pk>/',Emprunteurdetails.as_view()),

]