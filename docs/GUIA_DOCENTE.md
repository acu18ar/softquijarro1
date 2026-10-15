# Guía del docente — Práctica Scrum + GitHub «SoftQuijarro S.R.L.»

Gestión Estratégica de Proyectos de Software · UNITEPC · Ing. Ariel Acuña Apaza

Tú **no programas**. El sistema ya funciona: tiene login, menú, 5 módulos con datos de
prueba, verificación automática y despliegue en internet. Tu trabajo es **montarlo una vez**
(≈ 1 hora, solo clics) y luego **dirigir el proyecto** como Product Owner.

---

## 1. Qué hay en el repositorio

| Carpeta / archivo | Dueño | Para qué sirve |
|---|---|---|
| `clientes/` | Estudiante 1 (seguro) | Registro y búsqueda de clientes |
| `productos/` | Estudiante 2 (seguro) | Catálogo, precio, stock |
| `facturacion/` | Estudiante 3 (seguro, el más fuerte) | Emitir facturas, descontar stock |
| `proveedores/` | Estudiante 4 (puede faltar) | Proveedores y qué surten |
| `reportes/` | Estudiante 5 (puede faltar) | Ventas, más vendidos, clientes frecuentes |
| `config/`, `core/`, `templates/`, `.github/`, `.devcontainer/`, `render.yaml`, `build.sh`, `requirements.txt` | **Docente** | Configuración común. Ningún estudiante la toca |

**Por qué no habrá conflictos de Git:** cada estudiante solo puede modificar su carpeta.
Una verificación automática rechaza cualquier pull request que toque otra cosa, y explica
al estudiante cómo arreglarlo. Esto ya se probó: tres estudiantes cambiaron sus modelos en
paralelo, se fusionaron las tres ramas y no hubo ni un conflicto.

**Por qué nadie queda bloqueado:** los modelos de Cliente, Producto y Factura ya existen
con datos de prueba (8 clientes, 10 productos, 4 proveedores, 15 facturas). Facturación
puede trabajar el primer día sin esperar a nadie, y Reportes tiene ventas para mostrar.

**Por qué el sistema no se rompe si falta alguien:** los módulos de los dos estudiantes
inciertos (Proveedores y Reportes) son "hojas": nadie depende de ellos. Si no entregan, su
tarjeta en el tablero dice "En construcción" y el resto funciona igual.

---

## 2. Montaje (una sola vez, ≈ 1 hora)

Hazlo **una semana antes de la Clase 1, no antes** (la base de datos gratuita dura 30 días).

### Paso 1 · Crear el repositorio (5 min)
1. Entra a <https://github.com> con tu cuenta.
2. Botón verde **New** (o el **+** arriba a la derecha → *New repository*).
3. Nombre: `softquijarro`. Marca **Public**. **No** marques "Add a README".
4. **Create repository**.

> **Por qué público:** la protección de la rama `main` es gratis solo en repositorios
> públicos. Para un proyecto de clase no hay inconveniente.

### Paso 2 · Subir los archivos (10 min)
**Opción A (la más fácil):** dile a Claude el nombre del repositorio
(`tu-usuario/softquijarro`) y lo sube por ti.

**Opción B (manual):**
1. En el repositorio vacío, haz clic en **uploading an existing file**.
2. Descomprime el ZIP en tu computadora. Abre la carpeta `softquijarro`.
3. Selecciona **todo su contenido**, **incluidas** las carpetas `.github` y `.devcontainer`
   (empiezan con punto; en Mac aparecen con <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>.</kbd>).
4. Arrástralo a la página. GitHub acepta hasta 100 archivos por vez. Si se queja, sube
   primero la carpeta `core` sola, haz *Commit changes*, y luego todo lo demás.
5. Escribe "Esqueleto inicial" y **Commit changes**.

✔ Comprobación: en la página del repositorio ves `.github`, `.devcontainer`, `clientes`,
`core`… y abajo el README con la captura del tablero.

