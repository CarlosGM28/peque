# Sistema de Gestión Turística

Este sistema fue desarrollado en **Python con Flask** y MySQL. Aquí tienes todos los pasos para ejecutarlo correctamente en un nuevo entorno.

---

## 📦 Requisitos

- Python 3.9 o superior
- MySQL Server
- pip

---

## ⚙️ Instalación

1. **Clona el proyecto**

```bash
git clone <URL-del-repositorio>
cd nombre-del-proyecto
```

2. **Crea un entorno virtual (opcional pero recomendado)**

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

4. **Configura tu archivo `.env`** (crea uno en la raíz)

```env
FLASK_ENV=development
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_de_tu_base_de_datos
SECRET_KEY=una_clave_secreta_para_flask
```

5. **Inicializa la base de datos**

Crea la base de datos en MySQL con las tablas necesarias. Puedes usar un script SQL si fue proporcionado.

---

## 🚀 Ejecutar el sistema

```bash
python app.py
```

Luego accede en tu navegador a:

```
http://127.0.0.1:5000/login
```

---

## 👤 Credenciales de acceso (por defecto)

- Usuario: `admin@example.com`
- Contraseña: `123456`

> Estos valores pueden variar, asegúrate de crearlos manualmente si no hay datos precargados.

---

## 🛠 Funcionalidades

- CRUD de Clientes, Propietarios, Pequepeques, Paquetes, Servicios, Usuarios.
- Login con sesión y control de roles.
- UI con Bootstrap + Select2 + DataTables + SweetAlert2.
- Código modular y organizado por Blueprint.

---

## 📁 Estructura de Carpetas

```
├── app.py
├── requirements.txt
├── .env
├── templates/
│   ├── dashboard/
│   └── vistas/
├── static/
├── controllers/
├── services/
└── models/
```

---

## 👨‍💻 Desarrollador

> Para cualquier duda, contacta al equipo técnico.