import pyodbc

def update_data(nom, id):
    # Connection string to SQL Server database
    conn_str = (
        "Driver=ODBC Driver 17 for SQL Server;"
        "Server=localhost;"
        "Database=projdb;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Trusted_Connection=yes;"
    )
    
    # Establishing a connection to the database
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()

    # SQL command to update data in the 'jeu' table
    sqlCommand = "UPDATE jeu SET nom=? WHERE id=?;"

    # Data to be provided during execution
    data = (nom, id)

    # Replace the "?" placeholders with the values provided
    cursor.execute(sqlCommand, data)

    # Committing the transaction
    cnxn.commit()

    print("Data updated successfully.")

    cursor.close()
    cnxn.close()

