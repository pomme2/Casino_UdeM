import pyodbc
from html import escape

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

# Function to generate HTML from query results
def generate_html_table(header, data):
    html = "<table border='1'><tr>"
    # Adding table headers
    for column in header:
        html += f"<th>{escape(str(column[0]))}</th>"
    html += "</tr>"
    # Adding table rows
    if data:
        for row in data:
            html += "<tr>"
            for value in row:
                html += f"<td>{escape(str(value))}</td>"
            html += "</tr>"
    html += "</table>"
    return html

# Function to execute stored procedure and write HTML result to a file
def execute_and_write_to_html(proc_name, *args, file_name):
    result, header = execute_stored_procedure(proc_name, *args)
    html_result = generate_html_table(header, result)
    # Linking to styles.css file
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Data</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
{html_result}
<div style="text-align: center;">
    <a href="requetes.html">Back to Requetes</a>
</div>

</body>
</html>
"""
    with open(file_name, "w") as file:
        file.write(html_content)

# Example stored procedure functions:
def rechercheProfitInterval(date1, date2):
    execute_and_write_to_html("rechercheProfitInterval", date1, date2, file_name="output_profit_intervalle.html")

def rechercheProfitDate(date1):
    execute_and_write_to_html("rechercheProfitDate", date1, file_name="output_profit_date.html")

def recherchePieceParPanne(enPanne):
    execute_and_write_to_html("recherchePieceParPanne", enPanne, file_name="output_piece_par_panne.html")

# Execute stored procedures and save results to HTML files
rechercheProfitInterval('2023-01-01', '2023-04-09')
rechercheProfitDate('2023-04-01')
recherchePieceParPanne(1)
