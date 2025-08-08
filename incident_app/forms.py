# incident_app/forms.py (Mis à jour)

from django import forms
from .models import CollecteIncident, ActionMenee, AnalyseIncident, EquipeAnalyse, RecommandationAnalyse
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
    class Meta:
        model = AnalyseIncident
        exclude = ['incident'] # L'incident sera lié automatiquement dans la vue
        widgets = {
            'date_analyse': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure_dbt_analyse': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'heure_fin_analyse': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'constat': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'cause': forms.Select(attrs={'class': 'form-select'}),
            # Vous pouvez ajouter ici des widgets pour les autres champs si nécessaire
        }

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