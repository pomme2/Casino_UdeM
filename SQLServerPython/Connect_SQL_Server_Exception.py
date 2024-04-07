import pyodbc

# Exception Handling
try:

    # Trusted Connection to Named Instance
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    print()
    print("Successfully connected to SQL Server.")
    print()

    cursor.close()
    connection.close()

except pyodbc.Error as ex:
    print()
    print("Exception: ",ex)    
    print("Closing program...")
    print()
    exit()

print()