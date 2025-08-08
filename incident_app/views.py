# incident_app/views.py

from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db import transaction
from django.shortcuts import render, get_object_or_404
from .models import CollecteIncident, AnalyseIncident, SuiviIncident
from .forms import CollecteIncidentForm, ActionFormSet, AnalyseIncidentForm,EquipeAnalyseFormSet , RecommandationAnalyseFormSet, SuiviIncidentForm

def home_view(request):
    """ Affiche la page d'accueil (landing page). """
    return render(request, 'incident_app/home.html')

class CollecteIncidentListView(ListView):
    model = CollecteIncident
    template_name = 'incident_app/collecteincident_list.html'
    context_object_name = 'incidents'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date_inc', '-heure_inc')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(num_inc__icontains=query) |
                Q(lieu__libelle_lieu__icontains=query) |
                Q(ouvrage__libelle_ouvrage__icontains=query)
            )
        return queryset

class CollecteIncidentDetailView(DetailView):
    model = CollecteIncident
    template_name = 'incident_app/collecteincident_detail.html'
    pk_url_kwarg = 'num_inc'

class CollecteIncidentCreateView(CreateView):
    model = CollecteIncident
    form_class = CollecteIncidentForm
    template_name = 'incident_app/collecteincident_form.html'
    
    def get_success_url(self):
        return reverse_lazy('incident_app:collecteincident_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            # data['equipes'] = EquipeFormSet(self.request.POST, prefix='equipes')
            data['actions'] = ActionFormSet(self.request.POST, prefix='actions')
        else:
            # data['equipes'] = EquipeFormSet(prefix='equipes')
            data['actions'] = ActionFormSet(prefix='actions')
        return data
        
    def form_valid(self, form):
        context = self.get_context_data()
        actions = context['actions']
        
        with transaction.atomic():
            self.object = form.save()
            if actions.is_valid():
                actions.instance = self.object
                actions.save()

        return super().form_valid(form)
    
    
    
    
    
    

class AnalyseIncidentCreateView(CreateView):
    model = AnalyseIncident
    form_class = AnalyseIncidentForm
    template_name = 'incident_app/analyse_incident_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # On récupère l'incident parent pour l'afficher en contexte
        self.collecte_incident = get_object_or_404(CollecteIncident, num_inc=self.kwargs['num_inc'])
        data['collecte_incident'] = self.collecte_incident
        
        if self.request.POST:
            data['equipes'] = EquipeAnalyseFormSet(self.request.POST, prefix='equipes')
            data['recommandations'] = RecommandationAnalyseFormSet(self.request.POST, prefix='recommandations')
        else:
            data['equipes'] = EquipeAnalyseFormSet(prefix='equipes')
            data['recommandations'] = RecommandationAnalyseFormSet(prefix='recommandations')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        equipes = context['equipes']
        recommandations = context['recommandations']
        
        with transaction.atomic():
            # On lie l'analyse à l'incident parent avant de sauvegarder
            form.instance.incident = self.collecte_incident
            self.object = form.save()
            
            if equipes.is_valid() and recommandations.is_valid():
                equipes.instance = self.object
                equipes.save()
                recommandations.instance = self.object
                recommandations.save()

        return super().form_valid(form)

    def get_success_url(self):
        # Redirige vers la page de détail de l'incident après l'analyse
        return reverse_lazy('incident_app:collecteincident_detail', kwargs={'num_inc': self.object.incident.num_inc})
    
    
    
    

class SuiviIncidentCreateView(CreateView):
    model = SuiviIncident
    form_class = SuiviIncidentForm
    template_name = 'incident_app/suivi_incident_form.html'

    def form_valid(self, form):
        # On récupère l'incident parent depuis l'URL
        collecte_incident = get_object_or_404(CollecteIncident, num_inc=self.kwargs['num_inc'])
        # On lie le suivi à cet incident
        form.instance.incident = collecte_incident
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # On ajoute l'incident au contexte pour l'afficher sur la page
        context['collecte_incident'] = get_object_or_404(CollecteIncident, num_inc=self.kwargs['num_inc'])
        return context

    def get_success_url(self):
        # On redirige l'utilisateur vers la page de détail de l'incident
        return reverse_lazy('incident_app:collecteincident_detail', kwargs={'num_inc': self.kwargs['num_inc']})