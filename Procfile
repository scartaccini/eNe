release: python manage.py migrate --noinput
web: gunicorn WORKSPACE.wsgi:application --log-file -