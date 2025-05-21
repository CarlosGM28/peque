import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# 📦 Configuración de la base de datos
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "pequepeques"
}

# 👤 Datos del usuario de prueba
username = "admin@senati.pe"
password_plano = "admin123"
rol = "admin"

# 🔐 Generar hash
hashed_password = generate_password_hash(password_plano, method='pbkdf2:sha256')

# 🧾 Mostrar hash generado
print("🔐 Hash generado:")
print(hashed_password)

# ✅ Verificar localmente
if check_password_hash(hashed_password, password_plano):
    print("✅ Verificación local correcta (el hash coincide con la contraseña)")
else:
    print("❌ Verificación local fallida (el hash no coincide con la contraseña)")

# 🧩 Insertar en la base de datos
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO usuarios (username, password, rol)
        VALUES (%s, %s, %s)
    """, (username, hashed_password, rol))
    conn.commit()
    print("✅ Usuario insertado correctamente.")
except mysql.connector.Error as err:
    print(f"❌ Error al insertar: {err}")
finally:
    if cursor: cursor.close()
    if conn: conn.close()
