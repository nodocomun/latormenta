virtualenv venv
source venv/bin/activate
pip install django

(configure SECRET_KEY in latormenta/local_settings.py)

./manage.py migrate

(this creates the db. check django reference for other options.)

./manage.py createsuperuser (creates admin user).
./manage.py runserver
