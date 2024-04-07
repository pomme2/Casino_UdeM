import pyodbc

# Establishing a connection to the database
conn_str = (
    "Driver=ODBC Driver 17 for SQL Server;"
    "Server=localhost;"
    "Database=projdb;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
    "Trusted_Connection=yes;"
)
cnxn = pyodbc.connect(conn_str)

# Creating a cursor object
cursor = cnxn.cursor()

# Deleting data from the table
delete_statement1 = "DELETE FROM Jeu WHERE id = ?"
delete_statement2 = "DELETE FROM Machine_de_jeu WHERE id = ?"
# Replace 'id' with the primary key or the column you want to use as the condition

# Providing the value for the condition
data2 = (8,)
data1 = (6,)  # Replace this value with the actual value you want to delete

# Executing the delete statement
cursor.execute(delete_statement1, data1)

# Committing the transaction
cnxn.commit()

print("Data deleted successfully.")

# Don't forget to close the cursor and connection when you're done
cursor.close()
cnxn.close()
