import sqlite3
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
DATABASE = 'clients.db'

def init_db():
    """Initialize the database with sample data."""
    if os.path.exists(DATABASE):
        os.remove(DATABASE)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create clients table
    cursor.execute('''
        CREATE TABLE clients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            account_type TEXT
        )
    ''')

    # Create flags table (secret data)
    cursor.execute('''
        CREATE TABLE flags (
            id INTEGER PRIMARY KEY,
            flag_text TEXT
        )
    ''')

    # Insert sample client data
    clients = [
        ('Google LLC', 'contact@google.com', 'Premium'),
        ('Amazon Inc', 'info@amazon.com', 'Premium'),
        ('Microsoft Corp', 'support@microsoft.com', 'Standard'),
        ('Apple Inc', 'business@apple.com', 'Premium'),
        ('Meta Platforms', 'enterprise@meta.com', 'Standard'),
    ]

    for client in clients:
        cursor.execute('INSERT INTO clients (name, email, account_type) VALUES (?, ?, ?)', client)

    # Insert the flag (secret data that shouldn't be easily accessible)
    cursor.execute('INSERT INTO flags (flag_text) VALUES (?)',
                   ('flag{SQL_Injection_Is_Dangerous_m10dd}',))

    conn.commit()
    conn.close()

def get_db():
    """Get a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page with the lookup form."""
    result = None
    query_text = ""

    if request.method == 'POST':
        query_text = request.form.get('query', '')

        if query_text:
            try:
                conn = get_db()
                cursor = conn.cursor()

                # VULNERABLE: Direct string concatenation without parameterization
                # This allows SQL injection attacks
                sql_query = f"SELECT * FROM clients WHERE name LIKE '%{query_text}%' OR email LIKE '%{query_text}%'"

                cursor.execute(sql_query)
                rows = cursor.fetchall()

                if rows:
                    result = []
                    for row in rows:
                        result.append({
                            'id': row['id'],
                            'name': row['name'],
                            'email': row['email'],
                            'account_type': row['account_type']
                        })
                else:
                    result = []

                conn.close()
            except Exception as e:
                result = [{'error': str(e)}]

    return render_template('index.html', result=result, query=query_text)

@app.route('/flag', methods=['GET'])
def flag():
    """Endpoint containing the flag (accessible via SQL injection)."""
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute('SELECT flag_text FROM flags LIMIT 1')
        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify({'flag': row['flag_text']})
        return jsonify({'error': 'No flag found'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
