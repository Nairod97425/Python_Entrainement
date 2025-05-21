import plotly.express as px
import pandas as pd
import webbrowser

# Charger les données
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# a. Graphique des ventes par produit
figure_ventes_par_produit = px.bar(données, x='produit', y='qte', title='Ventes par produit')
figure_ventes_par_produit.write_html('ventes-par-produit.html')

# b. Graphique du chiffre d'affaires par produit
# Supposons que le chiffre d'affaires est calculé comme quantité * prix_unitaire
données['chiffre_affaires'] = données['qte'] * données['prix']
figure_ca_par_produit = px.bar(données, x='produit', y='chiffre_affaires', title='Chiffre d\'affaires par produit')
figure_ca_par_produit.write_html('chiffre-affaires-par-produit.html')

# Graphique existant des ventes par région
figure_ventes_par_region = px.pie(données, values='qte', names='region', title='Quantité vendue par région')
figure_ventes_par_region.write_html('ventes-par-region.html')

print('Les graphiques ont été générés avec succès !')
# Ouvrir le fichier HTML dans le navigateur par défaut
webbrowser.open_new_tab('ventes-par-region.html')
webbrowser.open_new_tab('ventes-par-produit.html')
webbrowser.open_new_tab('chiffre-affaires-par-produit.html')

print('ventes-par-région.html généré avec succès et ouvert dans une nouvelle fenêtre de navigateur !')
