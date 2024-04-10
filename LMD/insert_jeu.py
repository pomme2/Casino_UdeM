import pyodbc

def insert_data_jeu(id, nom, min_mise, max_mise):
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

    cursor.execute("SELECT COUNT(*) FROM jeu WHERE id = ?", (id,))
    if cursor.fetchone()[0] > 0:
        print(f"A record with ID {id} already exists in the 'jeu' table.")
        return

    # Insertion de données dans la table jeu
    insert_statement = "INSERT INTO jeu (id, nom, min_mise, max_mise) VALUES (?, ?, ?, ?)"

    # Fournir les valeurs pour l'insertion
    data = (id, nom, min_mise, max_mise)

    # Exécuter l'instruction d'insertion
    cursor.execute(insert_statement, data)

    # Validation de la transaction
    cnxn.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnxn.close()

# Example usage of the method

