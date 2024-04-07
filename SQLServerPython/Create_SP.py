
# Create a SQL Server Stored Procedure Using pyodbc
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand="""CREATE PROCEDURE uspCusDetails (@cusID int, @out nvarchar(max) OUTPUT)
    AS 
    SELECT * FROM tblCustomers where id=@cusID
    """

    # Create Stored Procedure
    cursor.execute(sqlCommand)
    connection.commit()

    print("Stored procedure successfully created.")

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