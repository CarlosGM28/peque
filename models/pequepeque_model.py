from services.db_service import get_connection

def get_all_pequepeques():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT pq.id,
               pq.matricula,
               pq.nombre,
               pq.capacidad,
               pq.material,
               pq.color,
               pq.propietario_id,
               pr.nombres AS propietario_nombre,
               pr.dni AS propietario_dni
        FROM pequepeques pq
        JOIN propietarios pr ON pq.propietario_id = pr.id
    """)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def get_pequepeque_by_id(pequepeque_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pequepeques WHERE id = %s", (pequepeque_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_pequepeque(data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pequepeques (matricula, nombre, capacidad, material, fecha_registro, fecha_inicio, color, propietario_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data['matricula'], data['nombre'], data['capacidad'],
        data['material'], data['fecha_registro'], data['fecha_inicio'],
        data['color'], data['propietario_id']
    ))
    conn.commit()
    cursor.close()
    conn.close()

def update_pequepeque(pequepeque_id, data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE pequepeques
        SET matricula=%s, nombre=%s, capacidad=%s, material=%s,
            fecha_registro=%s, fecha_inicio=%s, color=%s, propietario_id=%s
        WHERE id=%s
    """, (
        data['matricula'], data['nombre'], data['capacidad'],
        data['material'], data['fecha_registro'], data['fecha_inicio'],
        data['color'], data['propietario_id'], pequepeque_id
    ))
    conn.commit()
    cursor.close()
    conn.close()

def patch_pequepeque(pequepeque_id, campos):
    conn = get_connection()
    cursor = conn.cursor()
    keys = ", ".join([f"{k}=%s" for k in campos.keys()])
    values = list(campos.values()) + [pequepeque_id]
    query = f"UPDATE pequepeques SET {keys} WHERE id=%s"
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_pequepeque(pequepeque_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pequepeques WHERE id = %s", (pequepeque_id,))
    conn.commit()
    cursor.close()
    conn.close()
