import pyodbc
from html import escape

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

def camel_case_to_title(camel_case_str):
    words = []
    start_index = 0
    for i in range(1, len(camel_case_str)):
        if camel_case_str[i].isupper():
            words.append(camel_case_str[start_index:i])
            start_index = i
    words.append(camel_case_str[start_index:]) 
    
    return ' '.join(word.capitalize() for word in words)

def execute_stored_procedure(proc_name, *args):
    """
    Execute a stored procedure with optional arguments and return the result.
    """
    cursor = cnxn.cursor()
    formatted_args = [f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args]
    cursor.execute(f"EXEC {proc_name} " + ', '.join(formatted_args))
    try:
        rows = cursor.fetchall()
    except pyodbc.ProgrammingError:
        # Handle non-select queries
        rows = None
    return rows, cursor.description


def generate_html_table(header, data):
    html = "<table border='1'><tr>"
   
    for column in header:
        html += f"<th>{escape(str(column[0]))}</th>"
    html += "</tr>"
   
    if data:
        for row in data:
            html += "<tr>"
            for value in row:
                html += f"<td>{escape(str(value))}</td>"
            html += "</tr>"
    html += "</table>"
    return html


def execute_and_write_to_html(proc_name, *args, file_name):
    result, header = execute_stored_procedure(proc_name, *args)
    html_result = generate_html_table(header, result)
    # Linking to tables.css file
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Data</title>
    <link rel="stylesheet" href="../static/CSS/tables.css">
</head>
<body>
<h2>{camel_case_to_title(proc_name)}:</h2>
{html_result}
<div style="text-align: center;">
    <a href="../static/requetes.html" class="button">Retour aux requ&ecirc;tes</a>
</div>

</body>
</html>
"""
    with open(file_name, "w") as file:
        file.write(html_content)

# Fonctions pour les procédures stockées :
def rechercheProfitInterval(date1, date2):
    execute_and_write_to_html("rechercheProfitInterval", date1, date2, file_name="table_profit_intervalle.html")

def rechercheProfitDate(date1):
    execute_and_write_to_html("rechercheProfitDate", date1, file_name="table_profit_date.html")

def recherchePieceParPanne(enPanne):
    execute_and_write_to_html("recherchePieceParPanne", enPanne, file_name="table_piece_par_panne.html")

def NbrPieceParFournisseur():
    execute_and_write_to_html("NbrPieceParFournisseur", file_name="table_piece_par_fournisseur.html")

def PersonnelSpecifique(id_role):
    execute_and_write_to_html("PersonnelSpecifique", id_role, file_name="table_personnel_specifique.html")

def listePanne():
    execute_and_write_to_html("listePanne", file_name="table_liste_panne.html")

def listeProfitJeuParSecteur():
    execute_and_write_to_html("listeProfitJeuParSecteur", file_name="table_liste_profit_jeu_par_secteur.html")

def listeProfitMachineParSecteur():
    execute_and_write_to_html("listeProfitMachineParSecteur", file_name="table_liste_profit_machine_par_secteur.html")

def listeProfitMachineParPanne(enPanne):
    execute_and_write_to_html("listeProfitMachineParPanne", enPanne, file_name="table_liste_profit_machine_par_panne.html")

def listeProfitJeuxParPanne(enPanne):
    execute_and_write_to_html("listeProfitJeuxParPanne", enPanne, file_name="table_liste_profit_jeux_par_panne.html")

# Exécute les procédures stockées et enregistre les résultats dans des fichiers HTML
rechercheProfitInterval('2023-01-01', '2023-04-09')
rechercheProfitDate('2023-04-01')
recherchePieceParPanne(1)

NbrPieceParFournisseur()
PersonnelSpecifique(2)
listePanne()
listeProfitJeuParSecteur()
listeProfitMachineParSecteur()
listeProfitMachineParPanne(0)
listeProfitJeuxParPanne(0)