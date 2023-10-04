//Run the server

 python3 manage.py runserver



pip3 install virtualenv

virtualenv venv

source venv/bin/activate

pip3 install django

django-admin startproject project_name

python3 manage.py startapp app_name

//chosen the database sqlite here

python3 manage.py migrate


//Create the superuser

python3 manage.py createsuperuser

admin/12345678


//Database make migration

 python3 manage.py makemigrations

//Migrate after creation model

 python3 manage.py migrate

//disable the virtual environment

deactivate

