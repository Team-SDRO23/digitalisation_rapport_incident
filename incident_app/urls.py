# incident_app/urls.py (Mis à jour)
from django.urls import path
from .views import (
    home_view,
    CollecteIncidentListView,
    CollecteIncidentDetailView,
    CollecteIncidentCreateView,
    AnalyseIncidentCreateView,
)


app_name = 'incident_app'

urlpatterns = [
    # Page d'accueil
    path('', home_view, name='home'),
    
    # Liste des incidents
    path('rapports/', CollecteIncidentListView.as_view(), name='collecteincident_list'),
    
    # Création d'un incident
    path('rapports/nouveau/', CollecteIncidentCreateView.as_view(), name='collecteincident_create'),
    
    path('rapports/<str:num_inc>/analyser/', AnalyseIncidentCreateView.as_view(), name='analyseincident_create'),
    
    # Détail d'un incident
    path('rapports/<str:num_inc>/', CollecteIncidentDetailView.as_view(), name='collecteincident_detail'),
]


