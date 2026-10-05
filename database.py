import sqlite3

def execute_query(query):
    # VULNERABLE TO SQL INJECTION
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor.execute(query) # INTENTIONAL: Executing raw query string
    results = cursor.fetchall()
    conn.close()
    return str(results)
