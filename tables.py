import pyodbc

# Establishing a connection to the database
conn_str = (
    "Driver=ODBC Driver 17 for SQL Server;"
    "Server=localhost;"
    "Database=projdb;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Trusted_Connection=yes;"
)
cnxn = pyodbc.connect(conn_str)

# Retrieving table names
cursor = cnxn.cursor()
cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE';")
tables = cursor.fetchall()

# Generating HTML content for navigation links
nav_links = ""
for table in tables:
    table_name = table[0]
    nav_links += f"<li><a href='#{table_name}'>{table_name}</a></li>"

# Generating HTML content for table data
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Data</title>
    <link rel="stylesheet" href="casino.css">
</head>

<body>
<div class="sidebar">
    <h2 class="sidebar-title">Casino</h2>
        <nav>
            <ul>{nav_links}</ul>
        </nav>
    <div id="bottom-link" style="text-align: center;">
        <a href="requetes.html" class="button" class="button">Consulter les requêtes SQL</a>
    </div>    
</div>

<div class="main-content">

    """
javascript_code = """
    <script>
    // Fonctionnalité pour supprimer des lignes de tableau
    document.addEventListener('DOMContentLoaded', function () {
        document.querySelectorAll('.delete-btn').forEach(button => {
            button.addEventListener('click', function (e) {
                e.target.closest('tr').remove(); // Supprime la ligne du tableau
            });
        });
    });
    </script>
</div>
"""

for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    html_content += f"<div id='{table_name}'><h2>{table_name}:</h2>"
    html_content += "<table border='1'><tr>"
    # Generating table headers
    for column in cursor.description:
        html_content += f"<th>{column[0]}</th>"
    html_content += "</tr>"
    # Generating table rows
    for row in rows:
        html_content += "<tr>"
        for value in row:
            html_content += f"<td>{value}</td>"
    # Ajout du bouton de suppression dans chaque ligne
        # html_content += "<td><button class='delete-btn'>Supprimer</button></td>"
        html_content += "</tr>"

    html_content += "</table></div>"

html_content += javascript_code
html_content += "</body></html>" 

# Saving HTML content to a file with UTF-8 encoding
with open("database_content.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML content saved to database_content.html")
