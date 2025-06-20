release: python manage.py collectstatic --noinput
web: gunicorn blogproject.wsgi --bind 0.0.0.0:${PORT:-8000} --timeout 120 --workers 1 