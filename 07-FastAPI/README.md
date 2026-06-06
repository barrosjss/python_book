# Apuntes del Profe — Introducción a FastAPI

> Notas de referencia rápida para clase. Cubre preguntas difíciles, analogías y profundidad técnica.

---

## La pregunta más frecuente: ¿Qué es Uvicorn?

Esta es **la** pregunta que más sale cuando ven `uvicorn main:app --reload`. Aquí la explicación completa:

### La respuesta corta (para en clase)
> "FastAPI sabe cómo construir una API, pero no sabe cómo escuchar en un puerto de red. Uvicorn es el que abre el puerto, recibe los paquetes HTTP que llegan, y se los pasa a FastAPI. FastAPI procesa y responde. Es separación de responsabilidades: cada uno hace su trabajo."

### La respuesta larga (por si insisten)

**El problema de fondo:**

Python, por sí solo, no puede recibir peticiones HTTP. Necesitas algo que:
1. Abra un socket en el puerto 8000
2. Escuche conexiones TCP entrantes
3. Reciba bytes crudos de la red
4. Convierta esos bytes en un objeto Python que tu código pueda entender
5. Cuando tu código responda, convierta la respuesta de vuelta a bytes y la mande por la red

Eso es lo que hace **Uvicorn**.

**WSGI vs ASGI (sin entrar en detalles):**

```
Flask/Django  →  usa  →  Gunicorn/uWSGI  →  WSGI
FastAPI       →  usa  →  Uvicorn         →  ASGI
```

- **WSGI** (Web Server Gateway Interface): el estándar viejo (2003). Sincrónico, un request a la vez por worker.
- **ASGI** (Asynchronous Server Gateway Interface): el estándar moderno (2019). Asíncrono, puede manejar miles de conexiones concurrentes.

FastAPI usa ASGI porque está construido sobre `async/await` de Python, lo que le da su velocidad.

**Uvicorn = Uber-fast + ASGI:**
El nombre viene de "Uvicorn" → "μvicorn" → la letra griega μ (micro) + "vicorn" (de ASGI). Es literalmente "micro-ASGI".

**El flag `--reload`:**
En producción nunca usarías `--reload`. En producción:
```bash
uvicorn main:app --workers 4 --host 0.0.0.0 --port 8000
```
- `--workers 4` → 4 procesos en paralelo (usa todos los núcleos del CPU)
- `--host 0.0.0.0` → acepta conexiones de cualquier IP (no solo localhost)
- Sin `--reload` → más eficiente

---

## Conceptos técnicos profundos

### ¿Por qué FastAPI es "rápido"?

Tres razones:

1. **ASGI + async/await**: puede manejar miles de peticiones simultáneas sin bloquear. Mientras espera la respuesta de una base de datos, atiende otra petición.

2. **Pydantic v2**: la validación de datos está escrita en Rust (no Python), lo que la hace extremadamente rápida.

3. **Sin overhead**: FastAPI no tiene capas innecesarias. Flask tiene middleware acumulado de décadas. FastAPI nació limpio.

**Benchmark** (aproximado, varía según hardware):
- Flask: ~3,000 req/seg
- FastAPI: ~40,000-80,000 req/seg
- Go/Node.js: ~100,000+ req/seg

Para el 99% de proyectos, la velocidad de Flask es más que suficiente. FastAPI brilla en microservicios que reciben millones de requests por día.

### ¿Qué son los type hints de Python?

Los type hints son anotaciones que indican el tipo esperado de una variable. FastAPI los usa para todo:

```python
# Sin type hints (Python clásico)
def saludar(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años"

# Con type hints (Python 3.5+)
def saludar(nombre: str, edad: int) -> str:
    return f"Hola {nombre}, tienes {edad} años"
```

Python **no enforcea** los type hints en tiempo de ejecución por defecto. Son "sugerencias". FastAPI, sin embargo, sí los usa activamente: cuando declara un parámetro como `int`, FastAPI intenta convertir el valor de la URL a `int` y falla con 422 si no puede.

### ¿Qué es Pydantic por dentro?

Pydantic toma un `dict` de Python y lo valida/transforma contra un modelo:

```python
from pydantic import BaseModel

class Estudiante(BaseModel):
    nombre: str
    semestre: int

# Pydantic acepta strings y los convierte a int si puede
e = Estudiante(nombre="Ana", semestre="4")  # semestre="4" se convierte a 4
print(e.semestre)  # 4 (int, no string)
print(type(e.semestre))  # <class 'int'>

# Si no puede convertir → ValidationError
e2 = Estudiante(nombre="Ana", semestre="cuatro")  # ← error
```

**¿Por qué `BaseModel`?** Herencia de clases. `BaseModel` tiene toda la lógica de validación. Tu clase hereda esa lógica y solo define qué campos quieres.

**Pydantic v1 vs v2:** FastAPI moderno usa Pydantic v2 (escrito en Rust, 5-50x más rápido). Algunas cosas cambiaron (ej: `.dict()` → `.model_dump()`). Si un estudiante ve errores de deprecación, es porque el ejemplo usa la API vieja.

