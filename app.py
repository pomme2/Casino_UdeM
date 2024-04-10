from flask import Flask, request, redirect, url_for, render_template_string
from delete import delete_row
from insert_jeu import insert_data_jeu
from insert_panneau_affichage import insert_data_panneau_affichage
from insert_camera_surveillance import insert_data_camera_surveillance
from update import update_data
from tables import render_tables_html  # Import the insert_data method

app = Flask(__name__, '/static')

@app.route('/')
def show_tables():
    # Génère et retourne le HTML pour afficher les tables
    html_content = render_tables_html()
    return render_template_string(html_content)


# Endpoint for handling data insertion
@app.route('/insert_jeu', methods=['POST'])
def handle_insert_data1():
    # Extract data from the form
    id = request.form['id']
    nom = request.form['nom']
    min_mise = request.form['min_mise']
    max_mise = request.form['max_mise']
    
    # Call the insert_data method
    insert_data_jeu(id, nom, min_mise, max_mise)
    
    # Redirect to the main page showing the updated tables
    return redirect(url_for('show_tables'))


# Endpoint for handling data insertion
@app.route('/insert_panneau_affichage', methods=['POST'])
def handle_insert_data2():
    # Extract data from the form
    id = request.form['id']
    marque = request.form['marque']
    longueur = request.form['longueur']
    largeur = request.form['largeur']
    
    # Call the insert_data method
    insert_data_panneau_affichage(id, marque, longueur, largeur)
    
    # Redirect to the main page showing the updated tables
    return redirect(url_for('show_tables'))


# Endpoint for handling data insertion
@app.route('/insert_camera_surveillance', methods=['POST'])
def handle_insert_data3():
    # Extract data from the form
    id = request.form['id']
    secteur = request.form['secteur']
    
    # Call the insert_data method
    insert_data_camera_surveillance(id, secteur)
    
    # Redirect to the main page showing the updated tables
    return redirect(url_for('show_tables'))


#Endpoint for handling data update
@app.route('/update', methods=['POST'])
def handle_update_data():
    # Extract data from the form
    id = request.form['id']
    nom = request.form['nom']

#Call the update_data method
    update_data(nom, id)

#Redirect to the main page showing the updated tables
    return redirect(url_for('show_tables'))

# Faire distinction entre tous les delete avec les table 
@app.route('/', methods=['POST'])
def handle_delete_row():
    # Extrait le nom de la table et l'ID de la ligne à supprimer depuis le formulaire
    table_name = request.form['table_name']
    row_id = request.form['row_id']
    # Appelle la fonction de suppression
    delete_row(table_name, row_id)
    # Redirige vers la page principale qui montre les tables, maintenant mise à jour
    return redirect(url_for('show_tables'))

if __name__ == '__main__':
    app.run(debug=True)
