# drf-project-oreilly-course

python3.10 -m venv .venv       
source .venv/bin/activate     

pip install djangorestframework
pip install django         
pip freez    

django-admin startproject watchmate .  
python manage.py startapp watchlist_app


python manage.py createsuperuser
python manage.py runserver
python manage.py migrate  
python manage.py makemigrations