### ¿Por qué `response_model`?

```python
@app.get("/estudiantes", response_model=list[EstudianteConID])
def listar():
    return list(db.values())
```

`response_model` hace dos cosas:
1. **Filtra** la respuesta — si tu objeto tiene campos sensibles (contraseña, tokens), los excluye si no están en el modelo de respuesta
2. **Documenta** — le dice a Swagger qué campos tiene la respuesta

Ejemplo de seguridad:
```python
class EstudianteDB(BaseModel):
    nombre: str
    email: str
    password_hash: str  # ← no queremos exponerlo

class EstudiantePublico(BaseModel):
    nombre: str
    email: str
    # no tiene password_hash

@app.get("/estudiantes/{id}", response_model=EstudiantePublico)
def obtener(id: int):
    return db[id]  # devuelve EstudianteDB pero response_model filtra password_hash
```

### ¿Por qué 201 y no 200 para crear?

Por semántica HTTP. El protocolo define códigos específicos:
- `200 OK` — la operación fue exitosa (lectura, actualización)
- `201 Created` — se creó un nuevo recurso

Los clientes pueden usar esto para comportarse diferente:
- Una app puede mostrar "Guardado" para 200 y "Nuevo registro creado" para 201
- Algunos frameworks frontend procesan automáticamente el header `Location` que debería acompañar un 201

```python
# FastAPI te permite especificar el status_code por defecto:
@app.post("/estudiantes", status_code=201)  # ← explícito
def crear(est: Estudiante):
    ...
```

### ¿Qué es OpenAPI y cómo genera FastAPI los docs?

FastAPI genera un archivo JSON en `localhost:8000/openapi.json` que describe toda tu API:
- Qué endpoints existen
- Qué parámetros acepta cada uno
- Qué respuestas devuelve
- Los esquemas Pydantic

Ese archivo sigue el estándar **OpenAPI 3.0** (antes llamado Swagger). Swagger UI lee ese JSON y genera la interfaz interactiva.

Puedes exportar ese JSON y usarlo para:
- Generar código cliente automáticamente (ej: TypeScript SDK para tu frontend)
- Importar en Postman
- Documentación en plataformas como Readme.io o Stoplight

### ¿Qué es CORS y por qué bloquea Streamlit?

CORS (Cross-Origin Resource Sharing) es una política de seguridad del navegador:

> "Si una página web en `localhost:8501` intenta hacer una petición a `localhost:8000`, el navegador la bloquea por defecto. El servidor (FastAPI) debe explícitamente permitirlo."

**¿Por qué existe?** Para evitar que un sitio malicioso (`malo.com`) haga peticiones a `tubanco.com` usando tus cookies ya almacenadas.

**Solución en FastAPI:**
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Streamlit
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)
```

En producción, nunca pongas `allow_origins=["*"]` si tu API maneja datos sensibles.

**¿Por qué Streamlit no tiene este problema con APIs externas?** Porque Streamlit hace la petición desde Python (servidor), no desde el navegador (cliente). CORS solo aplica a peticiones desde el navegador.

---

## Preguntas frecuentes — cómo responderlas

### "¿Por qué necesito un diccionario como base de datos y no SQLite?"

No necesitas, es una simplificación pedagógica. En producción usarías:
```
dict en memoria → se borra al reiniciar el servidor
SQLite → archivo en disco, persiste, ideal para proyectos pequeños
PostgreSQL → base de datos real, múltiples conexiones, para producción
```

FastAPI se integra con bases de datos via `SQLAlchemy` o `Tortoise ORM`. El CRUD es prácticamente idéntico, solo cambia de dónde viene y a dónde va el dato.

### "¿Puede FastAPI manejar archivos (imágenes, PDFs)?"

Sí:
```python
from fastapi import UploadFile, File

@app.post("/upload")
async def subir_archivo(archivo: UploadFile = File(...)):
    contenido = await archivo.read()
    # guardar en disco o en S3...
    return {"filename": archivo.filename, "size": len(contenido)}
```

### "¿Qué diferencia hay entre PUT y PATCH?"

```
PUT   → Reemplaza el objeto COMPLETO
        Si olvidas un campo, ese campo queda vacío/null

PATCH → Modifica SOLO los campos que envías
        Los campos no enviados se mantienen igual
```

Ejemplo práctico:
```python
# Estudiante existente: {nombre: "Ana", carrera: "Sistemas", semestre: 4}

# PUT /estudiantes/1 con {nombre: "Ana García"}
# → Resultado: {nombre: "Ana García", carrera: null, semestre: null}
# ← Perdiste carrera y semestre!

# PATCH /estudiantes/1 con {nombre: "Ana García"}
# → Resultado: {nombre: "Ana García", carrera: "Sistemas", semestre: 4}
# ← Solo cambió el nombre
```

### "¿FastAPI puede hacer autenticación (login)?"

Sí, con `fastapi.security` y `python-jose` para JWT:

```python
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/mi-perfil")
def mi_perfil(token: str = Depends(oauth2_scheme)):
    # verificar token...
    return {"usuario": "Ana"}
