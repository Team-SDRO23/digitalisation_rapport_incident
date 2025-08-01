from flask import Blueprint, jsonify
from .models import Lieu
from .extensions import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify(message="Bienvenue dans l'application d'incident !")

@main.route('/lieux')
def get_lieux():
    lieux = Lieu.query.all()
    return jsonify([{"id": l.id, "libelle_lieu": l.libelle_lieu} for l in lieux])