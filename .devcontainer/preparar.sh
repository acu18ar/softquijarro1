#!/usr/bin/env bash
# Se ejecuta una sola vez, al crear el Codespace.
set -e
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos_demo
python manage.py asegurar_admin
echo ""
echo "========================================================"
echo " Listo. Para arrancar el sistema escribe:"
echo "     python manage.py runserver"
echo " Usuario: admin   Contraseña: admin123"
echo "========================================================"
