# incident_app/forms.py (Mis à jour)

from django import forms
from .models import (
    CollecteIncident, ActionMenee, AnalyseIncident, 
    EquipeAnalyse, RecommandationAnalyse, SuiviIncident,
    Acteur, Expertise 
)
from django.forms import inlineformset_factory




# ===================================================================
# --- FORMULAIRES POUR LA SECTION A (COLLECTE DE L'INCIDENT) ---
# ===================================================================


class CollecteIncidentForm(forms.ModelForm):
    class Meta:
        model = CollecteIncident
        # fields = '__all__'
        fields = [
            'objet', 'origine_cause_probable', 'num_inc', 'date_inc', 'heure_inc', 
            'lieu', 'ouvrage', 'equipement', 'constat', 'fait_avant', 'fait_apres',
            'env_atmospherique', 'env_vegeta', 'env_animal', 'env_humain', 'env_industriel',
            'cause_agression', 'cause_technique', 'reprise_client', 'mes_exploitation',
            'mes_maintenance', 'impact_param_qp', 'situation_provisoire', 'action_a_menee',
            'autre_info'
        ]
        widgets = {
            'objet': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'origine_cause_probable': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'num_inc': forms.TextInput(attrs={'class':'form-control'}),
            'date_inc': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'heure_inc': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
            'lieu': forms.Select(attrs={'class':'form-select'}),
            'ouvrage': forms.Select(attrs={'class':'form-select'}),
            'equipement': forms.Select(attrs={'class':'form-select'}),
            'constat': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'fait_avant': forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'fait_apres': forms.Textarea(attrs={'rows':3,'class':'form-control'}),
            'env_atmospherique': forms.TextInput(attrs={'class':'form-control'}),
            'env_vegeta': forms.TextInput(attrs={'class':'form-control'}),
            'env_animal': forms.TextInput(attrs={'class':'form-control'}),
            'env_humain': forms.TextInput(attrs={'class':'form-control'}),
            'env_industriel': forms.TextInput(attrs={'class':'form-control'}),
            'cause_agression': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'cause_technique': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'reprise_client': forms.TextInput(attrs={'class':'form-control'}),
            'mes_exploitation': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'mes_maintenance': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'impact_param_qp': forms.TextInput(attrs={'class':'form-control'}),
            'situation_provisoire': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'action_a_menee': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
            'autre_info': forms.Textarea(attrs={'rows':2,'class':'form-control'}),
        }



ActionFormSet = inlineformset_factory(
    CollecteIncident, ActionMenee,
    fields=['date','heure', 'manoeuvre', 'type_reseau', 'action'], extra=1, can_delete=True,
    widgets={
        'date': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        'heure': forms.TimeInput(attrs={'type':'time','class':'form-control'}),
        'manoeuvre': forms.TextInput(attrs={'class':'form-control'}),
        'type_reseau': forms.TextInput(attrs={'class':'form-control'}),
        'action': forms.Textarea(attrs={'rows': 2, 'class':'form-control'})
    }
)



# ===================================================================
# --- FORMULAIRES POUR LA SECTION B (ANALYSE DE L'INCIDENT) ---
# ===================================================================

class AnalyseIncidentForm(forms.ModelForm):
    # On définit les champs qui afficheront les cases à cocher
    # Ce ne sont PAS les champs du modèle, mais des champs temporaires pour le formulaire
    acteurs_selection = forms.ModelMultipleChoiceField(
        queryset=Acteur.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Sélectionner les acteurs au moment de l'incident"
    )
    
    expertises_selection = forms.ModelMultipleChoiceField(
        queryset=Expertise.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Sélectionner les expertises utiles pour analyse"
    )
    
    class Meta:
        model = AnalyseIncident
        fields = [
            'date_analyse', 'heure_dbt_analyse', 'heure_fin_analyse', 'constat', 
            'cause', 'illustration', 'conclusion'
        ]
        exclude = ['incident', 'list_acteurs', 'list_expertise']
        widgets = {
            'date_analyse': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_dbt_analyse': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'heure_fin_analyse': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'constat': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'cause': forms.Select(attrs={'class': 'form-select'}),
            'illustration': forms.FileInput(attrs={'class': 'form-control'}), # Widget pour les fichiers
            'conclusion': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}), # Widget pour la conclusion
            # Vous pouvez ajouter ici des widgets pour les autres champs si nécessaire
        }
        
    def save(self, commit=True):
        # On récupère les sélections des cases à cocher
        acteurs_selectionnes = self.cleaned_data.get('acteurs_selection', [])
        expertises_selectionnees = self.cleaned_data.get('expertises_selection', [])

        # On convertit la liste des objets en une chaîne de noms
        # ex: "Exploitants usine SOUBRE, Acteurs de conduite BCC"
        self.instance.list_acteurs = ", ".join([acteur.acteur for acteur in acteurs_selectionnes])
        self.instance.list_expertise = ", ".join([expertise.expertise for expertise in expertises_selectionnees])
        
        # On sauvegarde l'instance normalement
        return super().save(commit)

EquipeAnalyseFormSet = inlineformset_factory(
    AnalyseIncident, EquipeAnalyse,
    fields=['nom', 'structure', 'role'], extra=1, can_delete=True,
    widgets={
        'nom': forms.TextInput(attrs={'class': 'form-control'}),
        'structure': forms.TextInput(attrs={'class': 'form-control'}),
        'role': forms.TextInput(attrs={'class': 'form-control'}),
    }
)

RecommandationAnalyseFormSet = inlineformset_factory(
    AnalyseIncident, RecommandationAnalyse,
    fields=['action', 'responsabilite', 'delai'], extra=1, can_delete=True,
    widgets={
        'action': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
        'responsabilite': forms.TextInput(attrs={'class': 'form-control'}),
        'delai': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    }
)




# ===================================================================
# --- SECTION C : FORMULAIRE DE SUIVI D'INCIDENT ---
# ===================================================================

class SuiviIncidentForm(forms.ModelForm):
    class Meta:
        model = SuiviIncident
        # On exclut le lien avec l'incident, qui sera fait automatiquement
        exclude = ['incident']
        widgets = {
            'tenue_delai': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'commentaire_tenue_delai': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'efficacite_action': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'commentaire_efficacite': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }