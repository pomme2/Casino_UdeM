
# SQL Server DELETE T-SQL Example Using pyodbc (with no parameter)
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # SELECT Query Before DELETE 
    cursor.execute("SELECT * FROM tblCustomers")

    print("[Before DELETE...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)

    print()

    # DELETE Query
    print("[Deleting Record from Table...]")
    cursor.execute("DELETE FROM [tblCustomers] WHERE id=7")
    connection.commit()
    print("Done.")

    print()

    # SELECT Query After DELETE
    cursor.execute("SELECT * FROM tblCustomers")

    print("[After DELETE...]")
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