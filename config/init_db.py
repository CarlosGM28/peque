import mysql.connector
from config.config import config

def init_db():
    conn = mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS propietarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombres VARCHAR(100) NOT NULL,
        dni CHAR(8) NOT NULL UNIQUE,
        telefono VARCHAR(12),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pequepeques (
        id INT AUTO_INCREMENT PRIMARY KEY,
        matricula VARCHAR(20) NOT NULL UNIQUE,
        nombre VARCHAR(100),
        capacidad INT,
        material VARCHAR(30) NOT NULL,
        fecha_registro DATE,
        fecha_inicio DATE,
        color VARCHAR(30),
        propietario_id INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (propietario_id) REFERENCES propietarios(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS paquetes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        denominacion VARCHAR(100) NOT NULL,
        precio FLOAT NOT NULL,
        tiempo_promedio VARCHAR(50),
        paradas INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        dni CHAR(8) NOT NULL UNIQUE,
        telefono VARCHAR(15),
        correo VARCHAR(100),
        procedencia VARCHAR(20) NOT NULL,
        acompanantes INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cliente_id INT NOT NULL,
        paquete_id INT NOT NULL,
        pequepeque_id INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (paquete_id) REFERENCES paquetes(id),
        FOREIGN KEY (pequepeque_id) REFERENCES pequepeques(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        rol VARCHAR(30),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("Base de datos inicializada correctamente.")
