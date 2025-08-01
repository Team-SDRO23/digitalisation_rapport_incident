from .extensions import db

class Lieu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle_lieu = db.Column(db.String(100))

class Ouvrage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    libelle_ouvrage = db.Column(db.String(100))

class EquipeAnalyse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    structure = db.Column(db.String(100))
    role = db.Column(db.String(100))

class Equipement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100))

class Cause(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_cause = db.Column(db.String(100))

class ActionMenee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    heure = db.Column(db.Time)
    manoeuvre = db.Column(db.String(200))
    type_reseau = db.Column(db.String(100))
    action = db.Column(db.String(200))

class CollecteIncident(db.Model):
    num_inc = db.Column(db.Integer, primary_key=True)
    date_inc = db.Column(db.Date)
    heure_inc = db.Column(db.Time)
    siege = db.Column(db.String(100))
    id_lieu = db.Column(db.Integer, db.ForeignKey('lieu.id'))
    id_ouvrge = db.Column(db.Integer, db.ForeignKey('ouvrage.id'))
    localisation = db.Column(db.String(100))
    id_equip = db.Column(db.Integer, db.ForeignKey('equipement.id'))
    constat = db.Column(db.String(200), default='RAS')
    fait_avant = db.Column(db.String(200))
    fait_apres = db.Column(db.String(200), nullable=True)
    env_atmospherique = db.Column(db.String(200), default='RAS')
    env_vegeta = db.Column(db.String(200), default='RAS')
    env_animal = db.Column(db.String(200), default='RAS')
    env_industriel = db.Column(db.String(200), default='RAS')
    cause_agression = db.Column(db.String(200))
    cause_technique = db.Column(db.String(200))
    id_action = db.Column(db.Integer, db.ForeignKey('action_menee.id'))
    reprise_client = db.Column(db.String(200))
    mes_exploitation = db.Column(db.String(200), default='RAS')
    mes_maintenance = db.Column(db.String(200), default='RAS')
    impact_param_qp = db.Column(db.String(200))
    situation_provisoire = db.Column(db.String(200))
    action_a_menee = db.Column(db.String(200))
    autre_info = db.Column(db.String(200), default='RAS')