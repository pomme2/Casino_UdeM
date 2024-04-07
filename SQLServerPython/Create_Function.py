
# Create a SQL Server User-Defined Function Using pyodbc
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand="""CREATE FUNCTION ufnGetCusCode(@cusID int)
    RETURNS VARCHAR(50)
    AS
    BEGIN
    DECLARE @cusCode VARCHAR(50)
    SET @cusCode = (SELECT code from tblCustomers where id=@cusID)
    
    RETURN @cusCode

    END;
    """

    # Create Function
    cursor.execute(sqlCommand)
    connection.commit()

    print("User-defined function created.")

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