```

Eso es un tema aparte (FastAPI tiene documentación excelente sobre auth).

### "¿Qué es `async def` vs `def` en FastAPI?"

```python
# Síncrono — FastAPI lo ejecuta en un thread pool
@app.get("/sync")
def endpoint_sync():
    return {"ok": True}

# Asíncrono — FastAPI lo ejecuta en el event loop
@app.get("/async")
async def endpoint_async():
    return {"ok": True}
```

Para principiantes: usa `def` normal. Usa `async def` solo si usas librerías asíncronas (aiohttp, databases, tortoise-orm). Mezclar `async def` con código síncrono bloqueante (como `requests.get()`) puede crear problemas de rendimiento.

### "¿Por qué no usar Flask en vez de FastAPI?"

Ambas son válidas. Razones para elegir FastAPI hoy:
- Validación automática → menos bugs
- Docs automáticas → menos trabajo de documentación
- Más rápido → menos servidores en producción
- Type hints → mejor autocompletado en IDEs
- Async nativo → mejor para operaciones I/O intensivas

Flask sigue siendo útil para: proyectos legacy, cuando todo el equipo lo conoce, apps web completas (no solo APIs).

---

## Estructura del proyecto FastAPI para producción

```
mi_proyecto/
├── main.py              ← punto de entrada
├── routers/
│   ├── estudiantes.py   ← endpoints de estudiantes
│   └── cursos.py        ← endpoints de cursos
├── models/
│   └── schemas.py       ← modelos Pydantic
├── database/
│   └── db.py            ← conexión a la base de datos
├── requirements.txt
└── .env                 ← variables de entorno (API keys, DB URL)
```

Para la clase mostramos todo en `main.py` por simplicidad. En proyectos reales se separa.

---

## Errores comunes de estudiantes

| Error | Causa | Solución |
|-------|-------|----------|
| `ImportError: cannot import name 'FastAPI'` | No instalaron fastapi | `pip install fastapi uvicorn` |
| `Address already in use` | El puerto 8000 ya está ocupado | `uvicorn main:app --port 8001` o matar el proceso |
| `422 Unprocessable Entity` | Los datos no coinciden con el modelo | Revisar nombres de campos en el body |
| `AttributeError: 'dict' has no attribute 'id'` | El ORM devuelve objeto, no dict | Usar `model.id` en vez de `model["id"]` |
| CORS bloqueado desde Streamlit | No agregaron middleware CORS | Agregar `CORSMiddleware` |
| Los cambios no se reflejan | Olvidaron el `--reload` | Siempre usar `--reload` en desarrollo |
| `global` no funciona con workers | Usaron `--workers 2` con diccionario en memoria | Con múltiples workers, la memoria no se comparte |

---

## Analogías para clase

**FastAPI como restaurante:**
- Los endpoints (`@app.get`) son las entradas del menú
- Pydantic es el/la chef que verifica que los ingredientes del pedido son los correctos antes de cocinar
- Uvicorn es el edificio del restaurante: sin él, el menú no tiene dónde existir
- Swagger UI es la carta impresa que ven los clientes

**Pydantic como formulario de admisión:**
- Defines qué campos son obligatorios y de qué tipo
- Si alguien llena "cuatro" donde va un número → el formulario se rechaza automáticamente
- No tienes que revisar cada campo manualmente

**Decoradores como carteles en la puerta:**
- `@app.get("/estudiantes")` = cartel que dice "ENTRADA por aquí para GET"
- `@app.post("/estudiantes")` = cartel que dice "DEPOSITAR pedidos aquí"
- Sin decorador, la función existe pero nadie sabe cómo llegar a ella

---

## Datos de trivia

- FastAPI fue creado por Sebastián Ramírez, colombiano, lo lanzó en 2018
- Es el framework de Python que más creció en GitHub stars en 2020-2022
- FastAPI se usa en producción en: Netflix (scripting interno), Microsoft (Machine Learning), Uber (datos de mapas)
- Pydantic v2 fue reescrito completamente en Rust en 2023 — es 17x más rápido que Pydantic v1
- El nombre "Uvicorn" viene de: ASGI + monocorn (unicornio) → uvicorn
- `localhost:8000/openapi.json` es el "contrato" de tu API — puedes pegarlo en editor.swagger.io para verlo visualmente

---

## Recursos para profundizar

- FastAPI docs (excelentes): `fastapi.tiangolo.com`
- Tutorial oficial FastAPI: incluye autenticación, bases de datos, async
- Pydantic docs: `docs.pydantic.dev`
- ASGI explicado: `asgi.readthedocs.io`
- HTTPie (como curl pero más amigable para probar APIs): `httpie.io`
- Postman (cliente gráfico para probar APIs): `postman.com`
