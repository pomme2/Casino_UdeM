

# SQL Server SELECT T-SQL Example Using pyodbc (with parameter)
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # SELECT Query - With User Parameter
    # Set parameter value
    prmID=3

    # Execute query
    cursor.execute("SELECT * FROM tblCustomers WHERE id=?",prmID)

    print("[Query Results...]")
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
