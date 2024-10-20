import pyodbc # type: ignore
from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

# SQL Server connection string
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server_name;'
        'DATABASE=your_database_name;'
        'UID=your_username;'
        'PWD=your_password;'
    )
    return conn

@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Items")  # Adjust table name as necessary
    rows = cursor.fetchall()
    items = [{'id': row[0], 'name': row[1], 'description': row[2]} for row in rows]
    conn.close()
    return jsonify(items), 200

if __name__ == '__main__':
    app.run(debug=True)
