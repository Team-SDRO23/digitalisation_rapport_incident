# incident_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Redirige la racine du site vers la liste des incidents
    path('', RedirectView.as_view(url='/incidents/', permanent=True)),
    # Inclut les URLs de l'application sous le préfixe "incidents/"
    path('incidents/', include('incident_app.urls')),
]