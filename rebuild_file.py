import sqlite3
import os

def rebuild_file(filename, output_path):
    """
    Reconstruct a file from fragments stored in fragment1.db to fragment11.db.
    Args:
        filename (str): Original filename to lookup file_id.
        output_path (str): Path to save the reconstructed file.
    Raises:
        Exception: If file_id not found or fragments missing.
    """
    # Find file_id from credentials.db
    try:
        conn = sqlite3.connect("/mnt/db/credentials.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT file_id FROM files WHERE filename = ?",
            (filename,)
        )
        result = cursor.fetchone()
        conn.close()

        if not result:
            raise Exception(f"File '{filename}' not found in database")
        file_id = result[0]

    except Exception as e:
        raise Exception(f"Failed to retrieve file_id: {str(e)}")

    # Collect fragments
    fragments = []
    db_paths = [f"/mnt/db/fragment{i}.db" for i in range(1, 12)]
    try:
        for i, db_path in enumerate(db_paths, 1):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT data FROM fragments WHERE file_id = ? AND serial_number = ?",
                (file_id, i)
            )
            result = cursor.fetchone()
            conn.close()

            if result:
                fragments.append(result[0])
            else:
                raise Exception(f"Fragment {i} missing for file_id {file_id}")

    except Exception as e:
        raise Exception(f"Failed to retrieve fragments: {str(e)}")

    # Reconstruct file
    try:
        with open(output_path, 'wb') as f:
            for fragment in fragments:
                f.write(fragment)
    except Exception as e:
        raise Exception(f"Failed to write reconstructed file: {str(e)}")

if __name__ == "__main__":
    # Example usage for testing
    try:
        rebuild_file("test.txt", "/app/test_reconstructed.txt")
        print("File reconstructed successfully")
    except Exception as e:
        print(f"Error: {str(e)}")
