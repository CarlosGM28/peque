from services.db_service import get_connection

def get_all_paquetes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM paquetes")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_paquete_by_id(paquete_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM paquetes WHERE id = %s", (paquete_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_paquete(denominacion, precio, tiempo_promedio, paradas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO paquetes (denominacion, precio, tiempo_promedio, paradas)
        VALUES (%s, %s, %s, %s)
    """, (denominacion, precio, tiempo_promedio, paradas))
    conn.commit()
    cursor.close()
    conn.close()

def update_paquete(paquete_id, denominacion, precio, tiempo_promedio, paradas):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE paquetes
        SET denominacion=%s, precio=%s, tiempo_promedio=%s, paradas=%s
        WHERE id=%s
    """, (denominacion, precio, tiempo_promedio, paradas, paquete_id))
    conn.commit()
    cursor.close()
    conn.close()

def patch_paquete(paquete_id, campos):
    conn = get_connection()
    cursor = conn.cursor()
    keys = ", ".join([f"{k}=%s" for k in campos.keys()])
    values = list(campos.values()) + [paquete_id]
    query = f"UPDATE paquetes SET {keys} WHERE id=%s"
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_paquete(paquete_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM paquetes WHERE id = %s", (paquete_id,))
    conn.commit()
    cursor.close()
    conn.close()
