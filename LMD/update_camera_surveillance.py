import pyodbc

def update_data_camera_surveillance(secteur, id):
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

    sqlCommand = "UPDATE camera_surveillance SET secteur=? WHERE id=?;"

    data = (secteur, id)

    cursor.execute(sqlCommand, data)

    cnxn.commit()

    print("Data updated successfully.")

    cursor.close()
    cnxn.close()

