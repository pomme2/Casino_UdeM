
# Call SQL Server System Functions Using pyodbc and display the results
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()


    # System Function 1 - HOST_NAME
    cursor.execute("SELECT HOST_NAME () as HostName")

    print("[System Function 1 - HOST_NAME - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("HostName: ", row.HostName)

    print()

    # System Function 2 - DB_NAME
    cursor.execute("SELECT DB_NAME() as CurrentDBName")

    print("[System Function 2 - DB_NAME - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Current Database Name: ",row.CurrentDBName)

    print()

    # System Function 3 - ISNUMERIC
    prmIsNumeric="20"
    cursor.execute("SELECT ISNUMERIC (?) as IsNumericValue",prmIsNumeric)

    print("[System Function 3 - ISNUMERIC - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Checking if [",prmIsNumeric,"] is numeric. Check Result (0-False / 1-True): ",row.IsNumericValue)

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