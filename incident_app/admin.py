from django.contrib import admin
from .models import (
    Lieu, Ouvrage, EquipeAnalyse, Equipement,
    Cause, ActionMenee, CollecteIncident, AnalyseIncident,
    TypeReseau, RecommandationAnalyse, SuiviIncident,Acteur,Expertise
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
    list_display = ['id', 'nom', 'structure', 'role', 'analyseInc']
    search_fields = ['nom', 'role']
    list_filter = ['structure']


@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'ouvrage']
    search_fields = ['ouvrage']
    list_filter = ['type']


@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_cause']
    search_fields = ['type_cause']

@admin.register(Acteur)
class ActeurAdmin(admin.ModelAdmin):
    list_display = ['id', 'acteur']
    search_fields = ['acteur']

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'expertise']
    search_fields = ['expertise']



@admin.register(ActionMenee)
class ActionMeneeAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'heure', 'manoeuvre', 'type_reseau', 'action', 'incident']
    search_fields = ['manoeuvre', 'action']
    list_filter = ['date']


@admin.register(CollecteIncident)
class CollecteIncidentAdmin(admin.ModelAdmin):
    list_display = ['num_inc', 'date_inc', 'heure_inc', 'lieu', 'ouvrage', 'equipement']
    search_fields = ['num_inc']
    list_filter = ['date_inc', 'lieu']


@admin.register(AnalyseIncident)
class AnalyseIncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_analyse', 'repartition', 'incident', 'cause']
    search_fields = ['id']
    list_filter = ['date_analyse']


@admin.register(RecommandationAnalyse)
class RecommandationAnalyseAdmin(admin.ModelAdmin):
    list_display = ['id', 'action', 'responsabilite', 'delai', 'cout', 'analyse_inc']
    search_fields = ['action']
    list_filter = ['delai']


@admin.register(SuiviIncident)
class SuiviIncidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'incident', 'tenue_delai', 'efficacite_action']
    list_filter = ['tenue_delai']
