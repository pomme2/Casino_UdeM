import pyodbc

def render_tables_html():
    # Établissement d'une connexion à la base de données
    conn_str = (
        "Driver=ODBC Driver 17 for SQL Server;"
        "Server=localhost;"
        "Database=projdb;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Trusted_Connection=yes;"
    )
    cnxn = pyodbc.connect(conn_str)

    # Récupération des noms de table
    cursor = cnxn.cursor()
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
    tables = cursor.fetchall()

    # Generation HTML
    nav_links = ""
    for table in tables:
        table_name = table[0]
        nav_links += f"<li><a href='#{table_name}'>{table_name}</a></li>"

    # Generation HTML pour les tables
    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SQL Data</title>
        <link rel="stylesheet" href="../static/casino.css">
    </head>

    <body>
    <div class="sidebar">
        <h2 class="sidebar-title">Casino</h2>
            <nav>
                <ul>{nav_links}</ul>
            </nav>
        <div id="bottom-link" style="text-align: center;">
            <a href="../static/requetes.html" class="button" class="button">Consulter les requêtes SQL</a>
        </div>    
    </div>

    <div class="main-content">

        """

    # Insert the form for data insertion
    html_content += """
        <h2>Insert Data</h2>
        <form action="/insert_jeu" method="post">
            <label for="id">ID:</label><br>
            <input type="text" id="id" name="id"><br>
            
            <label for="nom">Nom:</label><br>
            <input type="text" id="nom" name="nom"><br>
            
            <label for="min_mise">Mise Minimale:</label><br>
            <input type="text" id="min_mise" name="min_mise"><br>
            
            <label for="max_mise">Mise Maximale:</label><br>
            <input type="text" id="max_mise" name="max_mise"><br><br>
            
            <input type="submit" value="Submit">
        </form>

        <form action="/insert_panneau_affichage" method="post">
            <label for="id">ID:</label><br>
            <input type="text" id="id" name="id"><br>
            
            <label for="marque">Marque:</label><br>
            <input type="text" id="marque" name="marque"><br>
            
            <label for="longueur">Longueur:</label><br>
            <input type="text" id="longueur" name="longueur"><br>
            
            <label for="largeur">Largeur:</label><br>
            <input type="text" id="largeur" name="largeur"><br><br>
            
            <input type="submit" value="Submit">
        </form>

        <form action="/insert_camera_surveillance" method="post">
            <label for="id">ID:</label><br>
            <input type="text" id="id" name="id"><br>
            
            <label for="marque">Secteur:</label><br>
            <input type="text" id="secteur" name="secteur"><br>
            
            <input type="submit" value="Submit">
        </form>
    """
    
    # Add update option
    html_content += """
        <h2>Update Data</h2>
        <form action="/update_jeu" method="post">
            <label for="update_id">ID:</label><br>
            <input type="text" id="update_id" name="id"><br>

            <label for="update_nom">Nouveau Nom:</label><br>
            <input type="text" id="update_nom" name="nom"><br><br>

            <input type="submit" value="Submit">
        </form>

        <form action="/update_panneau_affichage" method="post">
            <label for="update_id">ID:</label><br>
            <input type="text" id="update_id" name="id"><br>

            <label for="update_nom">Nouvelle Marque:</label><br>
            <input type="text" id="update_Marque" name="marque"><br><br>

            <input type="submit" value="Submit">
        </form>

        <form action="/update_camera_surveillance" method="post">
            <label for="update_id">ID:</label><br>
            <input type="text" id="update_id" name="id"><br>

            <label for="update_nom">Nouveau Secteur:</label><br>
            <input type="text" id="update_Secteur" name="secteur"><br><br>

            <input type="submit" value="Submit">
        </form>
    """

    for table in tables:
        table_name = table[0]
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        html_content += f"<div id='{table_name}'><h2>{table_name}:</h2>"
        html_content += "<table border='1'><tr>"

        # Generation des Titres
        for column in cursor.description:
            html_content += f"<th>{column[0]}</th>"
        html_content += "<th>Actions</th>"  # Ajout de l'en-tête "Actions"
        html_content += "</tr>"

        # Remplacement du bouton de suppression par un formulaire
        for row in rows:
            html_content += "<tr>"
            for value in row:
                html_content += f"<td>{value}</td>"
            # Ajout d'un formulaire de suppression dans chaque ligne
            row_id = row[0]  # Assumant que l'ID est la première colonne de la table
            html_content += f'''
            <td>
                <form action="/" method="POST">
                    <input type="hidden" name="table_name" value="{table_name}">
                    <input type="hidden" name="row_id" value="{row_id}">
                    <button type="submit" class="delete-btn">Supprimer</button>
                </form>
            </td>
            '''
            html_content += "</tr>"

        html_content += "</table></div>"

    html_content += "</body></html>" 

    # Retourne le contenu HTML généré
    return html_content
