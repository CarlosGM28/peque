from services.db_service import get_connection

def get_all_propietarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM propietarios")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_propietario_by_id(propietario_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM propietarios WHERE id = %s", (propietario_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_propietario(nombres, dni, telefono):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO propietarios (nombres, dni, telefono)
        VALUES (%s, %s, %s)
    """, (nombres, dni, telefono))
    conn.commit()
    cursor.close()
    conn.close()

def update_propietario(propietario_id, nombres, dni, telefono):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE propietarios
        SET nombres=%s, dni=%s, telefono=%s
        WHERE id=%s
    """, (nombres, dni, telefono, propietario_id))
    conn.commit()
    cursor.close()
    conn.close()

def patch_propietario(propietario_id, campos):
    conn = get_connection()
    cursor = conn.cursor()
    keys = ", ".join([f"{k}=%s" for k in campos.keys()])
    values = list(campos.values()) + [propietario_id]
    query = f"UPDATE propietarios SET {keys} WHERE id=%s"
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_propietario(propietario_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM propietarios WHERE id = %s", (propietario_id,))
    conn.commit()
    cursor.close()
    conn.close()
