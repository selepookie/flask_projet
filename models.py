from . import db, app
from flask_sqlalchemy import SQLAlchemy

class vue_produits_cat(db.Model):
    id_produit = db.Column(db.Integer, primary_key=True)
    nom_prod = db.Column(db.String(25), nullable=False)
    descr_prod = db.Column(db.String(200))
    prix = db.Column(db.Float, nullable=True)
    nom_cat = db.Column(db.String(30), nullable=False)
    image = db.Column(db.String(60), nullable=True)
    id_cat = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.id_produit} : {self.nom_prod} : {self.descr_prod} : {self.prix} : {self.image} : {self.nom_cat}'