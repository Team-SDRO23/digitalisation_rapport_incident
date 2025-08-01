from django.contrib import admin
from .models import (
    Lieu, Ouvrage, EquipeAnalyse, Equipement,
    Cause, ActionMenee, CollecteIncident
)

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle_lieu']
    search_fields = ['libelle_lieu']


@admin.register(Ouvrage)
class OuvrageAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle_ouvrage']
    search_fields = ['libelle_ouvrage']


@admin.register(EquipeAnalyse)
class EquipeAnalyseAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'structure', 'role']
    search_fields = ['nom', 'structure', 'role']


@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    search_fields = ['type']


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_cause']
    search_fields = ['type_cause']


@admin.register(ActionMenee)
class ActionMeneeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'heure', 'manoeuvre', 'type_reseau', 'action']
    search_fields = ['manoeuvre', 'action']
    list_filter = ['date', 'type_reseau']


@admin.register(CollecteIncident)
class CollecteIncidentAdmin(admin.ModelAdmin):
    list_display = ['num_inc', 'date_inc', 'heure_inc', 'siege', 'lieu', 'ouvrage', 'equipement']
    search_fields = ['siege', 'localisation', 'reprise_client']
    list_filter = ['date_inc', 'lieu', 'ouvrage', 'equipement']