### Paso 3 · Registrar al equipo (5 min)
1. Pide a cada estudiante su **usuario de GitHub** (deben crear cuenta si no tienen).
2. En el repositorio abre `.github/equipo.json` → ícono del **lápiz** (Edit).
3. Reemplaza `USUARIO_DOCENTE` por tu usuario y cada `USUARIO_…` por el del estudiante
   que tendrá ese módulo. Ejemplo:
   ```json
   "docente": "arielacuna",
   "estudiantes": {
     "juanmamani": ["clientes"],
     ...
   ```
4. **Commit changes**.
5. Edita también `README.md` y llena la tabla del equipo.

### Paso 4 · Invitar a los estudiantes (5 min)
*Settings* → *Collaborators* → **Add people** → escribe el usuario de cada uno.
Les llega un correo; **deben aceptar la invitación** (es la tarea previa de la Clase 1).

### Paso 5 · Crear el tablero y el backlog (10 min)
1. Pestaña **Projects** del repositorio → **New project** → plantilla **Board** →
   nombre `Sprint SoftQuijarro` → *Create*.
2. Dentro del proyecto: menú **⋯** → **Workflows** → **Auto-add to project** →
   *Edit* → repositorio `softquijarro`, filtro `is:issue` → **Save and turn on workflow**.
3. Vuelve al repositorio → pestaña **Actions** → a la izquierda **Crear backlog** →
   botón **Run workflow** → **Run workflow**.
4. Espera 1 minuto. En **Issues** aparecen las 24 historias, con su sprint y su módulo,
   y también llegan solas al tablero.

### Paso 6 · Publicar en internet con Render (15 min)
1. Entra a <https://render.com> → **Get Started** → **Sign in with GitHub**.
2. Arriba: **New** → **Blueprint** → elige el repositorio `softquijarro` → *Connect*.
3. Render lee el archivo `render.yaml` y te pide dos datos:
   - `ADMIN_USUARIO`: el usuario con el que entrarás al sistema publicado (ej. `docente`).
   - `ADMIN_CLAVE`: una contraseña.
4. **Apply** (o *Deploy Blueprint*). Tarda 5–8 minutos la primera vez.
5. Cuando el servicio `softquijarro` diga **Live**, abre su dirección
   (algo como `https://softquijarro.onrender.com`). Pon esa dirección en el README.

Desde ahora, **cada merge a `main` se publica solo**, pero únicamente si la verificación
automática pasó. El pie de página del sistema muestra la versión publicada (los 7
primeros caracteres del último commit), así los estudiantes ven aparecer su cambio.

> **Límites del plan gratuito:** el servidor "se duerme" tras 15 minutos sin visitas y
> tarda ~1 minuto en despertar → ábrelo 2 minutos antes de la clase. La base de datos
> gratuita **vence a los 30 días**; para tres clases alcanza.

### Paso 7 · Proteger la rama `main` (5 min)
*Settings* → *Branches* → **Add classic branch protection rule**:
- *Branch name pattern*: `main`
- ✅ **Require a pull request before merging** → ✅ *Require approvals*: **1**
- ✅ **Require status checks to pass before merging** → busca y agrega
  **«Solo tocaste tu carpeta»** y **«El sistema funciona»**.
- **Create**.

> Las verificaciones solo aparecen en el buscador después de que corrieron una vez.
> «El sistema funciona» ya corrió al subir los archivos. «Solo tocaste tu carpeta» corre
> con el primer pull request: si no aparece, **vuelve a este paso después del primer PR
> de la Clase 1** y agrégala.

Como administrador, tú sí puedes seguir editando archivos directamente en `main`
(por ejemplo `equipo.json`).

### Paso 8 · Prueba general (10 min)
1. En el repositorio: botón verde **Code** → pestaña **Codespaces** →
   **Create codespace on main**. Espera ~3 minutos.
2. En la terminal de abajo escribe `python manage.py runserver`.
3. Aparece un aviso "Open in Browser" (o pestaña **Ports** → ícono del globo en el 8000).
4. Entra con **admin / admin123**. Si ves el tablero con los 5 módulos, todo está listo.
5. Cierra el Codespace: *Code* → *Codespaces* → ⋯ → **Stop codespace**.

