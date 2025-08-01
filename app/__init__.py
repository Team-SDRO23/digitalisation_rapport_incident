from flask import Flask
from .extensions import db
from .routes import main

# Import pour l'admin
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import (
    Lieu, Ouvrage, EquipeAnalyse, Equipement,
    Cause, ActionMenee, CollecteIncident
)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    app.register_blueprint(main)

    # 🔧 Configuration de Flask-Admin
    admin = Admin(app, name='Interface Admin', template_mode='bootstrap3')
    admin.add_view(ModelView(Lieu, db.session))
    admin.add_view(ModelView(Ouvrage, db.session))
    admin.add_view(ModelView(EquipeAnalyse, db.session))
    admin.add_view(ModelView(Equipement, db.session))
    admin.add_view(ModelView(Cause, db.session))
    admin.add_view(ModelView(ActionMenee, db.session))
    admin.add_view(ModelView(CollecteIncident, db.session))

    return app
