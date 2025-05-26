import sqlite3
import os
import uuid
import math

def main(file_path):
    """
    Split a file into 11 fragments and store in fragment1.db to fragment11.db.
    Args:
        file_path (str): Path to the file to split.
    Returns:
        dict: {'file_id': str, 'filename': str} on success, raises Exception on failure.
    """
    # Generate unique file_id
    file_id = str(uuid.uuid4())
    filename = os.path.basename(file_path)

    # Read file content
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()
    except Exception as e:
        raise Exception(f"Failed to read file: {str(e)}")

    file_size = len(file_data)
    if file_size == 0:
        raise Exception("File is empty")

    # Calculate fragment size (ceiling division for equal parts)
    num_fragments = 11
    fragment_size = math.ceil(file_size / num_fragments)

    # Connect to databases
    db_paths = [f"/mnt/db/fragment{i}.db" for i in range(1, 12)]
    try:
        for i in range(num_fragments):
            # Extract fragment data
            start = i * fragment_size
            end = min((i + 1) * fragment_size, file_size)
            fragment_data = file_data[start:end]

            # Connect to fragment database
            conn = sqlite3.connect(db_paths[i])
            cursor = conn.cursor()

            # Ensure fragments table exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS fragments (
                    file_id TEXT,
                    serial_number INTEGER,
                    data BLOB,
                    PRIMARY KEY (file_id, serial_number)
                )
            """)

            # Insert fragment
            cursor.execute(
                "INSERT INTO fragments (file_id, serial_number, data) VALUES (?, ?, ?)",
                (file_id, i + 1, fragment_data)
            )

            conn.commit()
            conn.close()

        # Store metadata in credentials.db (optional, adjust as needed)
        conn = sqlite3.connect("/mnt/db/credentials.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                file_id TEXT PRIMARY KEY,
                filename TEXT
            )
        """)
        cursor.execute(
            "INSERT INTO files (file_id, filename) VALUES (?, ?)",
            (file_id, filename)
        )
        conn.commit()
        conn.close()

        return {"file_id": file_id, "filename": filename}

    except Exception as e:
        raise Exception(f"Failed to store fragments: {str(e)}")

if __name__ == "__main__":
    # Example usage for testing
    try:
        result = main("/app/Uploads/test.txt")
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")