---

## 3. Roles

| Rol | Quién | Qué hace |
|---|---|---|
| **Product Owner** | Docente (el dueño de la ferretería) | Prioriza, acepta o rechaza historias, pide cambios, aprueba los pull requests |
| **Scrum Master** | Rota: Estudiante 1 → 2 → 3 (uno por clase) | Conduce el daily, mantiene el tablero al día, atiende impedimentos. Además sigue con su módulo |
| **Equipo de desarrollo** | Los 5 | Cada uno su módulo |

Los dos estudiantes inciertos no son Scrum Master: si faltan, no se cae la ceremonia.

---

## 4. Tarea previa a la Clase 1 (para los estudiantes)

Envíala con anticipación por el grupo del curso. Es lo que hace que la Clase 1 no se
pierda en instalaciones.

1. Crear cuenta en GitHub y mandarte el usuario.
2. Aceptar la invitación al repositorio (llega al correo).
3. Abrir el Codespace una vez y comprobar que el sistema arranca
   (`docs/GUIA_ESTUDIANTE.md`, sección 1).

---

## 5. Guion de las tres clases (1 hora útil cada una)

Cada clase es un sprint. El código puede avanzar entre clase y clase; **en clase se hacen
las ceremonias y la integración**.

### Clase 1 · Sprint 1 — Arranque
| Min | Actividad | Tú (PO) |
|---|---|---|
| 0–10 | **Planificación del sprint.** Visión del producto, recorrido del tablero. Cada uno toma sus tarjetas del Sprint 1 (X0 y X1), las estima con los dedos (1, 2, 3, 5, 8) y anota los puntos en la Issue | Explicas qué quiere el dueño de la ferretería |
| 10–25 | **Primer pull request, todos juntos:** historia X0 (poner su nombre en `apps.py`). Proyectas la guía del estudiante y lo hacen paso a paso | Apruebas y haces *merge* de cada PR en vivo |
| 25–50 | Historia X1 (agregar campos + migración) | Recorres puestos |
| 50–60 | Cada uno explica su PR en voz alta (máx. 2 min) → apruebas → *merge*. Abren la URL de Render y ven sus nombres en el tablero | Aceptas o devuelves |

**Meta mínima:** cada presente con al menos 1 merge (X0). Tarea: terminar X1.

### Clase 2 · Sprint 2 — Construcción y pedido de cambio
| Min | Actividad | Tú (PO) |
|---|---|---|
| 0–10 | **Daily** conducido por el Scrum Master de turno: ¿qué hice?, ¿qué haré?, ¿qué me bloquea? Mueve las tarjetas | Observas, no intervienes |
| 10–20 | **Pedido de cambio** (ver sección 6). Lo creas como Issue con la plantilla "Pedido de cambio". El equipo completa el análisis de impacto y propone qué sale del sprint | Decides |
| 20–50 | Trabajo en historias del Sprint 2 | Atiendes impedimentos |
| 50–60 | Merges. Revisan en el tablero cuántas historias del sprint están cerradas vs. abiertas | Aceptas |

### Clase 3 · Sprint 3 — Lanzamiento y cierre
| Min | Actividad | Tú (PO) |
|---|---|---|
| 0–10 | Daily y últimos merges | |
| 10–30 | **Revisión del sprint sobre la URL pública.** Cada responsable muestra sus historias; tú pruebas contra los criterios de aceptación y aceptas o rechazas | Cliente exigente |
| 30–45 | **Retrospectiva:** en el pizarrón, tres columnas: *Empezar / Dejar de / Seguir haciendo*. Comparan las horas estimadas vs. reales de sus PR | Facilitas |
| 45–60 | **Cierre formal del proyecto:** en GitHub → *Releases* → **Draft a new release** → etiqueta `v1.0` → *Generate release notes* → **Publish**. Las notas listan cada PR con su autor: es el acta de entrega | Firmas el cierre |

