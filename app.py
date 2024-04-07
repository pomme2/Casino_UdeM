from flask import Flask, request, jsonify
import pyodbc

app = Flask(__name__)

@app.route('/delete-row', methods=['POST'])
def delete_row():
    data = request.json
    table_name = data['table_name']
    row_id = data['row_id']

    conn_str = (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"
        "Database=projdb;"
        "TrustServerCertificate=yes;"  # Only for testing environments
        "Trusted_Connection=yes;"
    )
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    query = f"DELETE FROM {table_name} WHERE id=?"
    cursor.execute(query, row_id)
    cnxn.commit()

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)