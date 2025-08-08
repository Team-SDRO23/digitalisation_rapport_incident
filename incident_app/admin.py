from django.contrib import admin
from .models import (
    Lieu, Ouvrage, EquipeAnalyse, Equipement,
    Cause, ActionMenee, CollecteIncident, AnalyseIncident,
    TypeReseau, RecommandationAnalyse, SuiviIncident
)

# "inlines" permettra de voir et de modifier les analyses, les actions, les équipes et
# les recommandations directement depuis la page d'un incident,
# sans avoir à naviguer entre les différentes sections.

# ===================================================================
# --- DÉFINITION DES VUES "INLINE" ---
# ===================================================================

# Ces classes permettent d'afficher les modèles liés directement
# dans la page du modèle parent.

class ActionMeneeInline(admin.TabularInline):
    model = ActionMenee
    extra = 1  # Affiche 1 formulaire vide par défaut

class EquipeAnalyseInline(admin.TabularInline):
    model = EquipeAnalyse
    extra = 1

class RecommandationAnalyseInline(admin.TabularInline):
    model = RecommandationAnalyse
    extra = 1

class SuiviIncidentInline(admin.StackedInline):
    model = SuiviIncident
    extra = 1
    max_num = 1 # Un seul suivi par incident

# L'analyse est un cas particulier (OneToOne), on l'affiche de manière groupée
class AnalyseIncidentInline(admin.StackedInline):
    model = AnalyseIncident
    extra = 1
    max_num = 1 # Une seule analyse par incident


# ===================================================================
# --- CONFIGURATION DES VUES PRINCIPALES DE L'ADMIN ---
# ===================================================================

@admin.register(CollecteIncident)
class CollecteIncidentAdmin(admin.ModelAdmin):
    list_display = ('num_inc', 'objet', 'date_inc', 'lieu', 'ouvrage')
    search_fields = ('num_inc', 'objet', 'lieu__libelle_lieu', 'ouvrage__libelle_ouvrage')
    list_filter = ('date_inc', 'lieu', 'ouvrage')
    date_hierarchy = 'date_inc' # Permet une navigation rapide par date
    
    # On intègre les modèles liés directement dans la page de l'incident
    inlines = [
        ActionMeneeInline,
        AnalyseIncidentInline,
        SuiviIncidentInline,
    ]

@admin.register(AnalyseIncident)
class AnalyseIncidentAdmin(admin.ModelAdmin):
    list_display = ('incident', 'date_analyse', 'cause')
    search_fields = ('incident__num_inc', 'constat')
    list_filter = ('date_analyse', 'cause')

    # On intègre l'équipe et les recommandations directement dans la page de l'analyse
    inlines = [
        EquipeAnalyseInline,
        RecommandationAnalyseInline,
    ]

@admin.register(EquipeAnalyse)
class EquipeAnalyseAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'structure', 'role', 'analyse')
    search_fields = ('nom', 'structure', 'role')
    list_filter = ['structure']


# --- Enregistrement des autres modèles (moins complexes) ---

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle_lieu')
    search_fields = ('libelle_lieu',)

@admin.register(TypeReseau)
class TypeReseauAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')

@admin.register(Ouvrage)
class OuvrageAdmin(admin.ModelAdmin):
    list_display = ('libelle_ouvrage', 'type_reseau')
    list_filter = ('type_reseau',)
    search_fields = ('libelle_ouvrage',)

@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ('type', 'ouvrage')
    list_filter = ('ouvrage',)
    search_fields = ('type',)

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('type_cause',)

@admin.register(ActionMenee)
class ActionMeneeAdmin(admin.ModelAdmin):
    list_display = ('incident', 'date', 'action')
    list_filter = ('date',)

@admin.register(RecommandationAnalyse)
class RecommandationAnalyseAdmin(admin.ModelAdmin):
    list_display = ('action', 'responsabilite', 'delai')
    list_filter = ('delai',)
    
@admin.register(SuiviIncident)
class SuiviIncidentAdmin(admin.ModelAdmin):
    list_display = ('incident', 'tenue_delai', 'efficacite_action')
    list_filter = ('tenue_delai', 'efficacite_action')