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

# Creating a cursor object
cursor = cnxn.cursor()

# Inserting data into a table
insert_statement1 = "INSERT INTO jeu (id, nom, min_mise, max_mise) VALUES (?, ?, ?, ?)"
insert_statement2 = "INSERT INTO machine_de_jeu (id, date_service, id_jeu) VALUES (?, ?, ?)"
insert_statement3 = "INSERT INTO distributeur_de_jeton (id, nombre_jeton, date_service) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement5 = "INSERT INTO camera_surveillance (id, secteur) VALUES (?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
insert_statement4 = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?)"
# Replace YourTableName with the actual table name and Column1, Column2, Column3 with actual column names



# Providing values for insertion
data1 = (6, 'CASINOTESTINGLOL', 420453, 6969354)  # Replace these values with your actual data
data2 = (8, '2023-05-06', 6)

# Executing the insert statement
cursor.execute(insert_statement1, data1)
cursor.execute(insert_statement2, data2)
#cursor.execute(insert_statement3, data)
#cursor.execute(insert_statement4, data)
#cursor.execute(insert_statement5, data)

# Committing the transaction
cnxn.commit()

print("Data inserted successfully.")

# Don't forget to close the cursor and connection when you're done
cursor.close()
cnxn.close()
