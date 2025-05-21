from services.db_service import get_connection

def get_all_clientes():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def insert_cliente(nombre, dni, telefono, correo, procedencia, acompanantes):
    conn = get_connection()
    cursor = conn.cursor()
    query = '''INSERT INTO clientes (nombre, dni, telefono, correo, procedencia, acompanantes)
               VALUES (%s, %s, %s, %s, %s, %s)'''
    cursor.execute(query, (nombre, dni, telefono, correo, procedencia, acompanantes))
    conn.commit()
    cursor.close()
    conn.close()

def get_cliente_by_id(cliente_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (cliente_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def update_cliente(cliente_id, nombre, dni, telefono, correo, procedencia, acompanantes):
    conn = get_connection()
    cursor = conn.cursor()
    query = '''UPDATE clientes
               SET nombre=%s, dni=%s, telefono=%s, correo=%s, procedencia=%s, acompanantes=%s
               WHERE id=%s'''
    cursor.execute(query, (nombre, dni, telefono, correo, procedencia, acompanantes, cliente_id))
    conn.commit()
    cursor.close()
    conn.close()

def patch_cliente(cliente_id, campos):
    conn = get_connection()
    cursor = conn.cursor()
    keys = ", ".join([f"{k}=%s" for k in campos.keys()])
    values = list(campos.values()) + [cliente_id]
    query = f"UPDATE clientes SET {keys} WHERE id=%s"
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_servicios_por_cliente(cliente_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT s.id AS servicio_id, p.denominacion AS paquete, pp.nombre AS embarcacion, s.created_at
        FROM servicios s
        JOIN paquetes p ON s.paquete_id = p.id
        JOIN pequepeques pp ON s.pequepeque_id = pp.id
        WHERE s.cliente_id = %s
    """
    cursor.execute(query, (cliente_id,))
    servicios = cursor.fetchall()
    cursor.close()
    conn.close()
    return servicios

def tiene_servicios(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM servicios WHERE cliente_id = %s", (cliente_id,))
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count > 0
