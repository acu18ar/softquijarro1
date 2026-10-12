#!/usr/bin/env bash
# Render ejecuta este archivo en cada despliegue (cada merge a main).
# ⚠️ Archivo del docente.
set -o errexit
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py cargar_datos_demo
python manage.py asegurar_admin
