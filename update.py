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

# les 2 "?" Représente une valeur à fournir durant l'exécution
sqlCommand = "update jeu set nom=? where id=?;"

data = ("Poker", 3)
# ces 2 "?" Seront remplacés par les valeurs pthon et 10
cursor.execute(sqlCommand, data)

# Committing the transaction
cnxn.commit()

print("Data modified successfully.")

cursor.close()
cnxn.close()

