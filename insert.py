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

# Inserting data into a table
insert_statement = "INSERT INTO JEU (id, nom, min_mise, max_mise) VALUES (?, ?, ? , ?)"
# Replace YourTableName with the actual table name and Column1, Column2, Column3 with actual column names

# Providing values for insertion
data = (6, 'CASINOTESTING', 420,6969)  # Replace these values with your actual data

# Executing the insert statement
cursor.execute(insert_statement, data)

# Committing the transaction
cnxn.commit()

print("Data inserted successfully.")

# Don't forget to close the cursor and connection when you're done
cursor.close()
cnxn.close()
