Instalacja Python --> python-3.4.3.amd64.msi
Podczas instalacji zaznaczyć wszystkie opcje (jedna jest odznaczona, trzeba ja zaznaczyć)
potem w CMD wpisujemy: 	pip install django==1.9
			easy_install Pillow
Następnie w cmd wchodzimy do folderu BLOG, tam gdzie jest manage.py i wpisujemy po kolei:
			python manage.py makemigrations
			python manage.py migrate
			python manage.py createsuperuser     --> Tutaj prosi nas o podanie emailu admina oraz hasła

I odpalamy serwer komendą: python manage.py runserver
Pojawi się link, najprawdopodobniej taki:  http://127.0.0.1:8000/ który wpisujemy w przeglądarke.


http://www.python.rk.edu.pl/w/p/wprowadzenie-do-django-10/

				
