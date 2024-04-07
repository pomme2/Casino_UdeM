# SQL Server INSERT T-SQL Example Using pyodbc (with parameter)
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # SELECT Query Before INSERT
    cursor.execute("SELECT * FROM tblCustomers")

    print("[Before INSERT...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.id,row.code,row.firstName,row.lastName)

    print()

    # INSERT Query - With User Parameter
    # Set the parameter values
    prmID=7
    prmCode="code7"
    prmFirstName="firstName7"
    prmLastName="lastName7"

    print("[Inserting Record to Table...]")
    cursor.execute("INSERT INTO [tblCustomers] ([id],[code],[firstName],[lastName]) VALUES (?,?,?,?)",(prmID,prmCode,prmFirstName,prmLastName))
    connection.commit()
    print("Done.")

    print()

    # SELECT Query After INSERT
    cursor.execute("SELECT * FROM tblCustomers")

    print("[After INSERT...]")
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