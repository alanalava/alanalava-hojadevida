#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# 4. Crear tu Superusuario (SOLO SI NO EXISTE)
# He puesto 'alan' como usuario y 'admin123' como contraseña.
# ¡CÁMBIALOS AQUÍ ABAJO SI QUIERES! 👇
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='alan').exists() or \
User.objects.create_superuser('alan', 'alan@admin.com', 'admin123')" \
| python manage.py shell