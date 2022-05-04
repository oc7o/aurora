#!/bin/sh

set -e

# echo "Collect static files"
# python manage.py collectstatic --noinput

echo "Make database migrations"
python manage.py makemigrations --noinput

echo "Apply database migrations"
python manage.py migrate


# echo "Creating superuser"
# echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser(username='admin', name='', email='', password='1234Password', is_active=True)" | python manage.py shell

if [ $DEBUG = 1 ]
then
    echo "Running Development"
    python manage.py runserver 0.0.0.0:8000
else
    echo "Running Production"
    uwsgi --socket :8000 --master --enable-threads --module djangoserver.wsgi
fi

