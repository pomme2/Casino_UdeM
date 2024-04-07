# SQL Server UPDATE T-SQL Example Using pyodbc
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # SELECT Query Before UPDATE
    cursor.execute("SELECT * FROM tblCustomers")

    print("[Before UPDATE...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)

    print()

    # UPDATE Query - No User Parameter
    print("[Updating Table...]")
    cursor.execute("UPDATE tblCustomers SET lastName='lastName 5 New' where id=5")
    connection.commit()
    print("Done.")

    print()

    # SELECT Query After UPDATE
    cursor.execute("SELECT * FROM tblCustomers")

    print("[After UPDATE...]")
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