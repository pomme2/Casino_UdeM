
# SQL Server SELECT T-SQL Example Using pyodbc (with no parameter)
import pyodbc

print()

# Exception Handling
try:
    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # SELECT Query - No User Parameter
    # Execute query
    cursor.execute("SELECT * FROM tblCustomers")

    print("[Query 1 Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)

    cursor.close()
    connection.close()    

except pyodbc.Error as ex:
    print("Exception: ",ex)
    cursor.close()
    connection.close()
    print("Closing program...")
    print()
    exit()

print()


