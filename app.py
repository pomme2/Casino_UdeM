from flask import Flask, request, redirect, url_for, render_template_string
from delete import delete_row  # Assurez-vous que cette fonction accepte 'table_name' et 'row_id'
from tables import render_tables_html  # Cette fonction doit retourner le HTML des tables

app = Flask(__name__)

@app.route('/')
def show_tables():
    # Génère et retourne le HTML pour afficher les tables
    html_content = render_tables_html()
    return render_template_string(html_content)

@app.route('/delete_row', methods=['POST'])
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
