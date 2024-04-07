
# Call a User-Defined Function Using pyodbc and display the results
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # Set the T-SQL statement
    sqlCommand="SELECT dbo.ufnGetCusCode(?) as CusCode"

    # Set the parameter value
    prmCusID=2

    # Execute query - Call User-Defined Function
    cursor.execute(sqlCommand,prmCusID)

    print("[User-Defined Function Call Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Customer Code for ID:",prmCusID,"-",row.CusCode)

    print()

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