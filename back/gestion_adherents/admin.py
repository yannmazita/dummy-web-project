from django.contrib import admin
from .models import (
    Adherents,
    Arbitre,
    Archives,
    Catalogue,
    Categories,
    Contacts,
    Courriels,
    Creneaux,
    Documents,
    Entraine,
    Entrainements,
    Equipes,
    Joue,
    Matchs,
    Postes,
    Salles,
    Telephones,
)

admin.site.register(Adherents)
admin.site.register(Categories)
admin.site.register(Equipes)
admin.site.register(Entraine)
admin.site.register(Postes)
admin.site.register(Archives)
admin.site.register(Entrainements)
admin.site.register(Joue)
admin.site.register(Contacts)
admin.site.register(Creneaux)
admin.site.register(Salles)
admin.site.register(Courriels)
admin.site.register(Telephones)
admin.site.register(Arbitre)
admin.site.register(Matchs)
admin.site.register(Documents)
admin.site.register(Catalogue)
