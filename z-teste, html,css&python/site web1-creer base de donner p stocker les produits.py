import sqlite3

conn = sqlite3.connect('boutique.db')
cursor = conn.cursor()

# Créez une table pour stocker les produits
cursor.execute('''
    CREATE TABLE produits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT,
        description TEXT,
        prix REAL,
        quantite INTEGER
    )
''')

conn.commit()
conn.close()
