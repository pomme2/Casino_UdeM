import pyodbc

def delete_row(table_name, row_id):
    # Connexion à la base de données
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

    # Instruction SQL pour supprimer une ligne
    delete_statement = f"DELETE FROM {table_name} WHERE id = ?"

    cursor.execute(delete_statement, (row_id,))
    cnxn.commit()  
    
    print(f"Row with ID {row_id} was successfully deleted from table {table_name}.")

    cnxn.close()