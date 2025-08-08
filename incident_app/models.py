from django.db import models

class Lieu(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_lieu = models.CharField(max_length=100)

    def __str__(self):
        return f"Lieu: {self.libelle_lieu}"


class TypeReseau(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"TypeReseau: {self.type}"




class Ouvrage(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_ouvrage = models.CharField(max_length=100)
    type_reseau = models.ForeignKey(TypeReseau, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ouvrage: {self.libelle_ouvrage} ({self.type_reseau})"



class Equipement(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    ouvrage = models.ForeignKey(Ouvrage, on_delete=models.CASCADE)
    def __str__(self):
        return f"[{self.id}] Équipement: {self.type} ({self.ouvrage.id})"


class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    type_cause = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.id}] Cause: {self.type_cause}"
    

class ActionMenee(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    heure = models.TimeField()
    manoeuvre = models.CharField(max_length=200)
    type_reseau = models.CharField(max_length=100)
    action = models.CharField(max_length=200)
    incident = models.ForeignKey( 'CollecteIncident',  on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"[{self.id}] {self.date} {self.heure} - "
            f"{self.manoeuvre} - {self.type_reseau} - {self.action} "
            f"(Incident {self.incident})"
        )

class CollecteIncident(models.Model):
    
    objet = models.TextField(verbose_name="Objet de l'analyse", blank=True, null=True)
    origine_cause_probable = models.TextField(verbose_name="Origine et cause probable",blank=True, null=True)
    
    # Champs existants
    num_inc = models.CharField("N° Fiche", max_length=50, primary_key=True)
    date_inc = models.DateField("Date de l'événement")
    heure_inc = models.TimeField("Heure de l'événement")
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    ouvrage = models.ForeignKey(Ouvrage, on_delete=models.CASCADE)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    constat = models.TextField("Constat sur terrain (non-conformités)", default='RAS')
    fait_avant = models.TextField("Faits et paramètres avant l'incident")
    fait_apres = models.TextField("Faits et paramètres après l'incident", blank=True, null=True)
    
    # Section Environnement
    env_atmospherique = models.CharField("Environnement Atmosphérique", max_length=200, default='RAS')
    env_vegeta = models.CharField("Environnement Végétal", max_length=200, default='RAS')
    env_animal = models.CharField("Environnement Animal", max_length=200, default='RAS')
    env_humain = models.CharField("Environnement Humain", max_length=200, default='RAS')
    env_industriel = models.CharField("Environnement Industriel",  max_length=200, default='RAS')
    
    # Section Causes
    cause_agression = models.CharField(max_length=200)
    cause_technique = models.CharField(max_length=200)
    
    # Section Actions et Impacts
    reprise_client = models.CharField("Détails sur la reprise de la clientèle", max_length=200)
    mes_exploitation = models.CharField("Mesures conservatoires (Exploitation)", max_length=200, default='RAS')
    mes_maintenance = models.CharField("Mesures conservatoires (Maintenance)", max_length=200, default='RAS')
    impact_param_qp = models.CharField("Impact sur paramètres QP (ex: 224 MWh d'END)", max_length=200)
    situation_provisoire = models.CharField(max_length=200)
    action_a_menee = models.TextField("Actions à mener", blank=True, null=True)
    autre_info = models.TextField("Autres informations", default='RAS', blank=True)


    def __str__(self):
        return (
            f"[{self.num_inc}] {self.date_inc} {self.heure_inc} "
            f"Lieu: {self.lieu.libelle_lieu} - Ouvrage: {self.ouvrage.libelle_ouvrage} - "
            f"Equipement: {self.equipement.type} "
        )


class AnalyseIncident(models.Model):
    id = models.AutoField(primary_key=True)
    date_analyse = models.DateField()
    heure_dbt_analyse = models.TimeField()
    heure_fin_analyse = models.TimeField()
    impact_nod = models.CharField(max_length=200)
    impact_nip = models.CharField(max_length=200)
    impact_tmc = models.CharField(max_length=200)
    impact_cout = models.CharField(max_length=200)
    impact_autre = models.CharField(max_length=200)
    list_acteurs = models.TextField()
    list_expertise = models.TextField()
    complt_equipment = models.TextField()
    complt_equip_concerne = models.TextField()
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    ouvrage = models.ForeignKey(Ouvrage, on_delete=models.CASCADE)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    repartition = models.CharField(max_length=100)
    constat = models.TextField()
    jour_constat = models.CharField(max_length=100, default='RAS')
    heure_dbt_constat = models.CharField(max_length=100, default='RAS')
    heure_fin_constat = models.CharField(max_length=100, default='RAS')
    saison_constat = models.CharField(max_length=100, default='RAS')
    complt_espace_env = models.TextField()

    illustration = models.ImageField(upload_to='illustrations/', null=True, blank=True)

    cause = models.ForeignKey('Cause', on_delete=models.SET_NULL, null=True)
    incident = models.OneToOneField(CollecteIncident, on_delete=models.CASCADE, related_name='analyse')
    
    conclusion = models.TextField(verbose_name="Conclusion de l'analyse", blank=True, null=True)

    def __str__(self):
        return f'Analyse {self.cause.type_cause} - {self.incident}'

    
class EquipeAnalyse(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    analyse = models.ForeignKey(AnalyseIncident, on_delete=models.CASCADE, related_name='equipe', null=True)

    def __str__(self):
        return f"[{self.id}] {self.nom} - {self.structure} - {self.role} (Analyse {self.analyse})"

    

class Acteur(models.Model):
     id = models.AutoField(primary_key=True)
     acteur= models.CharField(max_length=100)
     def __str__(self):
        return f"acteur: {self.acteur}"
    
    
class Expertise(models.Model):
    id = models.AutoField(primary_key=True)
    expertise= models.CharField(max_length=100)
    def __str__(self):
        return f"expertise: {self.expertise}"
    
    
    
class RecommandationAnalyse(models.Model):
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=200)
    responsabilite = models.CharField(max_length=100)
    delai = models.DateField(null=True, blank=True)
    cout = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    analyse_inc = models.ForeignKey(AnalyseIncident, on_delete=models.CASCADE, related_name='recommandations', null=True)

    def __str__(self):
        return (
            f"[{self.id}] Action: {self.action}, "
            f"Analyse: {self.analyse_inc}"
        )



class SuiviIncident(models.Model):
    id = models.AutoField(primary_key=True)
    incident = models.ForeignKey(CollecteIncident, on_delete=models.CASCADE)
    tenue_delai = models.BooleanField()
    commentaire_tenue_delai = models.TextField(blank=True, null=True)
    efficacite_action = models.BooleanField()
    commentaire_efficacite = models.TextField(blank=True, null=True)

    def __str__(self):
        return (
            f"SuiviIncident({self.incident}, "
            f"tenue_delai={self.tenue_delai}, "
            f"commentaire_tenue_delai='{self.commentaire_tenue_delai}', "
            f"efficacite_action={self.efficacite_action}, "
            f"commentaire_efficacite='{self.commentaire_efficacite}')"
        )

