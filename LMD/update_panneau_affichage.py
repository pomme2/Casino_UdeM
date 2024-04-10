import pyodbc

def update_data_panneau_affichage(marque, id):
    # Connection string to SQL Server database
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

    sqlCommand = "UPDATE panneau_affichage SET marque=? WHERE id=?;"

    data = (marque, id)

    cursor.execute(sqlCommand, data)

    cnxn.commit()

    print("Data updated successfully.")

    cursor.close()
    cnxn.close()

