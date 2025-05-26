import sqlite3
import os

# Diretório para as bases de dados
DB_DIR = "/home/salithekid/Desktop/Projeto3Cadeiras/db"
os.makedirs(DB_DIR, exist_ok=True)

# Criar bases de dados para fragmentos (fragment1.db a fragment11.db)
for i in range(1, 12):
    db_path = os.path.join(DB_DIR, f"fragment{i}.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS fragments (
            file_id TEXT NOT NULL,
            serial_number INTEGER NOT NULL,
            data BLOB NOT NULL,
            user_id TEXT NOT NULL,
            PRIMARY KEY (file_id, serial_number)
        )
    """)
    conn.commit()
    conn.close()
    print(f"Created {db_path}")

# Criar base de dados para credenciais (credentials.db)
db_path = os.path.join(DB_DIR, "credentials.db")
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password_hash TEXT NOT NULL
    )
""")
c.execute("""
    CREATE TABLE IF NOT EXISTS file_metadata (
        file_id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        filename TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(username)
    )
""")
conn.commit()
conn.close()
print(f"Created {db_path}")
