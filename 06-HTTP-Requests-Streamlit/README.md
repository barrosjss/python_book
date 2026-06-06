# Apuntes del Profe — HTTP, APIs y Streamlit

> Notas de referencia rápida para clase. Cubre preguntas difíciles, analogías y profundidad técnica.

---

## Conceptos técnicos profundos

### ¿Qué hay dentro de una petición HTTP?

Una petición HTTP no es solo una URL. Tiene tres partes:

```
GET /api/character/1 HTTP/1.1          ← línea de inicio (método + ruta + versión)
Host: rickandmortyapi.com              ← headers (metadatos)
Accept: application/json
Authorization: Bearer eyJhbGci...

                                       ← línea vacía (separador)
{"nombre": "Rick"}                     ← body (solo en POST/PUT, vacío en GET)
```

**Headers importantes:**
- `Content-Type: application/json` — le dice al servidor que el body es JSON
- `Authorization` — credenciales (tokens, API keys)
- `Accept` — qué formato acepta el cliente
- `User-Agent` — qué cliente está haciendo la petición

### ¿Por qué HTTP/1.1 y no la versión 2 o 3?

HTTP/2 y HTTP/3 existen y son más rápidos (usan multiplexing, compresión de headers). Sin embargo, HTTP/1.1 sigue siendo el más universal. `requests` usa HTTP/1.1 por defecto. Para HTTP/2 en Python se usa `httpx`.

### ¿Por qué HTTPS encripta y HTTP no?

HTTP manda texto plano. Si estás en una red WiFi pública, alguien con Wireshark (herramienta de análisis de red) puede ver exactamente qué petición hiciste y qué respuesta recibiste.

HTTPS agrega una capa TLS (Transport Layer Security) que:
1. Negocia una clave secreta entre cliente y servidor (handshake)
2. Encripta todo con esa clave
3. Verifica que el servidor es quien dice ser (certificado SSL)

