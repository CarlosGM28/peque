from services.db_service import get_connection

def get_all_servicios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.id,
               s.created_at,
               
               c.id AS cliente_id,
               c.nombre AS cliente_nombre,
               c.dni AS cliente_dni,
               c.telefono AS cliente_telefono,
               c.correo AS cliente_correo,
               c.procedencia AS cliente_procedencia,
               c.acompanantes AS cliente_acompanantes,

               p.id AS paquete_id,
               p.denominacion AS paquete_denominacion,
               p.precio AS paquete_precio,
               p.tiempo_promedio AS paquete_duracion,
               p.paradas AS paquete_paradas,

               pq.id AS pequepeque_id,
               pq.nombre AS pequepeque_nombre,
               pq.matricula AS pequepeque_matricula,
               pq.capacidad AS pequepeque_capacidad,
               pq.material AS pequepeque_material,
               pq.color AS pequepeque_color

        FROM servicios s
        JOIN clientes c ON s.cliente_id = c.id
        JOIN paquetes p ON s.paquete_id = p.id
        JOIN pequepeques pq ON s.pequepeque_id = pq.id
        ORDER BY s.created_at DESC
    """)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_servicio_by_id(servicio_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM servicios WHERE id = %s", (servicio_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_servicio(cliente_id, paquete_id, pequepeque_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO servicios (cliente_id, paquete_id, pequepeque_id)
        VALUES (%s, %s, %s)
    """, (cliente_id, paquete_id, pequepeque_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_servicio(servicio_id, cliente_id, paquete_id, pequepeque_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE servicios
        SET cliente_id=%s, paquete_id=%s, pequepeque_id=%s
        WHERE id=%s
    """, (cliente_id, paquete_id, pequepeque_id, servicio_id))
    conn.commit()
    cursor.close()
    conn.close()

def patch_servicio(servicio_id, campos):
    conn = get_connection()
    cursor = conn.cursor()
    keys = ", ".join([f"{k}=%s" for k in campos.keys()])
    values = list(campos.values()) + [servicio_id]
    query = f"UPDATE servicios SET {keys} WHERE id=%s"
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_servicio(servicio_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM servicios WHERE id = %s", (servicio_id,))
    conn.commit()
    cursor.close()
    conn.close()
