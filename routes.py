from flask import render_template, url_for, redirect, request, flash
from flask_ti2_lebon import app, models
@app.route('/')
@app.route('/accueil')
def accueil():
    return render_template('accueil.html', title='Bienvenue sur mon super site de makeup')


@app.route('/categories')
def categories():
    liste_categories = models.vue_produits_cat.query.distinct('nom_cat')
    return render_template('categories.html', title='Nos categories', liste=type(liste_categories),liste_cat=liste_categories)

@app.route('/produits_categories')
def produits_categories():
    id_cat = request.args.get('id_cat')
    liste_produits = models.vue_produits_cat.query.filter_by(id_cat=id_cat)
    return render_template('produits_categorie.html', title='Nos produits',produits=liste_produits,
                           typeprod=type(liste_produits))

@app.route('/tous_produits')
def tous_produits():
    liste_produits = models.vue_produits_cat.query.all()
    return render_template('tous_produits.html', title='Nos produits', liste_prod=liste_produits)