### Relación con el temario
| Lo que pasa en la práctica | Tema |
|---|---|
| Roles, Scrum Master rotativo, PO | T14 lado humano · T15 organización · T16 jefe del proyecto |
| Docente como cliente que acepta o rechaza | T18 gestión de los implicados |
| Pedido de cambio con análisis de impacto | T19 gestión del cambio |
| Despliegue automático en Render | T21 lanzamiento del proyecto |
| Daily, tablero, impedimentos | T22 gestión del día a día |
| Historias cerradas vs. abiertas, estimado vs. real | T23 seguimiento y control · T13 estimación |
| Release `v1.0` + retrospectiva | T25 cierre ordinario |

---

## 6. Pedidos de cambio sugeridos (Clase 2)

Elige uno. No lo anuncies antes: la gracia es que llegue a mitad del sprint.

1. **(Recomendado) "Toda factura debe registrar la forma de pago: efectivo, QR o tarjeta,
   y quiero ver cuánto entra por cada una."** Afecta a Facturación y Reportes → obliga a
   coordinar dos personas. Si falta el de Reportes, el equipo debe decidir si se posterga.
2. **"El teléfono del cliente ahora es obligatorio."** Afecta solo a Clientes, pero hay
   clientes ya registrados sin teléfono: ¿qué se hace con ellos? (lección de migraciones).
3. **"Quiero el precio de los productos con y sin IVA (13 %)."** Afecta a Productos y,
   si se decide, a Facturación.

---

## 7. Contingencias

| Situación | Qué hacer |
|---|---|
| Falta un estudiante incierto | Nada. Su módulo queda "En construcción" |
| Falta un estudiante seguro | El Scrum Master reasigna su tarjeta en el daily. Tú editas `.github/equipo.json` y agregas esa carpeta a la lista del compañero que la toma: `"juanmamani": ["clientes", "productos"]` |
| Falta el Scrum Master de turno | Lo toma el siguiente de la rotación |
| A un estudiante no le abre el Codespace o no tiene internet | Trabaja en pareja con el dueño de la carpeta, en el Codespace de este |
| La verificación sale en rojo ❌ | El estudiante hace clic en **Details**: el mensaje dice qué hizo mal y cómo arreglarlo |
| Render no responde | Espera 1 minuto (estaba dormido). Si sigue sin responder, haz la demo desde tu Codespace |
| Se acabaron las horas de Codespaces | No debería pasar: son 60 h al mes por estudiante. Recuérdales hacer *Stop codespace* al terminar |

---

## 8. Evaluación con evidencia de GitHub

Todo queda registrado con nombre y fecha. Dónde mirarlo:
- **Pull requests** → filtro `author:usuario` → qué entregó cada uno y cómo lo describió.
- **Issues** → filtro `milestone:"Sprint 1"` → historias cerradas por sprint.
- **Insights** → **Contributors** → commits por persona.

| Criterio | Pts | Evidencia |
|---|---|---|
| Historias aceptadas en la revisión | 40 | Issues cerradas de su módulo |
| Calidad de sus PR: descripción, estimado vs. real, explicación oral | 20 | Pull requests |
| Integración limpia: verificación en verde, migraciones incluidas | 15 | Checks del PR |
| Participación en Scrum: daily, rol de SM, retrospectiva | 15 | Observación |
| Revisión a compañeros: al menos un comentario útil en un PR ajeno | 10 | Conversación del PR |

---

## 9. Ideas para el examen del 11 de noviembre

- "En la Clase 2 el cliente pidió registrar la forma de pago. Describa el análisis de
  impacto que hizo su equipo y la decisión tomada. ¿Qué tema de la Unidad IV aplica?"
- "Compare las horas que estimó y las que le tomaron sus historias. ¿A qué atribuye la
  diferencia? ¿Cambió algo el uso de IA?"
- "¿Por qué el sistema siguió funcionando aunque faltara un integrante? Relacione con
  gestión de riesgos."
- "Diferencia entre el Scrum Master y el jefe de proyecto, con un ejemplo de la práctica."