**El certificado SSL** es lo que ve el navegador cuando muestra el 🔒. Quien lo emite (Entidad Certificadora como Let's Encrypt, DigiCert) garantiza la identidad del servidor.

### ¿Por qué los códigos de estado son números?

Porque son más eficientes que texto. El servidor no manda "OK" (2 bytes de texto variable), manda `200` (número fijo, fácil de comparar en código). El estándar fue definido en RFC 2616 (1999) y los números están agrupados intencionalmente:
- `1xx` — informativos (raro verlos)
- `2xx` — éxito
- `3xx` — redirección (ej: `301 Moved Permanently`)
- `4xx` — error del cliente
- `5xx` — error del servidor

---

## Preguntas frecuentes — cómo responderlas

### "¿Por qué usamos `requests` si Python tiene `urllib`?"

Python tiene `urllib` incluida, pero su API es horrible:

```python
# urllib (viene con Python) — muy verboso
import urllib.request
import json

req = urllib.request.Request("https://rickandmortyapi.com/api/character/1")
with urllib.request.urlopen(req) as response:
    datos = json.loads(response.read().decode())
```

```python
# requests — limpio y legible
import requests
datos = requests.get("https://rickandmortyapi.com/api/character/1").json()
```

`requests` fue creada en 2011 específicamente para ser la alternativa humana. No viene instalada porque Python filosóficamente incluye solo lo esencial en la librería estándar.

### "¿Por qué POST para crear y no GET?"

GET es **idempotente**: puedes hacer la misma petición 100 veces y el servidor siempre responde igual, sin cambiar nada.

POST **no es idempotente**: si haces POST 100 veces para crear un usuario, creas 100 usuarios.

Los navegadores y servidores respetan esta convención:
- Los navegadores guardan en caché respuestas GET pero nunca POST
- Los proxies no almacenan respuestas POST
- Los formularios HTML usan POST para evitar reenviar datos al refrescar

### "¿Por qué `json=nuevo` y no `data=nuevo`?"

```python
# data= → manda como form-encoded (como un formulario HTML)
# Content-Type: application/x-www-form-urlencoded
# Resultado: nombre=Rick&edad=70
requests.post(url, data={"nombre": "Rick", "edad": 70})

# json= → convierte dict a JSON + agrega Content-Type correcto automáticamente
# Content-Type: application/json
# Resultado: {"nombre": "Rick", "edad": 70}
requests.post(url, json={"nombre": "Rick", "edad": 70})
```

Las APIs REST modernas esperan JSON. Si mandas `data=`, el servidor recibe un formato diferente y probablemente responde 400 Bad Request.

### "¿Qué es `raise_for_status()` por dentro?"

Es equivalente a esto:

```python
if 400 <= r.status_code < 600:
    raise requests.exceptions.HTTPError(
        f"{r.status_code} Error: {r.reason} for url: {r.url}"
    )
```

La ventaja: no tienes que chequear manualmente cada código posible. La desventaja: lanza excepción para cualquier 4xx/5xx, incluso si quieres manejar 404 de forma especial. Mezcla de enfoques:

```python
r = requests.get(url)
if r.status_code == 404:
    return None  # manejamos 404 específicamente
r.raise_for_status()  # lanza para cualquier otro error (500, 401, etc.)
datos = r.json()
```

### "¿Qué es localhost?"

`localhost` es simplemente `127.0.0.1` — la dirección IP que siempre apunta a tu propia computadora. Es el "espejo" de red: cuando le mandas un paquete a `127.0.0.1`, te lo mandas a ti mismo.

También existe `::1` (IPv6) que hace lo mismo.

```python
# Estas tres son idénticas:
requests.get("http://localhost:8501")
requests.get("http://127.0.0.1:8501")
requests.get("http://[::1]:8501")
```

### "¿Qué es un puerto?"

Una computadora tiene una sola IP pero puede tener miles de servicios corriendo al mismo tiempo. Los puertos son como departamentos en un edificio: la IP es la dirección del edificio, el puerto es el número del apartamento.

- Puerto 80 → HTTP por defecto
- Puerto 443 → HTTPS por defecto
- Puerto 8000 → FastAPI (por convención)
- Puerto 8501 → Streamlit (por defecto)
- Puerto 5432 → PostgreSQL (por convención)
- Puerto 3306 → MySQL

El sistema operativo tiene 65,535 puertos disponibles (0-1023 son "well-known" y requieren permisos de admin).

### "¿Por qué JSON y no XML o CSV?"

CSV es solo para datos tabulares (filas/columnas). No puede representar estructuras anidadas.

XML puede representar estructuras complejas pero es muy verboso:
```xml
<personaje>
  <id>1</id>
  <nombre>Rick Sanchez</nombre>
  <episodios>
    <episodio>https://.../episode/1</episodio>
  </episodios>
</personaje>
```

JSON es más compacto, más fácil de parsear, y JavaScript lo nativo (JSON = JavaScript Object Notation). Como la web corre sobre JavaScript, JSON ganó la guerra de formatos en los 2000s.

### "¿Qué es una API key?"

Muchas APIs requieren autenticación. La API de Rick and Morty es pública (sin key), pero si usaras la API de OpenAI, Twitter o Google Maps necesitarías una clave:

```python
headers = {
    "Authorization": "Bearer sk-abc123...",
    # o a veces:
    "X-API-Key": "mi-api-key"
}
r = requests.get(url, headers=headers)
```

El servidor verifica la key y decide si tienes permiso. Si no tienes key o es inválida → `401 Unauthorized`.

---

## Anatomía de una URL — detalles técnicos

```
https://rickandmortyapi.com:443/api/character?name=rick&status=alive#section1
│       │                   │   │             │                      │
│       │                   │   │             └── Query string       └── Fragment (solo en navegadores)
│       │                   │   └── Path
│       │                   └── Puerto (omitido si es el default)
│       └── Host (dominio)
└── Scheme (protocolo)
```

**Subdominio vs dominio:**
- `api.github.com` — subdominio `api`, dominio `github.com`
- `rickandmortyapi.com` — sin subdominio, dominio completo

**El fragment (#)** — la parte después del `#` nunca se manda al servidor. Es solo para el navegador (scrollear a una sección de la página). Las APIs no lo usan.

---

## ¿Qué es Streamlit por dentro?

Cuando ejecutas `streamlit run app.py`, Streamlit:

1. Inicia un servidor web en el puerto 8501
2. Ejecuta tu script `app.py` de arriba a abajo
3. Cada vez que el usuario interactúa (presiona un botón, escribe algo), **re-ejecuta todo el script desde cero**
4. Construye el HTML/CSS/JS de la interfaz automáticamente
5. Manda los cambios al navegador via WebSocket

**Por eso el orden importa**: si escribes un `st.text_input()` después de un `st.button()`, el input aparece debajo del botón. El script se ejecuta de arriba a abajo.

**`st.session_state`**: como el script se re-ejecuta completamente, las variables normales se pierden. `st.session_state` persiste entre re-ejecuciones:

```python
if "contador" not in st.session_state:
    st.session_state.contador = 0

if st.button("Sumar"):
    st.session_state.contador += 1

st.write(f"Clicks: {st.session_state.contador}")
```

---

## Errores comunes de estudiantes

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'requests'` | No instalaron `requests` | `pip install requests` |
| `ConnectionError` | No hay internet o URL mal escrita | Verificar URL y conexión |
| `KeyError: 'results'` | La API no respondió con resultados (ej: 404) | Verificar status_code antes de `.json()` |
| Streamlit no recarga | Guardaron el archivo pero no con Ctrl+S | Guardar explícitamente |
| El spinner nunca desaparece | Excepción dentro del `with st.spinner()` | Agregar try/except |
| `r.json()` da error | El servidor respondió HTML, no JSON (ej: error 500 de Django) | Ver `r.text` para diagnosticar |

---

## Analogías para clase

**HTTP como el correo postal:**
- Tu código → sobre con una dirección (URL) y contenido (body)
- El servidor → destinatario que te responde con otra carta
- Los headers → información en el sobre (remitente, tipo de contenido, tamaño)

**La URL como dirección de entrega:**
- `https://` → el servicio postal que usas (DHL, FedEx)
- `rickandmortyapi.com` → la ciudad y dirección
- `/api/character/1` → el número exacto del apartamento
- `?name=rick` → instrucciones adicionales ("solo entrega si hay alguien llamado Rick")

**JSON como formulario en blanco:**
- El servidor define qué campos existen (nombre, edad, email)
- El cliente llena los campos con valores
- Python recibe el formulario ya lleno como diccionario

---

## Datos de trivia para la clase

- HTTP fue inventado por Tim Berners-Lee en 1991 (el mismo que inventó la World Wide Web)
- La primera página web sigue viva en `info.cern.ch`
- El código 418 "I'm a teapot" es real y está en el RFC 2324. Fue una broma del Día de los Inocentes de 1998 y nunca se eliminó del estándar.
- La API de Rick and Morty tiene 826 personajes, 51 episodios y 126 ubicaciones (hasta 2023)
- `requests` tiene más de 30 millones de descargas por mes en PyPI — es una de las librerías Python más descargadas de la historia

---

## Recursos para profundizar

- HTTP en detalle: MDN Web Docs → "HTTP overview"
- Cómo funciona HTTPS: "How HTTPS Works" (howhttps.works — comic interactivo)
- API de Rick and Morty: `rickandmortyapi.com/documentation`
- Streamlit docs: `docs.streamlit.io`
- HTTP Status Codes con imágenes de gatos: `http.cat`
