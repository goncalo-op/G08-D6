import os
from databases import Database # Biblioteca fictícia para conexão com bases de dados

# Conexão com as bases de dados (exemplo)
fragment_dbs = [Database(f"postgresql://user:pass@db{i}:5432/fragments") for i in range(1, 11)]
credentials_db = Database("postgresql://user:pass@credentials-db:5432/credentials")
certificates_db = Database("postgresql://user:pass@certificates-db:5432/certificates")

async def upload_file(file_data, user_id):
    # Dividir o ficheiro em 10 fragmentos
    fragment_size = len(file_data) // 10
    fragments = [file_data[i:i + fragment_size] for i in range(0, len(file_data), fragment_size)]
    
    # Guardar cada fragmento numa base de dados diferente
    file_id = os.urandom(16).hex()  # ID único para o ficheiro
    for i, fragment in enumerate(fragments):
        serial_number = i + 1
        await fragment_dbs[i].execute(
            "INSERT INTO fragments (file_id, serial_number, data) VALUES (:file_id, :serial_number, :data)",
            {"file_id": file_id, "serial_number": serial_number, "data": fragment}
        )
    return file_id

async def download_file(file_id, user_id):
    # Recolher fragmentos
    fragments = []
    for i, db in enumerate(fragment_dbs):
        fragment = await db.fetch_one(
            "SELECT data FROM fragments WHERE file_id = :file_id AND serial_number = :serial_number",
            {"file_id": file_id, "serial_number": i + 1}
        )
        fragments.append(fragment["data"])
    
    # Reorganizar e devolver
    return b"".join(fragments)

# Exemplo de autenticação
async def authenticate(username, password):
    user = await credentials_db.fetch_one(
        "SELECT * FROM users WHERE username = :username AND password = :password",
        {"username": username, "password": password}  # Em produção, usa hash!
    )
    return user is not None