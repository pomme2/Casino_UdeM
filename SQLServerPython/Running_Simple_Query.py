# Running a Simple SQL Server Query
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    cursor.execute("SELECT @@VERSION as version")

    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.version)

    cursor.close()
    connection.close()

except pyodbc.Error as ex:
    print()
    print("Exception: ",ex)
    cursor.close()
    connection.close()
    print("Closing program...")
    print()
    exit()

print()