# Call a SQL Server Stored Procedure Using pyodbc and display the results
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    sqlCommand="""
    DECLARE @out nvarchar(max);
    EXEC dbo.uspCusDetails @cusID=?, @out = @out OUTPUT;
    """

    prmCusID=4

    # Call the Stored Procedure
    cursor.execute(sqlCommand,prmCusID)

    print("[Stored Procedure Call Results...]")
    rows=cursor.fetchall()

    # Display the results
    while rows:
        print(rows)
        if cursor.nextset():
            rows =cursor.fetchall()
        else:
            rows = None

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