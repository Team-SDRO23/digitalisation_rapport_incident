from django.db import models

class Lieu(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_lieu = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.id}] Lieu: {self.libelle_lieu}"


class Ouvrage(models.Model):
    id = models.AutoField(primary_key=True)
    libelle_ouvrage = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.id}] Ouvrage: {self.libelle_ouvrage}"


class EquipeAnalyse(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    structure = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.id}] {self.nom} - {self.structure} - {self.role}"


class Equipement(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return f"[{self.id}] Équipement: {self.type}"


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

    def __str__(self):
        return f"[{self.id}] {self.date} {self.heure} - {self.manoeuvre} - {self.type_reseau} - {self.action}"


class CollecteIncident(models.Model):
    num_inc = models.CharField(max_length=50, primary_key=True)
    date_inc = models.DateField()
    heure_inc = models.TimeField()
    siege = models.CharField(max_length=100)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    ouvrage = models.ForeignKey(Ouvrage, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=100)
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    constat = models.CharField(max_length=200, default='RAS')
    fait_avant = models.CharField(max_length=200)
    fait_apres = models.CharField(max_length=200, blank=True, null=True)
    env_atmospherique = models.CharField(max_length=200, default='RAS')
    env_vegeta = models.CharField(max_length=200, default='RAS')
    env_animal = models.CharField(max_length=200, default='RAS')
    env_industriel = models.CharField(max_length=200, default='RAS')
    cause_agression = models.CharField(max_length=200)
    cause_technique = models.CharField(max_length=200)
    action = models.ForeignKey(ActionMenee, on_delete=models.CASCADE)
    reprise_client = models.CharField(max_length=200)
    mes_exploitation = models.CharField(max_length=200, default='RAS')
    mes_maintenance = models.CharField(max_length=200, default='RAS')
    impact_param_qp = models.CharField(max_length=200)
    situation_provisoire = models.CharField(max_length=200)
    action_a_menee = models.CharField(max_length=200)
    autre_info = models.CharField(max_length=200, default='RAS')

    def __str__(self):
        return (
            f"[{self.num_inc}] {self.date_inc} {self.heure_inc} - Siege: {self.siege} - "
            f"Lieu: {self.lieu.libelle_lieu} - Ouvrage: {self.ouvrage.libelle_ouvrage} - "
            f"Equipement: {self.equipement.type} - Action: {self.action.action}"
        )
