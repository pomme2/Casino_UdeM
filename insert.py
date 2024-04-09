import pyodbc

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

cursor = cnxn.cursor()

# Insertion de données dans une table
insert_statement1 = "INSERT INTO jeu (id, nom, min_mise, max_mise) VALUES (?, ?, ?, ?)"
insert_statement2 = "INSERT INTO machine_de_jeu (id, date_service, id_jeu) VALUES (?, ?, ?)"
insert_statement3 = "INSERT INTO distributeur_de_jeton (id, nombre_jeton, date_service) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?, ?)"
insert_statement5 = "INSERT INTO camera_surveillance (id, secteur) VALUES (?, ?)"

# Fournir les valeurs pour l'insertion
data1 = (6, 'CASINOTESTINGLOL', 420453, 6969354)  # Replace these values with your actual data
data2 = (8, '2023-05-06', 6)

# Exécuter l'instruction d'insertion
cursor.execute(insert_statement1, data1)
cursor.execute(insert_statement2, data2)

# Validation de la transaction
cnxn.commit()

print("Data inserted successfully.")

cursor.close()
cnxn.close()
