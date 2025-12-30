#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Instalar librerías
pip install -r requirements.txt

# 2. Recolectar archivos estáticos
python manage.py collectstatic --no-input

# 3. --- MIGRACIONES (ESTO ARREGLA EL ERROR 500) ---
python manage.py makemigrations
python manage.py migrate

# 4. --- CREAR SUPERUSUARIO ALAN ---
# Crea el usuario 'alan' si no existe.
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='alan').exists() or \
User.objects.create_superuser('alan', 'alan@admin.com', 'admin123')" \
| python manage.py shell