sudo easy_install PyJWT
python manage.py syncdb # be sure to create superuser
python manage.py runserver 8080 
# login as superuser and create some users