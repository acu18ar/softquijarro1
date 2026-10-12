# Guía del estudiante — Proyecto SoftQuijarro S.R.L.

Vas a construir, con 4 compañeros, el sistema de ventas de una ferretería. Cada uno es
dueño de **un módulo** (una carpeta). Integran su trabajo por GitHub, como en una empresa.

> **Lo que se evalúa no es solo el código:** es cómo planificas, estimas, te coordinas y
> entregas. Puedes usar IA, pero tienes que poder explicar cada línea que subes.

---

## 1. Antes de la primera clase (tarea, 20 min)

1. Crea una cuenta en <https://github.com> (si no tienes) y envía tu usuario al docente.
2. Acepta la invitación al repositorio `softquijarro` (te llega al correo; también está
   en <https://github.com/notifications>).
3. En el repositorio: botón verde **Code** → pestaña **Codespaces** →
   **Create codespace on main**. Se abre VS Code en el navegador.
4. Espera a que la terminal de abajo diga **"Listo"** (unos 3 minutos la primera vez).
5. Escribe:
   ```bash
   python manage.py runserver
   ```
6. Aparece un aviso **Open in Browser** (o pestaña **Ports** → globo junto al 8000).
7. Entra con **admin / admin123**. Si ves el tablero de la ferretería, ya estás listo.
8. Para salir: *Code* → *Codespaces* → ⋯ → **Stop codespace**. (Tienes 60 h gratis al mes.)

La próxima vez, en *Code* → *Codespaces* aparece tu Codespace: ábrelo desde ahí, no crees
otro.

---

## 2. Reglas de oro

1. **Solo tocas archivos de tu carpeta** (`clientes/`, `productos/`, etc.). La verificación
   automática rechaza el pull request si tocas otra cosa.
2. **Nunca trabajes en `main`.** Cada historia va en su propia rama.
3. **No borres ni renombres los CAMPOS BASE** de tu modelo: otro compañero los usa.
4. **Todo campo nuevo es opcional** (`blank=True`, `null=True` o un `default`).
5. **Si cambias un modelo, subes la migración** en el mismo pull request.
6. **Si necesitas algo compartido** (una librería, un cambio en `settings.py`), abre una
   Issue para el docente. No lo hagas tú.

---

## 3. El ciclo de cada historia

Abre la terminal del Codespace (<kbd>Ctrl</kbd>+<kbd>ñ</kbd> o menú *Terminal → New Terminal*).

### a) Partir de la última versión
```bash
git checkout main
git pull
python manage.py migrate
```

### b) Crear tu rama
Usa el código de la historia y unas palabras:
```bash
git checkout -b c1-telefono-correo
```

En el tablero (**Projects**), mueve tu tarjeta a **In Progress**.

### c) Programar y probar
```bash
python manage.py runserver
```
Si cambiaste `models.py`:
```bash
python manage.py makemigrations
python manage.py migrate
```
Corre tus pruebas:
```bash
python manage.py test clientes      # ← tu módulo
```

### d) Guardar y subir
```bash
git add .
git commit -m "C1: agrega teléfono y correo al cliente"
git push -u origin c1-telefono-correo
```

### e) Abrir el pull request
1. En GitHub aparece un aviso amarillo **Compare & pull request**. Haz clic.
2. Llena la plantilla. En **Closes #** pon el número de tu Issue (así se cierra sola).
3. **Create pull request**.
4. Espera 1–2 minutos a las verificaciones:
   - ✅ **Solo tocaste tu carpeta**
   - ✅ **El sistema funciona**
5. Si sale ❌, haz clic en **Details**: dice qué pasó y cómo arreglarlo. Corriges, haces
   `git add .`, `git commit`, `git push` y se vuelve a verificar solo.
6. En la revisión explicas tu PR en voz alta. El docente lo aprueba y hace el *merge*.

### f) Después del merge
```bash
git checkout main
git pull
python manage.py migrate
```
En pocos minutos tu cambio aparece publicado en el servidor (mira la versión en el pie de
página).

---

## 4. Dónde va cada cosa dentro de tu carpeta

```
clientes/
├── apps.py          ← tu nombre como responsable y el estado del módulo
├── models.py        ← tus campos nuevos (debajo de los CAMPOS BASE)
├── migrations/      ← se generan solas con makemigrations; se suben siempre
├── views.py         ← la lógica de tus páginas
├── urls.py          ← tus rutas (ya quedan bajo /clientes/)
├── forms.py         ← (créalo si haces formularios)
├── templates/clientes/  ← tus páginas HTML; empiezan con {% extends "base.html" %}
├── datos_demo.py    ← tus datos de prueba
├── admin.py         ← cómo se ve tu modelo en /admin
└── tests.py         ← tus pruebas automáticas
```

Cuando tu módulo esté terminado, en `apps.py` cambia `estado = "listo"`: la tarjeta del
tablero se pone en verde.

---

## 5. Errores comunes

| Mensaje | Qué pasó | Solución |
|---|---|---|
| ❌ *Solo tocaste tu carpeta*: "modifica archivos de otros" | Cambiaste un archivo fuera de tu carpeta (a veces la IA "arregla" `settings.py` o `urls.py`) | `git checkout origin/main -- config/settings.py` (el archivo que diga), luego commit y push |
| ❌ "Cambiaste un modelo pero no subiste la migración" | Olvidaste `makemigrations` | `python manage.py makemigrations`, `git add .`, commit, push |
| ❌ Falla una prueba de **contrato** | Borraste o renombraste un CAMPO BASE, o tus datos de prueba fallan | Lee el mensaje: dice qué campo. Devuélvelo a como estaba |
| `no such table` o `no such column` en tu Codespace | Tu base local no tiene las últimas migraciones | `python manage.py migrate` |
| `Updates were rejected` al hacer push | Estás en `main` o tu rama está atrasada | `git status` para ver tu rama; nunca hagas push a `main` |
| La página no carga en el navegador | El servidor no está corriendo | `python manage.py runserver` |

---

## 6. Sobre el uso de IA

Sí puedes usarla. Tres condiciones:
- Pídele que trabaje **solo dentro de tu carpeta**. Si te propone cambiar `settings.py`,
  `config/urls.py` o la plantilla base, dile que no: pídelo al docente por Issue.
- En tu pull request indica **para qué la usaste** y **qué tuviste que corregir**.
- Si en la revisión no puedes explicar tu código, el PR se devuelve.

---

## 7. Las ceremonias

- **Planificación:** eliges tus historias del sprint y las estimas en puntos.
- **Daily (10 min):** ¿qué hice?, ¿qué haré?, ¿qué me bloquea? Si algo te bloquea, crea
  una Issue con la plantilla **Impedimento**.
- **Revisión:** muestras tus historias funcionando en el servidor publicado.
- **Retrospectiva:** qué empezar, qué dejar de hacer, qué seguir haciendo.
