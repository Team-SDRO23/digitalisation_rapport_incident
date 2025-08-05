from django.contrib import admin
from .models import (
    Lieu, Ouvrage, EquipeAnalyse, Equipement,
    Cause, ActionMenee, CollecteIncident, AnalyseIncident,
    TypeReseau, RecommandationAnalyse, SuiviIncident
)


@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle_lieu']
    search_fields = ['libelle_lieu']


@admin.register(TypeReseau)
class TypeReseauAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']
    search_fields = ['type']


@admin.register(Ouvrage)
class OuvrageAdmin(admin.ModelAdmin):
    list_display = ['id', 'libelle_ouvrage', 'type_reseau']
    search_fields = ['libelle_ouvrage']
    list_filter = ['type_reseau']


@admin.register(EquipeAnalyse)
class EquipeAnalyseAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom', 'structure', 'role', 'incident']
    search_fields = ['nom', 'structure', 'role']
    list_filter = ['structure']


@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'ouvrage']
    search_fields = ['type']
    list_filter = ['ouvrage']


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_cause']
    search_fields = ['type_cause']


@admin.register(ActionMenee)
class ActionMeneeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'heure', 'manoeuvre', 'type_reseau', 'action', 'incident']
    search_fields = ['manoeuvre', 'action']
    list_filter = ['date', 'type_reseau']


@admin.register(CollecteIncident)
class CollecteIncidentAdmin(admin.ModelAdmin):
    list_display = ['num_inc', 'date_inc', 'heure_inc', 'lieu', 'ouvrage', 'equipement']
    search_fields = ['num_inc', 'equipement__type', 'reprise_client']
    list_filter = ['date_inc', 'lieu', 'ouvrage', 'equipement']


@admin.register(AnalyseIncident)
class AnalyseIncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_analyse', 'repartition', 'incident', 'cause']
    search_fields = ['repartition', 'constat', 'list_acteurs']
    list_filter = ['date_analyse', 'lieu', 'ouvrage', 'equipement']


@admin.register(RecommandationAnalyse)
class RecommandationAnalyseAdmin(admin.ModelAdmin):
    list_display = ['id', 'action', 'responsabilite', 'delai', 'cout', 'analyse_inc']
    search_fields = ['action', 'responsabilite']
    list_filter = ['delai']


@admin.register(SuiviIncident)
class SuiviIncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'incident', 'tenue_delai', 'efficacite_action']
    search_fields = ['commentaire_tenue_delai', 'commentaire_efficacite']
    list_filter = ['tenue_delai', 'efficacite_action']
