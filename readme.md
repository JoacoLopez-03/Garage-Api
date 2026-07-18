# 🚗 Garage API

API REST para la administración de vehículos personales: mantenimientos, historial, gastos y más. Desarrollada con **FastAPI** y **PostgreSQL**, pensada como proyecto de aprendizaje incremental — cada versión suma una capa nueva de complejidad (roles, tests, Docker, CI/CD, despliegue en la nube).

## 📌 Estado actual del proyecto

Este proyecto está en desarrollo activo. Funcionalidades implementadas hasta el momento:

- ✅ Registro y login de usuarios con autenticación **JWT**
- ✅ Catálogo de **Marcas** y **Modelos** (precargado vía seed)
- ✅ CRUD completo de **Vehículos**, asociados al usuario dueño
- ✅ CRUD completo de **Mantenimientos**, anidados a cada vehículo
- ✅ Arquitectura en capas (`models` / `schemas` / `routers` / `services`)
- ✅ Migraciones versionadas con **Alembic**

### 🔜 Próximos pasos

- [ ] Gastos y consumo de combustible
- [ ] Roles (Administrador / Usuario)
- [ ] Búsquedas y filtros avanzados
- [ ] Cálculo de próximos servicios y recordatorios
- [ ] Carga de fotos
- [ ] Tests automatizados (pytest)
- [ ] Dockerización
- [ ] CI/CD con GitHub Actions
- [ ] Despliegue en AWS
- [ ] Infraestructura como código (Terraform)
- [ ] Orquestación con Kubernetes
- [ ] Frontend en React con dashboard y gráficos

## 🛠️ Stack técnico

| Categoría | Tecnología |
|---|---|
| Lenguaje | Python 3.10 |
| Framework | FastAPI |
| Base de datos | PostgreSQL |
| ORM | SQLAlchemy |
| Migraciones | Alembic |
| Autenticación | JWT (python-jose) + bcrypt (passlib) |
| Validación de datos | Pydantic |

## 📂 Estructura del proyecto

```
Garage - Python y FastAPI/
├── alembic/                 # Migraciones de base de datos
├── app/
│   ├── core/                 # Seguridad (JWT, hashing) y dependencias
│   │   ├── security.py
│   │   └── dependencies.py
│   ├── database.py           # Configuración de conexión a PostgreSQL
│   ├── models/                # Modelos de SQLAlchemy (tablas)
│   ├── schemas/                # Esquemas de Pydantic (validación de entrada/salida)
│   ├── routers/                # Endpoints de la API, agrupados por entidad
│   ├── services/                # Lógica de negocio reutilizable
│   └── seed.py                 # Script de datos de prueba (marcas y modelos)
├── main.py                     # Punto de entrada de la aplicación
├── requirements.txt
├── .env.example                 # Plantilla de variables de entorno
└── .gitignore
```

## 🚀 Cómo correr el proyecto localmente

### Requisitos previos

- Python 3.10+
- PostgreSQL instalado y corriendo

### 1. Cloná el repositorio

```bash
git clone https://github.com/TU_USUARIO/garage-api.git
cd garage-api
```

### 2. Creá y activá un entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalá las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurá las variables de entorno

Copiá `.env.example` como `.env` y completá tus propios valores:

```bash
cp .env.example .env
```

```
DATABASE_URL=postgresql://usuario:password@localhost:5432/garage_db
SECRET_KEY=tu-clave-secreta-aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Para generar una `SECRET_KEY` segura:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Creá la base de datos

Desde `psql` o pgAdmin, creá una base llamada `garage_db` (o el nombre que hayas puesto en `DATABASE_URL`).

### 6. Aplicá las migraciones

```bash
alembic upgrade head
```

### 7. (Opcional) Cargá datos de prueba

```bash
python -m app.seed
```

Esto precarga algunas marcas y modelos de vehículos comunes.

### 8. Levantá el servidor

```bash
uvicorn main:app --reload
```

La API va a estar disponible en `http://127.0.0.1:8000`.

## 📖 Documentación interactiva

FastAPI genera documentación automática (Swagger UI), disponible en:

```
http://127.0.0.1:8000/docs
```

Ahí podés probar todos los endpoints sin necesidad de herramientas externas.

## 🔑 Autenticación

La API usa JWT. El flujo es:

1. `POST /auth/registro` → creás una cuenta
2. `POST /auth/login` → obtenés un `access_token`
3. En cada request a un endpoint protegido, mandá el header:
   ```
   Authorization: Bearer <access_token>
   ```

## 🧪 Probar la API

En la carpeta del proyecto vas a encontrar `Garage_API.postman_collection.json`, una colección de Postman lista para importar, con login automático (guarda el token solo) y todos los endpoints de Vehículos y Mantenimientos configurados.

## 📄 Licencia

Proyecto personal con fines educativos.