import pyodbc

def insert_data_panneau_affichage(id, marque, longueur, largeur):
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

    # Check if the record with the same id already exists
    cursor.execute("SELECT COUNT(*) FROM panneau_affichage WHERE id = ?", (id,))
    if cursor.fetchone()[0] > 0:
        print(f"A record with ID {id} already exists in the 'panneau_affichage' table.")
        # Optionally, handle the duplicate record scenario here
        return

    # Insertion de données dans la table jeu
    insert_statement = "INSERT INTO panneau_affichage (id, marque, longueur, largeur) VALUES (?, ?, ?, ?)"

    # Fournir les valeurs pour l'insertion
    data = (id, marque, longueur, largeur)
    #data1 = (6, "Apple", 400, 20)

    # Exécuter l'instruction d'insertion
    cursor.execute(insert_statement, data)
    #cursor.execute(insert_statement, data1)

    # Validation de la transaction
    cnxn.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnxn.close()

