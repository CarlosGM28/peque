from services.db_service import get_connection
from werkzeug.security import check_password_hash, generate_password_hash

def get_all_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_usuario_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def get_usuario_by_username(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_usuario(username, password, rol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (username, password, rol) VALUES (%s, %s, %s)", (username, password, rol))
    conn.commit()
    cursor.close()
    conn.close()

def update_usuario(user_id, username, password, rol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE usuarios SET username=%s, password=%s, rol=%s WHERE id=%s
    """, (username, password, rol, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def patch_usuario(user_id, campos):
    conn = get_connection()
    cursor = conn.cursor()
    keys = ", ".join([f"{k}=%s" for k in campos.keys()])
    values = list(campos.values()) + [user_id]
    query = f"UPDATE usuarios SET {keys} WHERE id=%s"
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def delete_usuario(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

def validar_credenciales(username, password):
    conn = get_connection()
    c = conn.cursor(dictionary=True)
    c.execute('''
        SELECT * FROM usuarios WHERE username = %s
    ''', (username,))
    usuario = c.fetchone()
    c.close()
    conn.close()

    if usuario and check_password_hash(usuario['password'], password):
        usuario.pop('password') 
        return usuario
    return None
