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

# CSS styles
css_styles = """
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
    }
    nav {
        background-color: #333;
        padding: 10px 0;
    }
    nav ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    nav ul li {
        display: inline;
        margin-right: 20px;
    }
    nav ul li a {
        color: #fff; 
        text-decoration: none; 
        font-weight: bold; 
        font-size: smaller; 
        font-family: Arial, sans-serif;
    }
    nav ul li a:hover {
        color: #ccc;
    }
    table {
        margin: 0 auto; /* Center the table */
        max-width: 800px; /* Limit the maximum width */
        width: 100%; /* Ensure the table takes the full width within its container */
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    a {
        color: #007bff; 
        text-decoration: none; 
        font-weight: bold; 
    }
    a:hover {
        color: #0056b3; 
    }
    h2, h1 {
        text-align: center;
    }
</style>

"""

# Generating HTML content for table data
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SQL Data</title>
    {css_styles}
</head>
<body>

<nav>
    <ul>{nav_links}</ul>
</nav>

<h1>Casino UdeM 2024</h1>

<div style="text-align: center;">
    <a href="requetes.html">Voir Requetes SQL</a>
</div>

"""

for table in tables:
    table_name = table[0]
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()

    html_content += f"<div id='{table_name}'><h2>{table_name}</h2>"
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
        html_content += "</tr>"
    html_content += "</table></div>"

html_content += "</body></html>"

# Saving HTML content to a file
with open("database_content.html", "w") as file:
    file.write(html_content)

print("HTML content saved to database_content.html")
