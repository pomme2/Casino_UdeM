# SQL Server Other T-SQL Query Examples Using pyodbc
import pyodbc

print()

# Exception Handling
try:

    # Trusted Connection to Named Instance 
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PROF-KKILANI;DATABASE=SampleDB;Trusted_Connection=yes;')

    cursor=connection.cursor()

    # Query 1 - Aggregation: COUNT
    cursor.execute("SELECT COUNT(*) AS TotalRecords FROM [SampleDB].[dbo].[tblCustomers]")

    print("[Query 1 - Aggregation by COUNT - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print("Total Records: ", row.TotalRecords)

    print()

    # Query 2 - System Global Variable: @@SERVERNAME
    cursor.execute("SELECT @@SERVERNAME as serverName")

    print("[Query 2 - ystem Global Variable: @@SERVERNAME - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.serverName)

    print()

    # Query 3 - Dynamic Management Views (DMVs): sys.dm_os_wait_stats 
    cursor.execute("SELECT TOP 10 wait_type, wait_time_ms FROM sys.dm_os_wait_stats where wait_time_ms>5 ORDER BY 2 DESC")

    print("[Query 3 - Dynamic Management Views (DMVs): sys.dm_os_wait_stats - Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.wait_type,row.wait_time_ms)

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