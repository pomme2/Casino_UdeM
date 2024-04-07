
# Call a SQL Server Stored Procedure Using pyodbc which does not return any results
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand="""CREATE PROCEDURE uspCusDetailsUpdate (@cusID int)
    AS 
    UPDATE tblCustomers SET lastName=lastName+' - Updated from SP' where id=@cusID
    """

    # Create Stored Procedure
    cursor.execute(sqlCommand)
    connection.commit()

    print()

    sqlCommand2="""
    EXEC dbo.uspCusDetailsUpdate @cusID=?;
    """

    # Set the parameter value
    prmCusID=2

    # Call Stored Procedure
    cursor.execute(sqlCommand2,prmCusID)
    connection.commit()

    # SELECT Query After Stored Procedure Call - Check table contents
    cursor.execute("SELECT * FROM tblCustomers")

    print("[After SP Call...]")
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