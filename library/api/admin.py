from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Livre, Auteur, Emprunt

# Classe ModelAdmin pour le modèle Livre
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    list_filter = (
        ('date_publication', DateFieldListFilter),
    )
    # Ajoutez ici d'autres options d'administration si nécessaire

# Enregistrement des modèles et des classes ModelAdmin correspondantes
admin.site.register(Livre, LivreAdmin)
admin.site.register(Auteur)  # Supposons que Auteur n'a pas besoin de personnalisation spéciale
admin.site.register(Emprunt)  # De même pour Emprunt

# Vous pouvez également créer des classes ModelAdmin pour Auteur et Emprunt si nécessaire
